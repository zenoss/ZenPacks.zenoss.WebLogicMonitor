######################################################################
#
# Copyright 2009 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

import Globals
from Products.ZenModel.ZenPack import ZenPackMigration
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.migrate.MigrateUtils import migratePropertyType

class PasswordType(ZenPackMigration):
    version = Version(2, 1, 0)
    
    def migrate(self, pack):
        """
        change password zProperty to be of type 'password' and run transformer
        against it.
        """
        migratePropertyType(pack.Devices, 
                            'zWebLogicJmxManagementPassword',
                            'password')
        
