# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:06:57 2023

@author: noafc
"""

def my_func(x1,x2,x3):
    
    denom = x1+x2+x3 
    
    # Checking if denominator is not equal to zero
    if denom == 0:
        return("Not a number -denominator equals Zero")
      
    ##Checking if all parameters are of float type
    
    if type(x1)==int or type(x2)== int or type(x3)==int:
        
         return("Error: parameters should be float")
         
     ## checking if the value is proper
         
    if type(x1)!= float or type(x2)!=float or type(x3)!=float:
        return None
        

     # Evaluating the equation and returning the result
    result =(x1+x2+x3)*(x2+x3)*x3 /denom 
    return float(result)
       
