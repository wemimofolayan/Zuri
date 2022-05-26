# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        file = f.read()
        f.close
    return file

read_file_content("story.txt")

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here 
    text=text.lower()
    text=text.split(" ")
    
    word_frequency={}
    
    for i in text:
        if i in word_frequency:
            word_frequency[i]+=1    
        else:
            word_frequency[i]=1
    return(word_frequency)

count_words()