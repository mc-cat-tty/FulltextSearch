from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from common import TEXT_REPO_PATH

if __name__ == "__main__":
  try:
    index = open_dir(TEXT_REPO_PATH)
  except:
    print(f"Failed to open {TEXT_REPO_PATH}")

  searcher = index.searcher()
  parser = QueryParser("content", index.schema)
  query = parser.parse(u"fratello")
  results = searcher.search(query)
  print(f"fratello in docs num: {results.docset}")

  query = parser.parse(u"nuvoloso")
  results = searcher.search(query)
  print(f"fratello in docs num: {results.docset}")
