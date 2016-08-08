spam = [ 'apples', 'bananas', 'tofu', 'cats']
spamString = ''

for i in range(len(spam)-1):
  spamString += spam[i] + ', '

spamString += 'and ' + spam[-1]

print(spamString)
