#Create a program that takes a string  input from the user 
#and reverses it.
#Store the original string and reversed string in a list and display
#count the number vowel in the original string

word=input('Enter a word:')
print('The entered word is:', word)
# the reversed word
print('the reversed word is:', word[: : -1])
# Count the number of vowel
vowels = 'aeiou'
vowels_count = 0
for vowel in vowels:
  vowels_count += word.count(vowel)

print(f"The number of vowels is {vowels_count}")
