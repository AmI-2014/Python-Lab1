'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
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
