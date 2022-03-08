from file_parser import *
from ssh_connect import *
from banner import *

from loguru import logger

'''
data=[]
data =fileToList("ass.txt")

logger.debug( data

appendLineToFile("xxx","pass.txt")

data = fileToList("pass.txt")

logger.debug( data
'''

con = SSHConnect("root", 'xxxxxx', "xxxxxxxxx", 22, 4)

logger.debug("username: ", con.userName)
logger.debug("passwd: ", con.passWord)
logger.debug("port: ", con.portNumber)
logger.debug("status: ", con.status)

con.connect()
# con.exec_command('who')

logger.debug(con.status)

# showBanner()
