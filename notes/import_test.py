#- steps to try for PyCharm:
#    - Mark directory as source
#    - add module paths to __init__.py (pyCharm seems to have a problem with empty __init__ files)
#    -

# Import package
print("1")
import test_package # Note that the print_hello_direct is automatically ran upon import

# Import sub-package
print("2")
import test_package.package_within_package # Automatically prints 'bye' due to existence of print_bye_direct function.
test_package.package_within_package.print_bye_function_container


# Access the files (i.e., modules)
print("3")
test_direct = test_package.print_hello_direct # directly prints the output
test_class_container = test_package.print_hello_class_container # assi
test_function_container = test_package.print_hello_function_container

#print("3")
#import test_package.print_hello_function_container.print_hello_function
#print_hello_function()


# Assign the actual, callable function to variable (style 1)
test_function = test_package.print_hello_function_container.print_hello_function # Note that there is no '()' when addressing the function
test_function() # It is now possible to call the function. Note that parantheses are used only when calling the function, not while it is being assinged.

# Import a function with style 2
print("4")
from test_package.print_hello_function_container import print_hello_function
print_hello_function()




# Assign the class to a variable
test_class   = test_class_container.Print_hello_class
# Create an instance of the class
test_intance = test_class_container.Print_hello_class()
# Use a class method
print("5")
test_intance.print_hello_method_within_class()



#test_package.print_hello_funtion_container
# Create an intance of the class
#my_instance = test_package.print_hello_class_container.Print_hello_class()
#my_instance.name
