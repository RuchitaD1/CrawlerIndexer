import whoosh.index as index
from whoosh.qparser import QueryParser
import testUI
def search(q):
    print "searching"

    ix = index.open_dir("indexdir3")
    s = ix.searcher()


    qp = QueryParser("content", schema=ix.schema)
    q = qp.parse(unicode(q))
    a=[]
    with ix.searcher() as s:
        results = s.search(q)
        print

q=testUI.ui()
search(q)

