'''
Template by JOR
Organise all the code in functions then call it at the end
'''
# Global variables
debug = True

# Imports
from packages.templates import class_template

# Instantiate and create an objects
my_template = class_template.JORzChildClass("Instance1")
#my_broken = class_template.JORzAbstractClass()
#my_broken.run()

# Functions
def func1():
    my_template.message = "Cad é mar atá tú, ar domhan?"
    my_template.jorz_do_stuff1(12345)
    my_template.jorz_do_stuff2()
    my_template.jorz_static_method()

# Main programme
if __name__ == "__main__":
    print("Running template.py directly")
    # Run the important code
    try:
        # Break the logic up into functions
        if debug == True:
            print("Calling functions sequentially")
        func1()
    # If there is an error, run this code
    except TypeError as e:
        print(f"Type error: {e}")
    except OSError as e:
        print(f"OS error: {e}")
    except:
        print("Unclassified error")
    # If there in no error, run this code
    else:
        if debug == True:
            print("Function was called correctly, no errors caught")
    # This code runs at the end
    finally:
        if debug == True:
            print("Finishing programme now")
else:
    # Break the logic up into functions
    if debug == True:
        print("template.py has been imported, objects are created only")

