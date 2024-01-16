# PostgreSQL
Cosa abbiamo già visto? Ricerca testuale con `LIKE`, `ILIKE`, `~`, `~*`:
- `WHERE str LIKE matching_str`
- `WHERE str ILIKE matching_str`
- `WHERE str ~ regex` Cerca di matchare la RE su **parte** della stringa e ritorna lo stato
- `WHERE str ~* regex` Cerca di fare un match case-insensitive della RE
- I due operatori precedenti possono essere negati: `!~`, `!~*`

#Ricorda di usare le ancore se vuoi un match totale quando usi le regex

Cosa vedremo? full text search, text tokenization, full text indexing (inverted index su una colonna e simili) and more

#vedi https://www.postgresql.org/docs/current/textsearch.html

**Textual item**: *documento* nel senso stretto del termine, ma non necessariamente un'intera pagina di testo, può anche derivare dalla concatenazione di campi di una tabella relazionale.

## Full text indexing
>Full text indexing permette ai documenti di essere preprocessati e di creare un indice per velocizzare la ricerca successivamente.

Il DBMS (in questo caso PostgreSQL) permetterà di fare preprocessing con un paradigma dichiarativo (resta pur sempre SQL).
## Full text search
> Un **documento** o **textual field** è l'unità di ricerca di un full text search system.

Un documento è normalmente un textual field all'interno della riga di una tabella o la concatenazione di campi, memorizzati non necessariamente nella stessa tabella (costruito dinamicamente).

```sql
SELECT title || ' ' || author || ' ' || body AS document
FROM messages
WHERE mid = 12;
```

#Nota `||` operatore di concatenazione (esegue la giustapposizione); spazio necessario per separare le parole.

Questa query ritorna, per ogni entry della tabella *messages* con *mid* pari a 12, il valore della colonna tabella concatenato (con spazio) ad autore e corpo.
### Text Search Types
Vengono forniti da PostgreSQL due tipi di dati progettati per supportare full-text search (TS - Text Search):
- `tsvector` è una lista ordinata di lessemi distinti. Viene usata la lemmatizzazione (lemma = parola normalizzata rispetto a un dizionario di riferimento) delle parole.
- `tsquery` memorizza i lessemi che devono essere cercati e permette di concatenarli con operatori logici di and (`&`), or (`|`) and not (`!`). La sintassi delle tsquery prevede: si possono usare operatori di AND, OR, NOT come prima e l'operatore di FOLLOWED BY (`<->`) usato per il phrasal retrieval; oppure l'operatore di PROXIMITY SEARCH (`<N>`) con N numero esatto di distanza (numero di parole tra gli operandi + 1, che equivale al numero di spazi).

Esistono funzioni per fare pre-processing, prima di interpretare la frase come i due tipi sopra spiegati:
- `to_tsvector('english', textual_field)` torna un output di tipo tsvector facendo a monte un'operazione di tokenizzazione, rimozione delle stopwords, lemmatizzazione, portandosi dietro la posizione delle parole.
- `to_tsquery('english', textual_field)` torna un output di tipo tsquery facendo le operazioni di preprocessing precedenti.
Il primo campo ha un valore di default pari a *english*

```sql
SELECT 'There are two cats in the room'::tsvector;  -- 'There' 'are' 'cats' 'in' 'room' 'the' 'two'
SELECT to_tsvector('english', 'There are two cats in the room');  -- 'cat':4 'room':7 'two':3
SELECT 'Cats & Rooms'::tsquery;  -- 'Cats' & 'Rooms'
SELECT to_tsquery('english', 'Cats | Rooms');  -- 'cat' | 'room'
```

#Nota L'operatore `::` è l'operatore di cast in SQL.
### Text match operator
È un operatore binario infisso che ritorna un tipo booleano. È case-insensitive e accetta tsvector a sinistra e tsquery a destra.

```sql
SELECT 'There are two cats in the room'::tsvector @@ 'cat & room'::tsquery;  -- false
SELECT to_tsvector('english', 'There are two cats in the room') @@ to_tsquery('english', 'CAT & Room');  -- true
SELECT to_tsvector('english', 'There is a critical error') @@ to_tsquery('english', 'critical <-> error');  -- true
SELECT to_tsvector('english', 'There is a error which is not critical') @@ to_tsquery('english', 'error <4> critical');  -- true
```

### Su tabelle
```sql
SELECT title
FROM documenti
WHERE to_tsvector(COL1 || ' ' || COL2) @ ts_query(QUERY);
```
#Nota l'inline concatenation
## Indici
Ci sono due tipi di indici che possono essere usati in PostgreSQL:
- GiST - Generalized Search Tree; generalizzazione del B+ tree. Lossy: può produrre falsi match.
- GIN - Generalized Inverted Index. Da preferirsi per text-search.

```sql
CREATE INDEX users_idx ON TABLE users USING GIN(email);
```

#Nota che la colonna deve essere di tipo `tsvector`. Trasforma la colonna se `varchar`, addirittura aggiungendo una colonna del tipo corretto come sotto, da mantenere accuratamente aggiornata:
```sql
ALTER TABLE documenti ADD COLUMN title_ts tsvector;
UPDATE documenti SET title_ts = to_tsvector(title);
CREATE INDEX title_idx ON documenti USING gin(title_ts);
```

