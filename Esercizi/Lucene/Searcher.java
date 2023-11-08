import java.nio.file.Paths;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.search.*;


public class Searcher {
  static final String queryText = "fratello";
  public static void main(String[] args) throws Exception {
    var path = Paths.get("text_repo");
    var directory = FSDirectory.open(path);
    var dirReader = DirectoryReader.open(directory);
    
    var analyzer = new StandardAnalyzer();
    var searcher = new IndexSearcher(dirReader);
    var parser = new QueryParser("body", analyzer);
    var query = parser.parse(queryText);
    ScoreDoc[] hits = searcher.search(query, 10).scoreDocs;
    for (var d : hits) {
      System.out.println(d.doc);
    }
    
    dirReader.close();
    directory.close();
  }
}
