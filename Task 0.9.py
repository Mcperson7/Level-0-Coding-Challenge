import re

def vowel_search(word):
    
    vowels = r"[AaEeIiOoUu]"

    if re.search(vowels, word):
        for i in word:
            if i in vowels:
                print(i, end = " ")
                
word = input("Enter any word ")
vowel_search(word)