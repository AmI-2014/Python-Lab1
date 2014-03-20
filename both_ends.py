'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''

def both_ends(string):
    # if the string has more than 2 chars, return only the first and the last 2
    if(len(string) > 2):
        return string[:2] + string[-2:]
    # else return the empty string
    else:
        return ""

if __name__ == '__main__':
    # get the input string
    string = raw_input("Insert a string:\n>")
    
    # print the computed string
    print both_ends(string)
