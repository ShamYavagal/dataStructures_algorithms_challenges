word = ''

rstring = "REVERSE"

i = 1
l = 0

for each in rstring:
  l+=1

while i < l:
  for each in rstring:
    word += rstring[-i]
    i+=1


print(word)
