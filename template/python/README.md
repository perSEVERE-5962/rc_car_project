# Python Templates
The templates in this folder are meant to be examples that can be used when creating the source for the project

Templates:
1. sensorTemplate.py - use this template when creating a new sensor library
2. commandTemplate.py - use this template to when creating a new command

## Using your classes (importing) in another python script
1. Make an empty file called `__init__.py` in the same directory as the sensor library file that you will be creating
   * _You could also copy the one from template/python folder_
2. That will signify to Python that it's "ok to import from this directory"
3. Then, in your main program file you can import your class

For example, if your sensor file is called hcsr04.py and the class is called Hcsr04 you would add the following to your main program file
`from hcsr04 import Hcsr04`
