# Crecimiento de la Inteligencia Artificial en biología
**Example**

```js
def details_rec(pmid):
    handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
    docs = Entrez.read(handle)["PubmedArticle"]```
