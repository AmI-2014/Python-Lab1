'''
Created on Mar 18, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''
def sort_last(array):
    return sorted(array, key=lambda x:  x[-1])

if __name__ == '__main__':
    input_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
    print input_list
    print sort_last(input_list)
