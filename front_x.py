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
