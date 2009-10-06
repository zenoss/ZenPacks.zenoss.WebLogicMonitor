###########################################################################
#
# Copyright 2009 Zenoss, Inc. All Rights Reserved.
#
###########################################################################

import logging
log = logging.getLogger("zen.migrate")

import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPackMigration
from Products.ZenModel.migrate.MigrateUtils import migratePropertyType

class MigratePassword(ZenPackMigration):
    version = Version(2, 2, 0)

    def migrate(self, dmd):
        log.info("Migrating zWebLogicJmxManagementPassword")
        migratePropertyType("zWebLogicJmxManagementPassword", dmd, "string")
        
MigratePassword()
