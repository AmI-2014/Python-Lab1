'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>

Copyright (c) 2014 Dario Bonino
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''

def prime(number):
    '''
    Checks if the given number is a prime

    Returns True if the number is a prime, false otherwise
    '''
    # if no divisor could be found the number is a prime 
    found = False
    
    # check even numbers except 2
    if((number % 2 == 0) and (number > 2)):
        found = True
    else:
        # iterate over odd numbers only
        for i in range(3, number / 2, 2):
            # check the remainder of the division
            if(number % i == 0):
                # set the prime flag at true
                found = True
                # stop searching
                break
    # if not found is a prime
    return not found

if __name__ == '__main__':
    number_as_string = raw_input("Insert a number:\n>");
    
    # convert to an integer number
    number = int(number_as_string)
    
    if(number > 0):
        # check if prime
        if(prime(number)):
            print "The number %d is a prime." % (number)
        else:
            print "The number %d is not a prime" % (number)
    else:
        print "Zero or negative numbers cannot be used..."
