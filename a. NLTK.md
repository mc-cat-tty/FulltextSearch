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