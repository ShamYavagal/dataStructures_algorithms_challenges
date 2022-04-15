word = ''

rstring = "REVERSE"

i = 1
length = 0

for each in rstring:
  length+=1

while i < length:
  for each in rstring:
    word += rstring[-i]
    i+=1


print(word)
