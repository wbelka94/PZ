#Lab 3
#Klasyfikacja polarity dataset v2.0

from os import listdir
from sklearn import svm

class corpus:
    def __init__(self, dir_pos, dir_neg):
        self.dir_pos = dir_pos
        self.dor_neg = dir_neg
        self.document = []
        for i, file in enumerate(listdir(dir_neg)):
            if i < 300:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0  # bo przegladamy negatywne
                train = 0  # przed 300 wiec testowy
                doc = document(text, positive, train)
                self.add_document(doc)
            else:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0  # bo przegladamy negatywne
                train = 1  # po 300 wiec treningowy
                doc = document(text, positive, train)
                self.add_document(doc)

        for i, file in enumerate(listdir(dir_pos)):
            if i < 300:
                fs = open(dir_pos + "\\" + file, 'r')
                text = fs.read()
                positive = 1  # bo przegladamy pozytywne
                train = 0  # przed 300 wiec testowy
                doc = document(text, positive, train)
                self.add_document(doc)
            else:
                fs = open(dir_pos + "\\" + file, 'r')
                text = fs.read()
                positive = 1  # bo przegladamy pozytywne
                train = 1  # po 300 wiec treningowy
                doc = document(text, positive, train)
                self.add_document(doc)

    def add_document(self, document):
        self.document.append(document)

    def get_train_document(self):
        train = []
        for doc in self.document:
            if doc.train == 1:
                train.append(doc.text)
        return train

    def initialize_vocabulary(self):
        self.vocabulary = {} #inicjalizacja pustego slownika przez {}; slownik w prost
        self.inverse_vocabulary = {} #przez podanie id zwraca slowo; slownik odwrotny
        for i,doc in enumerate(self.document):
            if i%1000 == 0:
                print(i)
            for word in doc.get_unique_words():
                if word not in self.vocabulary:
                    self.vocabulary[i] = word
                    self.inverse_vocabulary[word] = i

    def get_svm_vectors(self, Train=0, Test=0):
        Xs = []
        ys = []
        for doc in self.document:
            if Train == 1 and doc.train == 0:
                    continue # pominiecie dokumentu
            if Test == 1 and doc.train == 1:
                    continue
            x = doc.get_vector(self.inverse_vocabulary)
            y = doc.positive
            Xs.append(x)
            ys.append(y)
        return (Xs, ys)

class document:
    def __init__(self, text, positive=1, train=1):
        self.positive = positive
        self.train = train
        self.text = text

    def get_unique_words(self): #zwraca liste unikalnych slow dokumentu
        word_list=[]
        for word in self.text.split():
            if not word in word_list:
                word_list.append(word)
        return word_list

    def get_vector(self, inverse_vocabulary):
        lng = len(inverse_vocabulary)
        vector = [0 for i in range(lng)] #dla kazdej operacji na petli wpisujemy 0 do vector
        for word in self.text.split():
            vector[inverse_vocabulary[word]] = 1
        return vector


klasyfikator = svm.SVC(kernel = "linear")
crp = corpus("C:\\Users\\s0152851\\Desktop\\txt_sentoken\\pos", "C:\\Users\\s0152851\\Desktop\\txt_sentoken\\neg")
crp.initialize_vocabulary()

#print(crp.vocabulary)
#print(crp.inverse_vocabulary["pirate"])
(X,y) = crp.get_svm_vectors(Train = 1)
print("starting fitting procedure")
klasyfikator.fit(X,y)

(XT, yt) = crp.get_svm_vectors(Test = 1)
pozytywne = 0
wszystkie = 0
for i,x in enumerate(XT):
    wszystkie += 1
    klasa = klasyfikator.predict(x)
    if klasa == yt[i]:
        pozytywne = pozytywne+1

print(pozytywne)
print(wszystkie)