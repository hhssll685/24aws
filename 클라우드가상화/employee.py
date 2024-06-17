class Employee(object):
    def __init__(self, name, age, gender,birthday):
        self.__name=name
        self.__age=age
        self.__gender=gender
        self.__birthday=birthday
    
    @property
    def name(self):
        return self.__name
        
    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self,value):
        self.__birthday = value