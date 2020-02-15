#!/bin/python 3
__author__ = '_'
__copyright__ = "Copyright 2020, Intel Corporation"

"""


           Name:General Test Flow
           Author:
           Path:
           Purpose: Item that describe a general flow of the any test
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
    Class Test Flow
    brief: Contain the basic structure for create a test Flow

"""


class testFlow(object):

    def __init__(self, *args, **kwargs):
        """Parser and declare class variables"""
        self.test_name = kwargs.pop('test_name', self.__class__.__name__)

    def pre_process():
        """Method where is building the objects to be used during
         test flow stage
        """
        pass

    def test_performance_sequence():
        """Runing test flow step by step"""
        pass

    def post_process():
        """
            Method where is building the logs results in objects
            to be used at smart/fail stage
        """
        pass
