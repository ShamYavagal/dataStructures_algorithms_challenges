word = ''

rstring = "REVERSE"

i = 1
l = len(rstring)

while i < l:
  for each in rstring:
    word += rstring[-i]
    i+=1


print(word)