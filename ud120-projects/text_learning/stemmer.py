from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')

print(stemmer.stem('responsiveness'))
print(stemmer.stem('response'))
print(stemmer.stem('responsibility'))
print(stemmer.stem('unresponsive'))