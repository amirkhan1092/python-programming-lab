# words count 
f = open('birthdaywishes.txt', 'r')
data = f.read()
words = data.split()
print(words)
print(len(words))
f.close()
