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

# Thesaurus
*Iponimo*: auto è un iponimo di mezzo di trasporto
*Iperonimo*: mezzo di trasporto è iperonimo di auto

#Ricorda con ipo (sotto) e iper (sopra) - ipovedente, ecc.

> **Polisemia** = relazione tra parole identiche ma con semantica diversa

Esempi di thesaurus:
- Roget (primo dizionario, 1852)
- Wordnet
- INSPEC
- MESH

#Attenzione il plurale di *thesaurus* è *thesauri*
#Vedi Pubmed e MeSH (Ontologia terminologica): https://www.ncbi.nlm.nih.gov/mesh/

Perché usare thesaurus? avere un vocabolario controllato, affidabile, con basso rumore

Non necessari per ricerche generiche, sono utili soprattutto per i campi ristretti/settoriali

## TIT - Thesaurus Index Term
#Attenzione non è detto che un concetto sia espresso da una sola parola

Nei thesaurus il dato strutturato da essi memorizzato è: concetto (unità semantica di base, costituito da una parola, più parole o frasi) - definizione (spiegazione)

TIT relationship -> relazioni di generalizzazione (iperonimia) -  specializzazione (iponimia) e, sullo stesso livello, appartenenza allo stesso oggetto/ambito/ecc.

Esempio di *mouse*, parola polisemica: http://wordnetweb.princeton.edu/perl/webwn?s=mouse&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=

**Grafo bipartito** che collega parole, concetti a *synset*

