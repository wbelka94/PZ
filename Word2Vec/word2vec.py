from scipy.spatial.distance import cosine
import math

fs = open("C:\\Users\\s0152850\\Desktop\\glove.6B.100d.txt",'r', encoding='utf8')

def TOEFLParser(filename):
    tF = open(filename, 'r')
    state = 0
    question_words = []
    possibilities_bag = []
    answers = []
    for line in tF:
        if len(line.split()) == 0:
            question_words.append(question_word)
            possibilities_bag.append(possibilities)
            state = 0
        elif len(line.split()) == 2:
            if state == 1:
                possibilities.append(line.split()[1])
            if state == 0:
                question_word = line.split()[1]
                possibilities = []
                state = 1
        else:
            if line.split()[3] == 'a':
                answers.append(0)
            if line.split()[3] == 'b':
                answers.append(1)
            if line.split()[3] == 'c':
                answers.append(2)
            if line.split()[3] == 'd':
                answers.append(3)
    return (question_words,possibilities_bag,answers)

def cosine(v1, v2):
    v1v2 = 0
    for i in range(100):
        v1v2 += v1[i] * v2[i]
    v1norm = 0
    for i in range(100):
        v1norm += v1[i] * v1[i]
    v1norm = math.sqrt(v1norm)
    v2norm = 0
    for i in range(100):
        v2norm += v2[i] * v2[i]
    v2norm = math.sqrt(v2norm)
    return v1v2/(v1norm * v2norm)

model={}
for i,line in enumerate(fs):
    if i%1000 == 0:
        print(i);
    tokens = line.split()
    vec = [0 for i in range(100)]
    for i in range(100):
        vec[i] = float(tokens[i+1])
    model[tokens[0]] = vec
#
# king_vec =  model["king"]
# queen_vec =  model["queen"]
# man_vec =  model["man"]
# woman_vec =  model["woman"]
#
# print(cosine(king_vec,queen_vec))
# print(cosine(king_vec,man_vec))
# print(cosine(king_vec,woman_vec))

(question_words,possibilities_bag,answers) = TOEFLParser("C:\\Users\\s0152850\\Desktop\\toefl.txt")
print(question_words)
print(possibilities_bag)
print(answers)

true_positives = 0
for i in range(len(question_words)):
    maxSimilarity = -1
    try:
        sim1 = cosine(model[question_words[i]],model[possibilities_bag[i][0]])
        sim2 = cosine(model[question_words[i]],model[possibilities_bag[i][1]])
        sim3 = cosine(model[question_words[i]],model[possibilities_bag[i][2]])
        sim4 = cosine(model[question_words[i]],model[possibilities_bag[i][3]])
    except:
        sim1 = 0.5
        sim2 = 0.5
        sim3 = 0.5
        sim4 = 0.5

    if sim1> maxSimilarity:
        maxSimilarity = sim1
        answer = 0
    if sim2> maxSimilarity:
        maxSimilarity = sim2
        answer = 1
    if sim3> maxSimilarity:
        maxSimilarity = sim3
        answer = 2
    if sim4> maxSimilarity:
        maxSimilarity = sim4
        answer = 3
    if answer == answers[i]:
        true_positives += 1

print(true_positives/80.0)
