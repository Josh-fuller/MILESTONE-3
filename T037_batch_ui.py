# ECOR 1042 Milestone 3 - Batch UI
# T037
#Contributors: JOSH FULLER 101201594
#              JACK OOMEN 101187427
#Submitted April 9th 2021

from Cimpl import *

from T037_image_filters *


#Color dictionary
colordict = {
    "black": create_color(0,0,0),
    "white" : create_color(255,255,255),
    "blood" : create_color(255,0,0),
    "green" : create_color(0,255,0),
    "blue" : create_color(0,0,255),
    "lemon" : create_color(255,255,0),
    "aqua" : create_color(0,255,255),
    "pink" : create_color(255,0,255),
    "gray" : create_color(128,128,128)
    }    

# Creates the presets for cyan, blood and lemon
string1 = "aqua" 
string2 = "blood"
string3 = "lemon"

#Requests for the user to input a file namefile = str(input("What is the text file name?"))

def apply_filters(image: Image,filter_list: list):
    """
    Applies the requisite filters, gotten from the test_file. Simply type in the name of the file upon the prompt (ensuring its in the same place as the program), and two files 
    will be created (for 2 lines). To test the UI, open the files.
    """
    #Changes the filters to lowercase, so that the file does not have to be case sensitive
    lowerFilters = []
    for x in filter_list:
        lowerFilters.append(x.lower())
        
    #lowerFilters = [ x.lower() for x in filter_list ]
    
    #If relevant filter is present based on characters, said filter is applied to the image.
    if '3' in lowerFilters:  
        image = three_tone(image,string1,string2,string3)
    if 'x' in lowerFilters:  
        image = extreme_contrast(image)
    if 't' in lowerFilters:  
        image = sepia(image)
    if 'p' in lowerFilters:  
        image = posterize(image)
    if 'e' in lowerFilters:  
        image = detect_edges(image,15)
    if 'v' in lowerFilters:  
        image = flip_vertical(image)
    if 'h' in lowerFilters:  
        image = flip_horizontal(image)
        
    return image #Returns the filtered image

def batch_ui(filename:str) -> list:
    """
    Opens the filename specified, splits each word into a respective string, then applies each filter into a new designated file (for each line present).
    
    >>>batch_ui(file) 
    
    """
    
    #Opens the file and reads it
    in_file = open(filename,"r")
    
    for line in in_file:
        #Creates a string from each word in each line
        split_line = line.split()
        #Uses the first word to find which photo is being modified
        imageFilename = split_line[0]
        #Loads the image specified above
        image = load_image(imageFilename)
        #Names the filtered image using the second word
        newFilename = split_line[1] 
        #Applies the filters specified after the second word
        final_image = apply_filters(image,split_line[2:])
        #Saves the image to your folder as the new name
        save_as(final_image,newFilename)
        
    return None 

#Main Script
file = input("File path:")
batch_input = batch_ui(file) 
