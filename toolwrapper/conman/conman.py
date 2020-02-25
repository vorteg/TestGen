#
#
#
__autor__ = "vorteg1"
__copyright=""
# Import Python Modules ---------------------------------------------------
import os
import sys


# Import PGKS Modules -----------------------------------------------------
from utils.features.logger.logger import logger

# Global Variables --------------------------------------------------------
CONMAN_FOLDER="ISSDCM"
#Classes -------------------------------------------------------------------
"""
     :name:ConMan
     :author: Vorteg1
     :path:/home/qupi/Documents/testgen/toolwrapper/conman/conman.py
     :purpose: Conman does the drives managment

"""
def run(*args):

    try:
        if  os.path.exists(CONMAN_FOLDR):
            logger.info("ConMan Folder does not exist")
    except Exception:
        logger.critical('Got exception on main handler', exc_info=True)
        raise

if __name__ == '__main__':
    run()
