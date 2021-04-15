Milestone 3 Version 1.0

****Contact INFO*****
VOICE: 613-619-0942
EMAIL: joshfuller@cmail.carleton.ca

Date: 14 April 2021

Description
------------
A photo editing program that gives the user ability to apply a variety of unique images filters to a selected image of the user choosing. Two interfaces are provided. The text-based interactive UI and a batch UI. Through the interactive UI, the user is able to load an imagr and then perform a sequence of filters and draw curve functions on the imagr. The batch UI uses a .txt file that can load a list of images, apply a continuation filters and save the image.

- This project is made up using the following files:
    T037_image_filters.py
    T037_interactive_ui.py
    T037_user_interface.py
    T037_batch_ui.py

#Installation
-------------
Python 3.7.9 or newer version must be installed. 
Wing 101 7.2 or later version intalled. 
Extrenal modules that are used: Cimpl, point_manipulation, simple_Cimpl_filters, T037_image_filters, numpy and PIL.
Built in Python modules are used, they should be already imported in some of the extrenal modules. 

Usage
-------
> python T037_batch_ui.py

In order to use the batch user interface a .txt file is needed which is correctly formatted for the code to interpret.
This file acts as the users input. One line in the file represents one interation through the program. There are three pieces of information in each line of code, each being seperated by a space. The first part is the source image that the program will make a copy of and then modify. The second piece of information is the name that the resulting file. Finally a collection of specified letters represents what filters will be appllied to an image and in what order.

Sample .txt file: 'r.txt'
miss_sullivan.jpg test1.jpg e t v
miss_sullivan.jpg test2.jpg  v P

Example of T037_batch_ui
>>> file = input("File path:") #prompts the user to input the name of the desired .txt file for the program to take as input
>>> batch_input = batch_ui(file) #sends the selected file to 'batch_ui' function as a str variable
>>> #Program ends with a saved a copy of the orginal image with filters applied (via the 'apply_filters' function) which was named according the second part of the orginal .txt file
Note: The batch UI does not use the four colour channel filters (blue,red,green and combine) as well as the draw_curve function

> python T037_interactive_ui.py

When run, a menu of functions will be displayed for the user containing all the filter and file mangement commands. An option of filter or file management is selectedd by inputting the first character displayed in the menu. As an errir control, if a command that does not exist is called, the program will prompt for the user to enter another command. The menu that is displayed once the program has been run is below:

L)oad image  S)ave-as
3)-tone  X)treme contrast  T)int sepia  P)osterize
E)dge detect  D)raw curve  V)ertical flip  H)orizontal Flip 
Q)uit 

: 

The user is first able to load an image by inputting an 'l' or an "L" into the shell. Prior to this action, the selected image form the user will be displayed. In order to interact with the rest of the function sin the menu, the image must be closed. Once closed, the filter commands can be entered successfully in a cumulative manner until the user calls for the S)ave-as function. 

: L
L)oad image  S)ave-as
3)-tone  X)treme contrast  T)int sepia  P)osterize
E)dge detect  D)raw curve  V)ertical flip  H)orizontal Flip 
Q)uit 

: 3

The command above will call for the 3-tone filter. This will be applied to the image and displayed in a seperate window.

Note: The interactive UI does not use the four colour channel filters (red,blue,green,combine)

Credits: 
---------
Blue channel filter - Lauren Ogilvie 
Red channel filter - Jack Oomen
Green channel filter - Patrick Ferenc
Combine filter - Josh Fuller 
Three-tone filter - Josh Fuller
Extreme contrast filter -Jack Oomen
Sepia filter - Lauren Ogilvie
Posterize image filter - Patrick Ferenc
**********_adjust_component function - 
Edge Detection - Josh Fuller
Draw curve - Jack Oomen
Flip vertical filter - Lauren Ogilvie
Flip horizontal filter - Patrick Ferenc 
_image_border_finding function - Josh Fuller
_exhaustive_search function - Lauren Ogilvie
_interpolation function - Patrick Ferenc
Interactive UI - Patrick Ferenc and Lauren Ogilvie 
Batch UI - Josh Fuller and Jack Oomen

License: 
________

Copyright (c) 2021 MILESTONE 3. Josh Fuller, Patrick Ferenc, Jack Oomen, and Lauren Ogilvie. 
All rights reserved. 


THIS SOFTWARE IS PROVIDED "AS IS", WITH NO WARRENTY OF ANY KIND EXPRESSED OR IMPLIED.
IN NO EVENT SHALL THE COPYRIGHTERS BE HELD FOR LIABILITY OR CLAIM. ALL USE IS AT OWN RISK.
