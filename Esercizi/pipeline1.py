"""
This pipeline is able to filter out stopwords, punctuation marks
and words which are not nouns through tokenization and tagging
"""

import nltk
import sys
import pydash
from nltk.corpus import stopwords, wordnet as wn
from string import punctuation

def main(bag_of_words):
  tokens = nltk.word_tokenize(bag_of_words)
  important_tokens = (
    pydash.chain(tokens)
      .filter(lambda t: t not in punctuation)
      .filter(lambda t: t not in stopwords.words('english'))
  )

  tagged_tokens = nltk.pos_tag(important_tokens.value())
  nouns = (
    pydash.chain(tagged_tokens)
      .filter(lambda t: 'NN' in t[1])
      .map(lambda n: n[0])
  )

  print(nouns.value())

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1])