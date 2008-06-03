######################################################################
#
# Copyright 2007 Zenoss, Inc.  All Rights Reserved.
#
######################################################################
import Globals
import os
from Products.CMFCore.DirectoryView import registerDirectory
from Products.ZenModel.ZenPack import ZenPackBase

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

class ZenPack(ZenPackBase):
    "ZenPack Loader that loads zProperties used by WebLogic Monitor"
    packZProperties = [
        ('zWebLogicJmxManagementPort', 12347, 'int'),
        ('zWebLogicJmxManagementAuthenticate', False, 'boolean'),
        ('zWebLogicJmxManagementUsername', 'admin', 'string'),
        ('zWebLogicJmxManagementPassword', 'admin', 'string'),
        ]
