def common_charecter(word1,word2):
    
    for i in word1:
        if i in word2:
            
            print( i, end = " ")

word1 = input("Enter first string ")
word2 = input("Enter the second string ")
print()    
common_charecter(word1,word2)