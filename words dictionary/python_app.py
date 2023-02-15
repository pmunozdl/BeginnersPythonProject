#pip install PyDictionary

from PyDictionary import PyDictionary

dictionary = PyDictionary()

word = input("Enter your word: ")
print(dictionary.meaning(word))