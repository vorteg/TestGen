#!/usr/bin/env python3

import argparse
import sys



class translate():
    """This is a class to get external parameters, classified and parsered it"""
    def __init__(self, **kwargs):
        """Get all parameters from the automation System"""
        bar_param = kwargs.get('c')
        print("In Bar: {}".format(bar_param))
        #: docstring for a
        a='Hola'
        print (a)

    def identify():
        """Get to internal HW information"""
        pass

    def compare():
       """Compare external parameters vs internal HW parameters"""
       pass


if __name__ == '__main__':
    help(translate)  # to access Class docstring
    help(translate.identify)  # to access method's docstring
    help(translate.compare)  # to access method's docstring
