# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:10:46 2023

@author: noafc
"""
def revword(word:str) -> str:
    
    return word.lower()[::-1]


def countword()->int: 
    # open file and extract the first word
    file = open('text.txt')
    count = 0
    word = file.readline().strip()
   #Loop through the file, and count the occurrences of the
   # reversed words that match the extract word 
    for line in file:
        words = line.strip().split()
        for w in words:
            if revword(w) == word:
                count += 1
   # Add 1 to count to include the occurrence in the first line
    return count + 1
        
        
        
        