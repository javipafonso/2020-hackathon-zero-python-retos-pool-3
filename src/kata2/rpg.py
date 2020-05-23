#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    password = string.ascii_letters + string.punctuation + string.digits
    
    
    return ''.join(random.choice(password) for i in range(passLen)) 
    #
    #

    

password=RandomPasswordGenerator()
print(password)
