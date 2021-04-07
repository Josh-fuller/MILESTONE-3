from Cimpl import *

from T037_image_filters import *
#Contributors: JOSH FULLER 101201594
#              JACK OOMEN 101187427
# Creates the presets for gray, blood and lemon
gray = create_color(128,128,128)
blood = create_color(255,0,0)
lemon = create_color(255,255,0)

#Requests for the user to input a file namefile = str(input("What is the text file name?"))

def apply_filters(image,filters):
    """
    If the character in the if statement is present in the file, the relevant filter is applied 
    """
    
    #Relevant filter characters
    if '3' in filters:  
        image = three_tone(image,blood,lemon,gray)
    if 'X' in filters:  
        image = extreme_contrast(image)
    if 'T' in filters:  
        image = sepia(image)
    if 'P' in filters:  
        image = posterize(image)
    if 'E' in filters:  
        image = detect_edges(image,15)
    if 'V' in filters:  
        image = flip_vertical(image)
    if 'H' in filters:  
        image = flip_horizontal(image)
    if 'x' in filters:  
        image = extreme_contrast(image)
    if 't' in filters:  
        image = sepia(image)
    if 'p' in filters:  
        image = posterize(image)
    if 'e' in filters:  
        image = detect_edges(image,15)
    if 'v' in filters:  
        image = flip_vertical(image)
    if 'h' in filters:  
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
        #Splits each word into its own string.
        linesplit = line.split()
        #Takes the name of the picture that you want to apply filters to.
        imageFilename = linesplit[0]
        #Loads the image that you want to apply filters to. 
        image = load_image(imageFilename)
        #Saves the name you want the filtered image to be named
        saveFilename = linesplit[1] 
        #Makes the only strings in the list the filters that need to be applied.
        del linesplit[0:2]
        #Applies the filters wanted
        final_image = apply_filters(image,linesplit)
        #Saves the image to your folder as the name of saveFilename.
        save_as(final_image,saveFilename)
        
    return None 

#Main Script
Batch_input = batch_ui(file) 
