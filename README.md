#Team Leader Contact
Date: 16 April 2021

#PROJECT NAME/VERSION

#Description

#Installation
-------------
Python 3.7.9 or newer version must be installed. 
Wing 101 7.2 or later version intalled. 
Extrenal modules that are used: Cimpl, point_manipulation, simple_Cimpl_filters, T037_image_filters, 


#Usage
In order to use the batch user interface a .txt file is needed which is correctly formatted for the code to interpret.
This file acts as the users input. One line in the file represents one interation through the program. There are three pieces of information 
in each line of code, each being seperated by a space. The first part is the source image that the program will make a copy of and then modify. 
The second piece of information is the name that the resulting file. Finally a collection of specified letters represents what filters 
will be appllied to an image and in what order.

Sample .txt file: 'r.txt'
miss_sullivan.jpg test1.jpg e t v
miss_sullivan.jpg test2.jpg  v P

Example of T037_batch_ui
>>> file = input("File path:") #prompts the user to input the name of the desired .txt file for the program to take as input
>>> batch_input = batch_ui(file) #sends the selected file to 'batch_ui' function as a str variable
>>> #Program ends with a saved a copy of the orginal image with filters applied (via the 'apply_filters' function) which was named according the second part of the orginal .txt     file
