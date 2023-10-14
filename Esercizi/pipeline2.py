"""
This pipeline is able to filter out stopwords, punctuation marks
and words which are not nouns through tokenization and tagging.

In addition, it is capable of choosing the most appropriate
synset for each token, from a list of polysemous words and synonyms, 
by implementing a naive word sense disambiguation algorithm

Test:
python3 pipeline2.py "mouse eats the cheese while chased by a cat"
python3 pipeline2.py "I bought a new mouse for my new laptop"
"""

import nltk
import sys
import pydash
from nltk.corpus import stopwords, wordnet as wn, wordnet_ic
from string import punctuation

def naive_wsd(list_of_synsets, term_dis):
  """
  list_of_synsets list of lists containig synsets of each word
  term_dis term to be disambiguated
  """
  brown_ic = wordnet_ic.ic("ic-brown.dat")
  # Lower res_similarity -> low probability of associated concepts

  sense_confidence = float('-inf')
  disambiguated_sense = None

  for sense_dis in term_dis:
    confidence = 0
    for term_other in list_of_synsets:
      if term_dis != term_other:
        confidence += max([sense_dis.res_similarity(sense_other, brown_ic) for sense_other in term_other])
    if confidence > sense_confidence:
      disambiguated_sense = sense_dis
      sense_confidence = confidence
  
  return disambiguated_sense, confidence

def main(bag_of_words):
  tokens = nltk.word_tokenize(bag_of_words)
  important_tokens = (
    pydash.chain(tokens)
      .filter(lambda t: t not in punctuation)
      .filter(lambda t: t not in stopwords.words('english'))
  )

  print(important_tokens.value())
  nouns_synsets = (
    important_tokens
      .map(lambda n: wn.morphy(n, wn.NOUN))
      .filter(lambda n: n is not None)
      .map(lambda n: wn.synsets(n, wn.NOUN))
      .value()
  )
  print(nouns_synsets)

  disambiguated_terms = {}
  for term_dis in nouns_synsets:
    disambiguated_sense, sense_confidence = naive_wsd(nouns_synsets, term_dis)
    disambiguated_terms[disambiguated_sense] = sense_confidence
  
  print(*pydash.chain(disambiguated_terms)
      .map(lambda c, t: f"{t} [{t.definition()[:50]}]: {c}")
      .value(),
    sep = "\n"
  )
  # You can check online knowing the synset number

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1])