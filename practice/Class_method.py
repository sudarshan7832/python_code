class Employee:
    name = "sudarshan"
    #@classmethod
    def set_name(cls):
        return  cls.name.upper()
e1 = Employee()
print(e1.set_name())

#class variable if call with object then update it , only effect to that object
#if you update with class name like class_name.variable then effect to all objects

"""
without classmethod it works but not good practice

cls is actually the object (e1)

Python looks for name inside e1

Not found → it checks the class

Finds name = "sudarshan"
"""