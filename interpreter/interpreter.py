#!/usr/bin/env python3

import argparse
import sys



class translate():
    """This is a class to get external parameters, classified and parsered it
       :param client: A handle to the :class:`simpleble.SimpleBleClient` client object that detected the device
       :type client: class:`simpleble.SimpleBleClient`

    """

    def __init__(self, **kwargs):
        """Get all parameters from the automation System
          :param bar_param: Get any external data in dictionary format
          :type a: str, optional
        """
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
class Descriptor(object):

    def __init__(self, name =''):
        self.name = name

    def __get__(self, obj, objtype):
        return "{}for{}".format(self.name, self.name)

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")





if __name__ == '__main__':
    name = Descriptor()
    help(translate)  # to access Class docstring
    help(translate.identify)  # to access method's docstring
    help(translate.compare)  # to access method's docstring
