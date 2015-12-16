##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################


import logging
log = logging.getLogger("zen.migrate")

import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPackMigration


class MigrateTemplates(ZenPackMigration):
    version = Version(2, 2, 3)

    def migrate(self, dmd):
        log.info("Migrating WebLogic monitoring templates...")

        # Wipe out all WebLogic templates.
        for template_id in dmd.Devices.Server.WebLogic.rrdTemplates.objectIds():
            dmd.Devices.Server.WebLogic.rrdTemplates._delObject(template_id)

        # Re-import the ZenPack's objects.xml to recreate all templates.
        pack = dmd.ZenPackManager.packs._getOb('ZenPacks.zenoss.WebLogicMonitor')

        from Products.ZenModel.ZenPackLoader import ZPLObject
        ZPLObject().load(pack, dmd.getPhysicalRoot())

MigrateTemplates()