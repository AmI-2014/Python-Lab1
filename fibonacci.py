'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''

def fib(order):
    # initialization, we use a tuple
    a = (0, 1)
    
    # the resulting array
    fibonacci = []
    # init while variable
    i = 0
    
    # fill the array
    while i < order:
        a = (a[1], a[0] + a[1])
        fibonacci.append(a[0])
        i+=1
        
    return fibonacci
        

if __name__ == '__main__':
    # get the series order as a string
    order_as_string = raw_input("Insert the Fibonacci's series order:\n>")
    
    # convert the string to an integer number
    order = int(order_as_string)
    
    # get the Fibonacci's series value
    values = fib(order)
    
    # print the values
    print values
