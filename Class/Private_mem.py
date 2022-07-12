import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Class')
class Base:
    def __init__(self) -> None:
        self.a="Public_geeksforgeeks"
        self.__v="Private"
        self._p="Protected"
    
    def get_Private_mem(self):
        logger.info("Base: Accesing the Private Variable %s",self.__v)


class Derived(Base):
    def __init__(self) -> None:
        
        Base.__init__(self)
        # try:
        #     logger.info("Derived Class: Calling Private members of base class: ")
        #     logger.info(self.__v)
        # except Exception as e:
        #     logger.exception("Derived Class:You can't access Private members from dervied class {}".format(str(e)))


        logger.info("Derived Class:Accesing the Protected members from Base class %s ",self._p)


if __name__=="__main__":
    o1=Base()
    o1.get_Private_mem()
    d1=Derived()
    print(o1.a)

