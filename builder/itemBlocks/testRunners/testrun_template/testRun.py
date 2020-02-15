# linux
#!/usr/bin/env python 3
# WINDOWS
#!C:\Python3\

__author__ = '_'
__copyright__ = "Copyright 2020, Intel Corporation"

"""


           Name:General Test run
           Author:
           Path:
           Purpose: It is the interface betwen plugings scripts, pvt system
           and test flow items
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
    Class Test run
    brief: Contain the basic structure for create test runer

"""


class testrun(object):

    def hw_check():
        """The HW is confirmating before used it"""
        pass

    def defaultSetup():
        """Here is defined all parameters to default to run the item"""
        pass

    def parser():
        """All arguments are parsed into this section"""
        pass

    def results():
        """Logs managment  """
        pass


if __name__ == '__main__':
    main()
