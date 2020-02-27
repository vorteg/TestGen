
import importlib
import sys

PATHMODULE='toolwrapper'

class Tools():

    def __init__(self, tool):
        self.tool_name=tool

    def select_tool(self):
        t=self.tool_name
        module = importlib.import_module(PATHMODULE + '.' + t + '.' + t)

        return module

if __name__ == '__main__':
    a=Tools('conman')
    b= a.select_tool()
    b.run()
