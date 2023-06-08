"""
This file contains started up code for when we run
```
import nuclear
```
That is, any code here will be executed at the moment you import the module.

If your module is short, you may want to include all its functionalities here.

Otherwise, you can further organize your code into folders and files.
"""

def func_in_init():
    """This function is availiable when you import the module"""
    print("Hello from __init__.py!")

# Import all functions in the files from this folder
from .main import *
from .another import *
