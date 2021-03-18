import re

def vowel_search(word):
    
    vowels = r"[aeiouAEIOU]"

    if re.search(vowels,word):
        for i in word:
            if i in vowels:
                print(i, end = " ")
                
vowel_search("James") 