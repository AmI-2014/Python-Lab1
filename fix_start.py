'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''

def fix_start(string):
    # replace all the characters equal to the first
    return string[0] + string[1:].replace(string[0], "*")

if __name__ == '__main__':
    # get the input string
    string = raw_input("Insert a string:\n>")
    
    # print the computed string
    print fix_start(string)
