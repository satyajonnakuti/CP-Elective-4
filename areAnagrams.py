# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    s2=s2.lower()
    s1=s1.lower()
    liststr=list(s1)
    liststr2=list(s2)
    
    if len(liststr) != len(liststr2):
        return False
    else:
    
        for i in range(0,len(liststr)-1):
            if liststr[i]>liststr[i+1]:
                liststr[i],liststr[i+1]=liststr[i+1],liststr[i] 

    
        for j in range(0,len(liststr)-1):
            if liststr2[j]>liststr2[j+1]:
                liststr2[j],liststr2[j+1]=liststr2[j+1],liststr2[j] 
  
    
        if liststr==liststr2:
            return True
        else:
            return False
    
   
 
    
print(areAnagrams("aba","BAA"))