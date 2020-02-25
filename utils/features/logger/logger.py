#
#
#
__autor__ = "vorteg1"
__copyright=""
# Import Python Modules ---------------------------------------------------
import logging
# Import PGKS Modules -----------------------------------------------------
# Global variables
NAME='TestGen'
PATHFILE='/home/qupi/Documents/testgen/app.log'

#Classes -------------------------------------------------------------------
logging.basicConfig(level=logging.DEBUG,
                        filename=PATHFILE,
                            filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
                                    datefmt='%d-%b-%y %H:%M:%S')
logging.debug('%s This will get logged',NAME)
logging.warning('This will get logged to a file')

logger = logging.getLogger(__name__)
#logger = logging.getLogger("")
