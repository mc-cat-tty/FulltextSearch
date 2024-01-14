Obiettivo: sviluppo di un search engine con funzionalità avanzate di sentiment analysis e/o word2vec. In aggiunta, sarà necessario valutare le performance del sistema.

Dataset: sull'ordine delle migliaia (>3000). Scraping, dataset già pronti o altro.
#Vedi Kaggle, internet movie db

Indicizzazione:
- Whoosh
- Lucene
- PostgreSQL

Concretamente: crea un set di search engine evoluti rispetto al seed sopra fornito, mediante piccole variazioni del nucleo centrale. Prova a combinare i vari search engine che offrono pacchetti differenti.

Confronta le performance tra quello base e gli evoluti.

# Search engine
Il search engine dovrà implementare un modello di indicizzazione.

## Sentiment analysys
Il linguaggio di interrogazione dovrà permettere di esprimere query che includono i sentimenti richiesti.

# Confronto performance
## Benchmark
Gruppo di 10 UIN (User Information Need) espresse in linguaggio naturale, da tradurre nel linguaggio di interrogazione del search engine.

Necessario usare misure di performance adeguate -> almeno 3 metriche.

In tutto avremo 10\*3 = 30 misure.

Ogni query avrà una peculiarità che metta in evidenza le caratteristiche del search engine.

# Materiali
README con metriche di benchmark, risultati e installazione. Codice sorgente. Da consegnare una settimana prima.

Presentazione (max 20 slide, da presentare in 20 min) da mostrare il giorno stesso dell'esame.

## Presentazione
- descrizione della sorgente dati: caratteristiche e numero dei text item
- descrizione di pacchetti e architettura del search engine di base
- caratteristiche di ogni search engine evolute in termini di
	- modello di ranking (di solito comune ai diversi pacchetti di sentiment analysys) e integrazione
	- linguaggio di interrogazione e schema dell'indice
- benchmark

Consigli: essere chiari sul *come* il problema è stato risolto, descrivendo *quale* soluzione è stata individuata. Non fare vedere codice, se non per piccoli frammenti.


# Valutazione
- minimo: caratteristiche del dataset e funzione del search engine di base
- qualità dei search engine evoluti separati
- quantità di search engine evoluti
- modalità di confronto dei search engine
	- il benchmark è adatto a mostrare le performance?
	- le misure sono adeguate a mettere a confronto le performance?
	- efficacia della presentazione dei benchmark