Posso creare una colonna di giustapposizioni: `UPDATE documenti SET title_ts = to_tsvector(title || ' ' || body);`

# Apache Lucene
>Apache Lucene è una libreria per accedere a un motore di full-text search scritta in Java. Ha il vantaggio di essere cross-platform.

Cosa gestisce:
- indexing
- searching
- retrieving

Lucene fa anche ranking. Il ranking si basa su un modello di IR. La bontà di un modello è una metrica che permette di definire quanto il comportamento del modello è simile a quello atteso.

Agnostica rispetto all'input con cui si acquisisce la query; i documenti da indicizzare si trovano in un certo filesystem. Lucene non offre l'accesso a quest'ultimo.

## Indexing overview
>L'index ottiene i dati dal filesystem, che contiene la repository dei documenti; consiste di uno o più documenti.

>L'oggetto `Document` rappresenta gli oggetti che sono memorizzati nell'index e che sono ritornati a motivo di una ricerca.

Idea del processo di creazione dell'indice:
- "pesco" il contenuto
- lo trasformo in `Document`
- lo inserisco nell'`Index`

Idea del processo di querying:
- invio la query
- ricerca sull'indice
- ottengo un `Document`

## Document
```java
var doc = new Document();  // costrutto senza campi
// Due diversi campi di testo
doc.add(new TextField("title", "Lucene in action", Field.Store.YES));
doc.add(new StringField("isbn", "3874983274", Field.Store.YES));
```

#Nota `Field.Store.YES` significa *memorizza il contenuto del XXXField nell'inverted index, non solo posizione e documento* -> utile per veloci preview, come avviene su Google

Differenza tra `StringField` e `TextField`:
- `StringField` non esegue preprocessing
- `TextFiled` lo esegue

`Field.Store`: `YES`, `NO`, `COMPRESS` (poi da decomprimere)

## Index
Procedura di indexing:
- istanziare un oggetto `Analyzer`: prende un documento e lo trasforma in token pronti da essere indicizzati. `var analyzer = new StandardAnalyzer();`
	- `StandardAnalyzer` filtra con le stopwords inglesi
	- `BrazillianAnalyzer`
	- `ChineseAnalyzer`
	- ...
- configurare l'indice. Dove salvarlo? memoria principale o secondaria
	- `var d = FSDirectory.open(Paths.get("repo"));` - RAM (`RAMDirectory`) o disk based (`FSDirectory`). `Directory` è astratto
	- `IndexWriterConfig` - contiene la configurazione di `IndexWriter`: `var c = new IndexWriterConfig(analyzer);`
	- `var w = new IndexWriter(Directory d, IndexWriterConfig config)`
	- Aggiungere il documento all'index `w.addDocument(doc)`
- open directory
- access Index

Ricorda il paradigma: store first and query later. Si apre l'indice prima in scrittura per la creazione e, in differita, in lettura.

La cartella con i documenti che codificano l'indice sono file binari non direttamente intelleggibili.

## Query syntax
Una query è una serie di clausole. Ogni clausola può avere un prefisso:
- *+* clausola richiesta
- *-* clausola vietata
- *:* per specificare il campo nella forma `campo: valore` 

Esempio:
```java
Query q = parser.parse("parse")
```

## Query avanzate
- **Boosting**: dare la priorità ad una clausola piuttosto che ad un'altra
- **Proximity search**: estensione del phrasal retrieval
- **Ranges**: eg. date o numeri

## IndexSearcher & IndexReader
```java
IndexReader reader = DirectoryReader.open(dir);
IndexSearcher searcher = ...
```
#Completa 


Il risultato di `IndexSearcher.search(Query, int)` contiene diversi campi:
#Completa 

Esiste un wrapper di Lucene scritto in Python: _PyLucene_
# Whoosh
Successore di Lucene, scritto in Python.

Lo schema elenca i campi che devono essere indicizzati. Ogni campo può essere indicizzato e/o memorizzato. Nell'esempio sottostante il contenuto è indicizzato ma non memorizzato nell'indice; mentre titolo e percorso sono sia indicizzati che memorizzati.
Schema dell'indice:
```Python
from whoosh.fields import *
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
```

I campi possono essere dei seguenti tipi definiti in `whoosh.fields`:
- TEXT
- ID
- KEYWORDS

L'indicizzazione si ottiene con i seguenti passaggi:
- creazione dell'indexer che scriverà sul fs l'indice generato
- creazione di un writer
- aggiunta dei documenti
- commit in memoria

La ricerca passa attraverso le seguenti fasi:
- creazione dell'indexer: ha bisogno di conoscere dove si trova l'indice
- creazione del searcher
- creazione del parser. Dipende dalla schema, memorizzato nell'indice
- parse della query
- ricerca della query mediante il searcher
# Wrapping up
Sia Lucene che Woosh utilizzano il modello BM25 - Best Matching -, un evoluzione del modello probabilistico particolarmente adatto per corpus settoriali.

Ma non implementano nessun algoritmo di ranking, che sarà il prossimo argomento.