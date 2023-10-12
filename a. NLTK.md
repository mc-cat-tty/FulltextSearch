```python
import nltk
from nltk.corpus import stopwords

tokens = nltk.word_tokenize("this is a tests") # lista di parole
important_tokens = filter(lambda w: not w in stopwords.words('english'), tokens)

wnl = nltk.WordNetLemmatizer()
lemmatized_tokens = map(lambda w: wnl.lemmatize(w), important_tokens)

print(list(lemmatized_tokens))
```

Word Net è un dizionario ontologico -> thesaurus (vocabolario)

# Stemmers
Porter e Lancaster sono tra gli stemmer più famosi
```python
from nltk.stem.porter import PorterStemmer
from nltk.stem.porter import LancasterStemmer
p = PorterStemmer()
l = LancasterStemmer() # Più approssimativo
prt) for t in tokens])
print([l.stem(t) for t in tokens])
```

# POS Tagging e Parsing
```python
nltk.pos_tag(tokens)

# Per ottenere la tabella dei codici parlanti
nltk.help.upenn_tagset()
```

#Vedi https://www.nltk.org/book/ch08.html

```python
# Mostra un esempio
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
```

# Word disambiguation
```python
from nltk.corpus import wordnet as wn
wn.synsets('dog')
wn.synsets('dog', wn.VERB) # per restringere la ricerca a una certa part of speech
dog = wn.synset('dog.n.01')
dog.definition()
dog.hypernyms()  # iperonimi (sginificato di livello superiore
ld = dog.lemmas()  # lista di lemmi con quel significato (navigo al contrario il grafo)
ld[0].antonyms()
wn.morphy('denied', wn.VERB)  # Lemmatizer che sfrutta WordNet per morphing delle parole 
```

L'ordine in WordNon è casuale, infatti la logica di ordinamento è dal significato più diffuso a quello meno diffusa.

Morphy è usato in WordNet per portare inflessioni di una parola alla forma base, l'unica versione della parola memorizzata nei thesaurus.

## Word similarity
```python
dog = wn.synsets('dog')[0]
cat = wn.synsets('cat')[0]

dog.wup_similarity(cat)  # dog e cat sono synsets - distanza di WuPalmer
dog.path_similarity(cat)  # path similarity

from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
wn.res_similarity(brown_ic, dog)
cat.res_similarity(dog, brown_ic)
```

#Attenzione considera sempre le curve di ogni metrica