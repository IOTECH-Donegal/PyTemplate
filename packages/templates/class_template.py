"""
Class Template by JOR, by convention, use camel case to name classes
"""


# In any complex application, create a base class which will never be instantiated.
class JORzAbstractClass():
    # Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self):
        print("Running constructor for base class")
        # Create attributes and set initial values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")


# Then create child classes which can access the methods and properties of the base class
class JORzChildClass(JORzAbstractClass):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1):
        # Call back to the parent class
        JORzAbstractClass.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    # Dunder Methods
    # Return a string representing this object
    def __str__(self):
        return self.parameter1
    def __len__(self):
        print("Manually set this to something meangingful")
        return 0
    def __del__(self):
        print(f"Deleted the object {(self.parameter1)}")

    # Class Methods
    def jorz_do_stuff1(self, numberz):
        if self.debug:
            print("Executing the jorz_do_stuff1 method of template class")
            print(f"This method was passed {self.parameter1} as a tag for the object" )

    def jorz_do_stuff2(self):
        if self.debug == True:
            print("Executing the jorz_do_stuff2 method of template class")
            print(f"test_message was set to {self.parameter1}" )

    # Static methods
    @staticmethod
    def jorz_static_method():
        # Static method, you can't use self
        print("Executing the jorz_do_stuff1 method of template class")
        print(f"Parent class variable is {JORzAbstractClass.pi}")




