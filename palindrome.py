#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: # Open the file in read mode
with open('words.txt', 'r') as file:
    
    words = file.readlines()

palindrome_count = 0

for word in words:
  
    word = word.strip().lower()
    
    if word == word[::-1]:  
        palindrome_count += 1


print(f"Number of palindromes: {palindrome_count}")

