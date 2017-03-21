from os import listdir
from sklearn import svm
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords, reuters
import re

cahcedStopWords = stopwords.words("english")
min_length = 3

class corpus:
    def __init__(self, dir_pos, dir_neg):
        self.dir_pos = dir_pos
        self.dir_neg = dir_neg
        self.documents = []
        for i, file in enumerate(listdir(dir_neg)):
            if i < 300:  # pierwsze 300 dokumentow jako testowe
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0;
                train = 0;
                doc = document(text, positive, train)
                self.add_document(doc)
            else:
                fs = open(dir_neg + "\\" + file, 'r')
                text = fs.read()
                positive = 0;
                train = 1;
                doc = document(text, positive, train)
                self.add_document(doc)

        for i, file in enumerate(listdir(dir_pos)):
            if i < 300:  # pierwsze 300 dokumentow jako testowe
                fs = open(dir_pos + "\\" + file, 'r')
                text = fs.read()
                positive = 1;
                train = 0;
                doc = document(text, positive, train)
                self.add_document(doc)
            else:
                fs = open(dir_pos + "\\" + file, 'r')
                text = fs.read()
                positive = 1;
                train = 1;
                doc = document(text, positive, train)
                self.add_document(doc)

    def add_document(self,document):
        self.documents.append(document)

    def get_train_documents(self):
        train = []
        for doc in self.documents:
            if doc.train == 1:
                train.append(doc.text)
        return train

    def initialize_vocabulary(self):
        self.vocabulary = {}
        self.inverse_vocabulary = {}
        for i,doc in enumerate(self.documents):
            if i%1000 == 0:
                print(i)
            for word in doc.get_unique_words():
                if word not in self.vocabulary:
                    self.vocabulary[i] = word
                    self.inverse_vocabulary[word] = i

    def get_svm_vectors(self,  Train = 0, Test = 0):
        Xs = []
        Ys = []
        for doc in self.documents:
            if Train == 1 and doc.train == 0:
                continue
            if Test == 1 and doc.train == 1:
                continue
            x = doc.get_vector(self.inverse_vocabulary)
            y = doc.positive
            Xs.append(x)
            Ys.append(y)
        return (Xs, Ys)

class document:
    def __init__(self, text, positive = 1, train = 1):
        self.positive = positive
        self.train = train
        self.text = text

    def preprocesig(self,raw_tokens):
        #stemowanie i usowanie stopwords
        no_stopwords = [token for token in raw_tokens if token not in cahcedStopWords]
        stemmed_tokens = []
        stemmer = PorterStemmer()
        for token in no_stopwords:
            stemmed_tokens.append(stemmer.stem(token))

        #p pattern i sprawszanie dlugosci slowa
        p = re.compile('[a-zA-Z]+');
        pattern_checked = []
        for stem in stemmed_tokens:
            if p.match(stem) and len(stem) >= min_length:
                pattern_checked.append(stem)

        return pattern_checked

    def get_unique_words(self):
        word_list = []

        for word in self.preprocesig(self.text.split()):
            if not word in word_list:
                word_list.append(word)
        return word_list

    def get_vector(self, inverse_vocabulary):
        lng = len(inverse_vocabulary)
        vector = [0 for i in range(lng)]        # wypelnienie 0
        for word in self.text.split():
            vector[inverse_vocabulary[word]] = 1
        return vector

dir_neg = "C:\\Users\\s0152850\\Desktop\\txt_sentoken\\neg"
dir_pos = "C:\\Users\\s0152850\\Desktop\\txt_sentoken\\pos"

crp = corpus(dir_pos,dir_neg)


#print(crp.documents[0].text)    # wypisanie pojedynczego dokumentu

crp.initialize_vocabulary()

# print(crp.vocabulary)
klasyfikator = svm.SVC(kernel = 'linear')

(X, y) = crp.get_svm_vectors(Train = 1)
klasyfikator.fit(X, y)


(XT, yt) = crp.get_svm_vectors(Train=1)
pozytywne = 0
wszystkie = 0

for i,x in enumerate(XT):
    wszystkie += 1
    klasa = klasyfikator.predict(x)
    if klasa == yt[i]:
        pozytywne = pozytywne + 1

print(pozytywne)
print(wszystkie)



#zmiana


