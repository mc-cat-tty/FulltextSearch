import java.io.IOException;
import java.nio.file.Paths;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.document.*;
import org.apache.lucene.index.*;
import org.apache.lucene.search.*;


class Indexer {
	public static void main(String[] args) throws IOException {
    var analyzer = new StandardAnalyzer();
    var path = Paths.get("text_repo");
    var dir = FSDirectory.open(path);
    var config = new IndexWriterConfig(analyzer);
    var index = new IndexWriter(dir, config);

    var doc1 = new Document();
    doc1.add(new TextField("title", "Lu sule", Field.Store.YES));
    doc1.add(new TextField(
      "body",
      "Il signor fratello sole, il quale è la luce del giorno, e tu tramite" + 
      "lui ci dai la luce. E lui è bello e raggiante con grande splendore...",
      Field.Store.YES
    ));

    var doc2 = new Document();
    doc2.add(new TextField("title", "Lu ientu", Field.Store.YES));
    doc2.add(new TextField(
      "body",
      "Lodato sii, mio Signore, per fratello vento, e per l'aria" +
      "e per il cielo; per quello nuvoloso e per quello sereno...",
      Field.Store.YES
    ));
		
    index.addDocument(doc1);
    index.addDocument(doc2);
    index.close();
    dir.close();
	}
}
