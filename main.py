# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(i,j):
    # [assignment] Add your code here
    if(sorted(i)== sorted(j)):
        return True
    else:
        return False        
         
i ="listen"
j ="silent"
find_anagrams(i, j)

