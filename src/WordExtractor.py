#!/usr/bin/env python

class VocabularyStore:
    def __init__(self):
        self.word_list = []
        self.__word_map = {}
    def add(self, word):
        if word not in self.__word_map:
            self.__word_map[word] = word
        self.word_list.append(word)

    def printAsString(self ):
        for word in self.word_list:
            print word
    

def valid(word):
    return True

    
if __name__ == '__main__':
    FILENAME = '../test/article/eco_putin.txt'
    with open(FILENAME) as file:
        content = file.read()

    voc_store = VocabularyStore()
    reciteList = []
    for word in content.split():
        if valid(word):
            voc_store.add(word)
    voc_store.printAsString()
