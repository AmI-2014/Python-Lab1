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
