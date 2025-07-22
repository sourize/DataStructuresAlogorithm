str = "Sourish"
chars = []
for char in str:
    chars.insert(0, char)
reversed_str = ''.join(chars)
#print (reversed_str)
#print (char)
reversed_text = ""
for char in str:
    reversed_text = char + reversed_text
print(reversed_text)

# Reversing a Sentance
sentence = "hello world"
result = ' '.join(reversed(sentence.split()))
print(result)  # Output: world hello