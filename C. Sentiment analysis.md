# Introduzione
Classificazione binaria: sentimento positivo o negativo
**Problema di classificazione**

Polarità -> più granularmente: 12 emozioni fondamentali
Intensità -> non sempre vale l'assunzione che le intensità siano numeri interi, assegnamo a un vettore valori reali
**Problema di regressione**

Ogni frase può essere rappresentata come un vettore
Polarità: direzione (angolo del vettore), Intensità: magnitudine (modulo)

Usiamo la distanza del coseno.

Come passare da rappresentazione testuale a vettoriale? Pipeline standard di NLP:
1. tokenization
2. stop words removal
3. stemming
4. lemmatization
5. bag of words
6. POS - Part Of Speech - tagging
7. NER - Named Entity Recognition
8. WSD - Word-sense disambiguation

# Approcci per la sentiment analysis
## Tree-based approaches
SST - Stanford Sentiment Treebank. 5 labels: molto positivo, positivo, neutro, negativo, molto negativo.

#Nota il concetto di negazione, a livello di sentiment analysis, è delicato

## Neural Network-based tokenizer/detokenizer
_sentencepiece_ di Google usa un approccio BPE - Byte-pair-encoding - e *unigrams*

Problema: il linguaggio cambia in base alla lingua, ma non voglio tempi di inferenza diversi in base alla lingua utilizzata.
Intuizione: usare una codifica simile alla Huffman Encoding. Comprimo tenendo conto delle parole più frequenti.

#Vedi NIPS conference

## Transformers: contestual words representation
Introdotti con il paper *Attention is all you need* di Vaswani

Oggi vedremo:
- positional encoding
- multi-head attention

## Positional encoding
Per non perdere il significato complessivo della frase memorizzo all'inizio e trasporto lungo la rete la posizione di ogni token.

## Multi-head attention
Estratti token e posizione dalla frase li confronto tra di loro ed estraggo informazioni sulla loro importanza, anche in relazione agli altri token.
*Sono importante per la frase se vado in coppia con un certo altro token*

## Stato dell'arte
- Generative Pre-trained Transformer di OpenAI 1, 2, 3
- Bidirectional Encoder Representation for Transformeres di Google
- Robustly Optimized BERT pretraining Approach di Facebook AI
- T5: Text to Text Transfer Transformer (lingua intermedia language independent)

#Vedi *A comprehensive overview of large language models* di arXiv
#Vedi LLaMA 2 e Alpaca
#Vedi Hugging Face

## Pacchetti
- huggingface.co/models?other=sentiment-analysis
- huggingface.co/j-hartmann/emotion-english-distilroberta-base
- FEEL-IT di Bianchi et al.

#Vedi dataset DynaSent

## Pandas
#Vedi hdf5
Libreria per l'elaborazione scientifica di dadi tabellari

Divisione del dataset: train, validation, test
#Attenzione a come viene splittato il dataset, esistono diverse strategie (vedi stratificazione)

# Metriche
- **f1score** è la media geometrica tra precision e recall
- l'**accuratezza** è una metrica imprecisa in quanto non tiene conto di falsi positivi e negativi
- **loss** quanto perdo in base al massimo che potrei fare

#Ricorda sempre di salvare insieme al modello anche i parametri con cui è stato allenato, dato che sono robusti rispetto al cambiamento di versione del framework.