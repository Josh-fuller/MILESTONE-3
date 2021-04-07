from Cimpl import *

from T037_image_filters import *
#Contributors: JOSH FULLER 101201594
#              JACK OOMEN 101187427

# Creates the presets for gray, blood and lemon
gray = create_color(128,128,128)
blood = create_color(255,0,0)
lemon = create_color(255,255,0)

#Requests for the user to input a file namefile = str(input("What is the text file name?"))

def apply_filters(image: Image,filter_list: list):
    """
    If the character in the if statement is present in the file, the relevant filter is applied 
    """
    #Changes the filters to lowercase, so that the file does not have to be case sensitive
    lowerFilters = []
    for x in filter_list:
        lowerFilters.append(x.lower())
        
    #lowerFilters = [ x.lower() for x in filter_list ]
    
    #Relevant filter characters
    if '3' in lowerFilters:  
        image = three_tone(image,blood,lemon,gray)
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
file = input("Name of file:")
batch_input = batch_ui(file) 
