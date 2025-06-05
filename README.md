# Growth of Artificial Intelligence in the Biological Sciences (2000–2025): Semi-automated searches in PubMed 🔬

## **Introduction**
 
**Text mining phases**[^1][^2]
1. Study purpose
   - Identificate and label biological search terms
2. Information retrival (agregar el repositorio de donde obtuviste la base y los stack overflow)
   - Recolect, identify, pick and validate information
3. Text processing
   - Exploring large amounts of data or text
     - -Filters and cleaning duplicates
4. Data analysis and extraction
5. Outcome results
   - Storage information
   - Data display
     - Subplot
     - Barplot
     - Wordcloud

# Study purpose 
...
Use of Biopython `Bio.Entrez` to join NCBI database and get PubMed data 

¡Remember to write your email!
```
Entrez.email = "youremail@example.com"
```

Define the term list
`Agregar el script de lo de las carpetas`

# Information retrival

# Text processing 

# Data analysis and extraction

# Outcome results

## **Subplot**
<ins>Used libraries:</ins>

## **Barplot**


## **Wordcloud**

<ins>Used libraries:</ins>

```
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

"Charge" data, `index_col=0`

```
data = pd.read_csv("theterrible/database/isgoingtobe/here", index_col=0)
print(data.head())
```
Wordcloud

[^1]: Contreras, M. (2014). Minería de texto: una visión actual. *Biblioteca Universitaria*. 17(2), pp. 129-138.

[^2]: Sarkar, D. (2016). Text Analytics with Python: A practical real-world approach to gaining actionable insights from your data. https://doi.org/10.1007/978-1-4842-2388-8
