#!/usr/bin/env python3
# Import numpy

import numpy as np

def calculate(list_numbers):

    """
        -> This function outputs summary statistics for the rows, columns, and elements in a 3 x 3 matrix
        -> list_numbers is the input to this function 
        -> This is a 1x9 array 
        -> These summary statistics we want this function to return are:
            - mean;
            - variance;
            - standard deviation;
            - max;
            - min
            - sum
    """

    # -> If the input array contains less than 9 values, raise a ValueError
        # -> We are reshaping the input array into a 3x3 matrix, which means if it doesn't have 9 elements then we can't perform 
            #the calculations on it
        # -> In which case, we want to return an error message
    
    if len(list_numbers) < 9:
        raise ValueError("List must contain nine numbers.")

    # -> Now we know we have an input array which is 1x9 - the previous if block filtered out the other possible inputs up to this 
            #point in the code
    # -> We want to convert the input array into a 3x3 matrix 
    # -> The input array is called list_numbers
    # -> So we do this by using reshape on list_numbers, and setting it equal to a new variable 
    # -> np_matrix is now the input 1x9 array which we have converted into a 3x3 matrix 

    np_matrix = np.array(list_numbers).reshape((3, 3))

    # -> Now we want to take the 3x3 matrix, calculate its summary statistics and put them into a dictionary 
    # -> We first want to set up an empty dictionary which isn't populated with values, because we want the function to return a dictionary 
            #of summary statistics 
    # -> And then we want to take the 3x3 matrix, calculate its summary statistics and populate the dictionary with them 
    # -> So we first define the empty dictionary
     
    # Defining an empty dictionary 
        # -> On the webpage which provides example outputs of what we want from this function, it tells us what syntax we want the dictionary 
            # to be in. The structure of the empty dictionary below was based on this 
	# -> The next stage after this is to populate it with the summary statistics of the 3x3 matrix 
    
    dict_statistics = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    # Then we populate the dictionary with the list of statistics from the 3x3 matrix
    # calculations <- This is the name of the dictionary which we are returning

    calculations = dict()

    # We then iterate through each of the elements in the dictionary whose structure we just defined 
        # -> For each one of those elements, perform the function which is stored at that value of the dictionary 
        # -> Perform it three times, first on each of the rows on the matrix, then on each of the columns, then on one of the elements 

    for name, function in dict_statistics.items():
        calculations[name] = [
            function(np_matrix, axis=0).tolist(),
            function(np_matrix, axis=1).tolist(),
            function(np_matrix).tolist()]
        
    # Return the dictionary which is populated with these summary statistics 
        
    return calculations