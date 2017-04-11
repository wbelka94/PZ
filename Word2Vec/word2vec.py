import nltk

fs = open("C:\\Users\\s0152850\\Desktop\\glove.6B.100d.txt",'r', encoding='utf8')
model={}
for line in fs:
    tokens = line.split()
    vec = [0 for i in range(100)]
    for i in range(100):
        vec[i] = tokens[i+1]
    model[tokens[0]] = vec
