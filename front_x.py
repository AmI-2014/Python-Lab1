'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''

def front_x(strings, char):
    # build the two list of strings to be ordered
    beginning_with = []
    others = []
    
    # fill the lists
    for string in strings:
        if(string[0] == char):
            beginning_with.append(string)
        else:
            others.append(string)
    
    # sort both lists
    beginning_with.sort()
    others.sort()
    
    # concatenate the lists
    return beginning_with + others
    

if __name__ == '__main__':
    input_string = []
    ended = False
    
    # keep asking strings until the user types exit
    while not ended:
        # get the input string
        string = raw_input("Insert a string (exit to end):\n>")
        
        # check if exit
        if(string != "exit"):
            input_string.append(string)
        else:
            ended = True
    # print the computed string
    print "Input:%s" % (input_string)
    print "Output:%s" % (front_x(input_string, "x"))
