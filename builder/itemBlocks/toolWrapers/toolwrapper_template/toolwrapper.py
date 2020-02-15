# linux
#!/usr/bin/env python 3
# WINDOWS
#!C:\Python3\

__author__ = '_'
__copyright__ = "Copyright 2020, Intel Corporation"

"""


           Name:General Tool Wrapper
           Author:
           Path:
           Purpose: Template to create a Tool Wrapper
          """

# imports
import re
import subprocess
import os
import logging

# internal varibles

_LOGGER = logging.getLogger(__name__)

INSTALL_PATH_WINDOWS = "all vablies are cap"

"""
    Class Tool
    brief: Contain the basic structure to create and managment sw tool

"""


class tool(object):

    def get_tool():
        """Findig Tools inside OS"""
        pass

    def verify_version():
        """Comparing Tools installed on Os vs database tools version """
    def config_tool():
        """Setup tools"""
        pass

    def run_tool():
        """Running tool""""
