# Introduzione
Il fine ultimo è creare dei word embedding.

# One hot
>Usiamo una rappresentazione con simboli discreti. I vettori one-hot sono collezioni di 1 e 0, in cui uno 0 rappresenta l'assenza della parola - di un vocabolario - nel documento, mentre un 1 rappresenta la sua presenza.

Problemi:
- rappresentazione **discreta** non coglie le sfumature
- $|v|$ dipende dalla dimensione del vocabolario (tipicamente la eguaglia) -> si può arrivare a dimensioni esagerate (500k+ elementi)

Nuovi obiettivi: vettori densi, che contengano anche il contesto della parola, ovvero il legame della parola con quelle che le stanno attorno.

# Word vector
>Vettori densi di valori reali che rappresenta una parola, in modo tale che la distanza di questa da altre parole simili (semanticamente) sia bassa, mentre sia alta per parole semanticamente dissimili.

## Word2vec
>Framework di Mikolov et al. - 2013

Idea: dato un grande corpus di documenti, ogni parola appartenente a un dizionario fisso sarà codificata come vettore. Il vettore è influenzato dal contesto della parola. La dimensione del vettore dipende dalla dimensione della "sliding window" e quindi dal contesto.

# Modelli w2v
## Skipgram
Implementazione: NN 3 layer.
1. rappresentazione one-hot del vocabolario
2. hidden layer di dimensione arbitraria
3. layer di uscita di dimensione del vocabolario

La rete è unsupervised, grazie alla backpropagation.
## CBOW
>Esegue un task di tipo _fill in the blank_, in cui la rete restituisce un vettore di probabilità che ogni parola sia quella adatta a riempire lo spazio bianco.

La backpropagation funziona grazie alla conoscenza del vettore di ground-truth -> permette di calcolare l'errore di predizione.

## Confronto
Skipgram:
- funziona bene con corpus piccoli
- cattura bene il contesto
- funziona bene per parole poco frequenti
- Lento rispetto a CBOW
#Completa 

CBOW: #Completa

# LLM
>Hanno come vantaggio la capacità di contestualizzare le parole all'interno di grandi contesti. Nella versione, più grande, BERT riesce a catturare 1024 token.

CBOW cresce esponenzialmente con la dimensione, BERT no.

I modelli GPT gestiscono bene i task di language generation -> modelli generativi.

# Doc2vec
>Famiglia di algoritmi con scopi identici al w2v, ma sui documenti.

# Consigli per il progetto
Benchmark di un sistema IR con doc2vec vs word2vec vs modello vettoriale

#Vedi cross validation

https://scikit-learn.org/stable/
