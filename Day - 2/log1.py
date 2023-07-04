import logging

#logging using basic configurtion

logging.basicConfig(filename='demo.log' , level=logging.DEBUG ,format='%(levelname)s_%(asctime)s-%(message)s')

def checkname(name):
    if len(name)<2:
        logging.debug("checking name length")

        return "invalid name!"
    elif name.isalpha():
        logging.debug("checking name is alpha")
        return "name is valid"
    elif name.isspace():
        logging.debug("checking name isspace")
        return "invalid name!!"
    elif name.replace(' ','').isalpha():
        logging.debug("checking full name ")
        return "name is valid"
    else:
        logging.debug("all checking failed")
        logging.info("check full name pls")
        return "invalid name!!!"



print(checkname("Rajkumar123"))

