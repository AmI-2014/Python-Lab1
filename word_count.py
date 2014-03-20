'''
Created on Mar 19, 2014

@author: Dario Bonino <dario.bonino@polito.it>
'''

import string

def word_count(txt):
    # prepare the words dictionary
    count = {}
    
    # remove characters different from letters and spaces
    txt = txt.lower()
    to_remove = string.punctuation + string.digits + string.whitespace
    
    # remove undesired chars (check if can be done better, e.g., regexp)
    for i in range(0, len(to_remove)):
        txt = txt.replace(to_remove[i], " ")
    
    # split over spaces
    words = txt.split(" ")
    
    # iterate over distinct words
    for word in words:
        
        # strip leading and trailing chars
        key = word.strip()
        
        # filter out empty strings
        if key != '':
            # update the word count
            if (count.get(key, None) != None):
                count[key] = count[key] + 1
            else:
                count[key] = 1
    
    return count


if __name__ == '__main__':
    # main program
    
    # read the filename from the console
    filename = raw_input("Type the filename (absolute or relative path):\n>")
    
    # open the file
    txt_file = open(filename)
    
    # read the file
    text = txt_file.read()
    
    # close the file
    txt_file.close()
    
    # count the words
    count = word_count(text)
    
    # sort the words by ascending letters
    keys = count.keys()
    keys = sorted(keys)
    
    # initialize statistics
    all_words = 0
    (max_word, max_count) = ("", 0)
    
    # show the word counts
    for key in keys:
        print "%s : %d" % (key, count[key])
        all_words += count[key]
        if(max_count < count[key]):
            (max_word, max_count) = (key, count[key])
        
    # show statistics
    print "--------------------------------------------"
    print "Words number: %d" % (all_words)
    print "Unique words: %d" % (len(count))
    print "Most frequent word is: \"%s\"(%d occurrences)" % (max_word, max_count)
