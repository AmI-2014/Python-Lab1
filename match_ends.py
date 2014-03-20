'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''

def match_ends(string_array):
    count = 0
    for string in string_array:
        if((len(string) >= 2) and (string[0] == string[-1])):
            count += 1
    return count

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
    print "Output:%s" % (match_ends(input_string))
