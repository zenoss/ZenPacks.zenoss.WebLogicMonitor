##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

import logging
log = logging.getLogger('zen.WebLogicMonitor')

import sys
import os.path

from Products.ZenTestCase.BaseTestCase import BaseTestCase


ZENPACK_DEPENDENCIES = (
    'ZenPacks.zenoss.WebLogicMonitor',
    )


DEVICECLASS_DEPENDENCIES = (
    '/Server/WebLogic',
    )

DEVICECLASS_TEMPLATES = (
    'WebLogic Core',
    'WebLogic JCA',
    'WebLogic JMS',
    'WebLogic JMS Destination',
    'WebLogic JTA',
    'WebLogic JTA Rollbacks',
    'WebLogic JVM',
    'WebLogic Thread Pool',
    'WebLogic Timer Service',
    'WebLogic User Lockouts',
    )

DEVICECLASS_GRAPHS = (
    'WebLogic Thread Pool Usage',
    'WebLogic JCA Pools',
    'WebLogic JMS Status',
    'WebLogic JMS Destination Message Status',
    'WebLogic Memory Usage',
    'WebLogic Thread Pool Queue Length',
    'Load Average',
    'WebLogic JMS Servers',
    'WebLogic Open Sockets',
    'WebLogic RA Pools',
    'WebLogic JMS Destination Message Status (bytes)',
    'WebLogic Thread Pool Execution',
    'WebLogic Thread Pool Throughput',
    'CPU Idle',
    'WebLogic MarkSweep GC Performance',
    'WebLogic JTA Rollback Timeout Count',
    'WebLogic User Lockouts',
    'WebLogic Restarts',
    'WebLogic JTA Rollbacks by Category',
    'Free Memory',
    'WebLogic User Authentication Failures',
    'WebLogic JMS Connections',
    'WebLogic JTA Transaction Execution Time',
    'WebLogic Daemon Threads',
    'Free Swap',
    'CPU Utilization',
    'WebLogic Scavenge GC Performance',
    'WebLogic Timer Scheduled Triggers',
    'Load Average 5 min',
    'WebLogic User Accounts',
    'WebLogic JTA Total Transactions',
    'WebLogic Timer Service Performance',
    'WebLogic JTA Transactions by Category'
    )


class TestPack(BaseTestCase):
    """
    Tests for objects loaded from ZP.
    Checks for templates and graph definitions.
    """

    def afterSetUp(self):
        super(TestPack, self).afterSetUp()
        map(self.dmd.Devices.createOrganizer, (DEVICECLASS_DEPENDENCIES))

        self.dmd.REQUEST = None

        from Products.ZenRelations.ImportRM import NoLoginImportRM
        im = NoLoginImportRM(self.app)

        for zenpack in ZENPACK_DEPENDENCIES:
            __import__(zenpack)
            zp_module = sys.modules[zenpack]

            objects_file = '%s/objects/objects.xml' % zp_module.__path__[0]

            if os.path.isfile(objects_file):
                log.info('Loading objects for %s.', zenpack)
                im.loadObjectFromXML(objects_file)

        self.dc = self.dmd.Devices.Server.WebLogic

    def testTemplates(self):
        """Verify all templates are configured properly."""
        for t_name in DEVICECLASS_TEMPLATES:
            t = self.dc.rrdTemplates._getOb(t_name, None)
            self.assertFalse(t is None)

    def testGraphDefs(self):
        """Verify all graphs are configured properly."""
        d = self.dc.createInstance('test')
        graph_defs = set([x['title'] for x in d.getDefaultGraphDefs()])
        self.assertFalse(graph_defs is None)
        self.assertEqual(len(graph_defs - set(DEVICECLASS_GRAPHS)), 0)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPack))
    return suite
