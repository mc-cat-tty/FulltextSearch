from whoosh.index import *
from whoosh.fields import *
from os import *
from common import TEXT_REPO_PATH

if __name__ == "__main__":
  schema = Schema(title=TEXT(stored=True), content=TEXT)
  try:
    index = create_in(TEXT_REPO_PATH, schema)
  except:
    print(f"Failed to open {TEXT_REPO_PATH}")
    exit(1)
    
  writer = index.writer()
  writer.add_document(title=u"Lu sule", content=u"""
  Il signor fratello sole, il quale è la luce del giorno, e tu tramite 
  lui ci dai la luce. E lui è bello e raggiante con grande splendore...
  """)
  writer.add_document(title=u"Lu ientu", content=u"""
  Lodato sii, mio Signore, per fratello vento, e per l'aria
  e per il cielo; per quello nuvoloso e per quello sereno...
  """)
  
  try:
    writer.commit()
  except:
    print(f"Failed to write inside {TEXT_REPO_PATH} folder")
    exit(2)