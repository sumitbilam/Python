line = input ("Enter the sentence: ")
count = 0

for vowel in line:
    if vowel.lower() == 'a' or vowel.lower() == 'e' or vowel.lower() == 'i' or vowel.lower() == 'o' or vowel.lower() == 'u':
        count += 1

print("Vowel Found: " +str(count))

words = line.split()
length = len(words)
print("Total words found: " + str(len(words)))

palindrome = 0
digit = 0

for i in range(0, length):
    if words[i] == words[i][::-1]:
        palindrome += 1
    if words[i].isdigit() == True:
        digit += 1

print("Palindrome words found: ", str(palindrome))
print("Numeric words found: ", str(digit))