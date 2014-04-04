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

def fix_start(string):
    # replace all the characters equal to the first
    return string[0] + string[1:].replace(string[0], "*")

if __name__ == '__main__':
    # get the input string
    string = raw_input("Insert a string:\n>")
    
    # print the computed string
    print fix_start(string)
