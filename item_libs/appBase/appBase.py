#
#
#
__autor__ = "vorteg1"
__copyright=""
# Import Python Modules ---------------------------------------------------
import time
import os
import sys
import platform
import json
import argparse
import getopt

from utils.features.logger.logger import logger
"""
# Import PGKS Modules -----------------------------------------------------

from utils import app_base_consts as var
from utils.features import directories as dirs
from utils.exceptions import *
from utils import FolderManagment
# Global Variables --------------------------------------------------------
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.nsg_pv-cvt')
REFERENCE_CONFIG = os.path.join(CONFIG_DIR,'reference_config_file.json')
PLATFORM_CHOICES = var.PLATFORM_DATABASE.key()
HOST_CHOICES = ConfigDirName.host_dict.keys()
"""
#Classes -------------------------------------------------------------------

class Base(object):
    def __init__(self,*args, **kwargs):
        #Item information
        self.item_name =None
        self.item_TP = None
        #System information
        self.platform = None
        self.os = None
        self.hostname = None
        #Drives information
        self.driver = None
        self.quarch_number = None
        self.tool_drive = None
        self.host_nvme = None
        self.raid_host = None
        self.raid_target = None
        self.skip_sata =kwargs.pop('skip_sata',None)

    @classmethod
    def parser_commandline_arguments(cls, description=""):
        parser = argparse.ArgumentParser(description = description)
        parser.add_argument('--skip_sata', action='store_true',default=False,
                                                        help='Skip sata drives')
        return parser


    def test(self):
        print(self.hostname)

class BaseDecorate(object):
    @classmethod
    def initialize_variables_dec(cls,func):
        def func_wrapper(self):
            if self.initialize_variables_already:
                logger.info("Already initialize_variables_dec")
                return
            ret_val = func(self)
            self.initialize_variables_already = True
            return ret_val
        return func_wrapper


class Testing(Base):
    def __init__(self,*args,**kwargs):
        self.duration =kwargs.pop(duration, None)
        super(Testing,self).__init__(*args,**kwargs)
    @Base.BaseDecorate.initialize_variables_dec
    @classmethod
    def parser_commandline_arguments(cls, description=""):
        parser = argparse.ArgumentParser(description = description)
        parser.add_argument('--duration', type=str, default = 'default_time',
                                                        help='Skip sata drives')
        return parser

if __name__ == '__main__':


    parser=Testing.parser_commandline_arguments("testing")
    options,remaining_options = parser.parse_known_args()
    print(**(vars(options)))
    with open('unknown_args','w') as fp:
        fp.write(str(remaining_options))
    print(remaining_options)
    t=Testing(**(vars(options)))
    t.test()
    #t.test(name = 'yop', TP = 12212, platform ="wft")
