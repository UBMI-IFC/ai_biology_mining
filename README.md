# Growth of Artificial Intelligence in biological sciences: Pubmed automation 🔬
## **Introduction**
 *smart words*
 El uso de nuevos métodos para 
 
**Text mining phases**[^1][^2]
1. Study purpose
   - Identificate and label biological search terms
2. Information retrival
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
Entrez.email = "youremail@2hoursofsleepcaffeineandinsanity.com"
```

Define the term list
`Agregar el script de lo de las carpetas`

Create a dictionary, iterating your term lists
```
{'Biology': ['Artificial Intelligence', 'Machine learning', 'Deep learning'], 'Neurobiology': ['Artificial Intelligence', 'Machine learning', 'Deep learning'], 'Bioinformatics': ['Artificial Intelligence', 'Machine learning', 'Deep learning'], 'Genetics': ['Artificial Intelligence', 'Machine learning', 'Deep learning'], 'Ecology': ['Artificial Intelligence', 'Machine learning', 'Deep learning']}
```


# Information retrival

# Text processing 

# Data analysis and extraction

# Outcome results

## **Subplot**
<ins>Used libraries:</ins>

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
```

![Subplot AI and Bio](https://github.com/user-attachments/assets/524f911a-fece-4605-83f0-61e4a6f66cb2)

## **Barplot**


![Artificial Intelligence and Biology fields](https://github.com/user-attachments/assets/24e4b05b-a203-42a7-b56d-903c9a5cc8e1)

![Machine Learning and Biology fields](https://github.com/user-attachments/assets/d4e41fd9-e075-4da6-a7fd-3e99e612124b)


![Deep Learning and Biology fields](https://github.com/user-attachments/assets/2d33a91d-2515-49c9-9700-4f9b5116c139)


## **Lineplot**
![Growth of Artificial Intelligence research in biology fields (2000-2025)](https://github.com/user-attachments/assets/bc416514-b021-4f88-b954-176a58f4e093)


## **Wordcloud**

<ins>Used libraries:</ins>

```
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

"Charge" data, `index_col=0`, determines which csv column will be used... it's cleaner than do without it, trust the process

```
data = pd.read_csv("theterrible/database/isgoingtobe/here", index_col=0)
print(data.head())
```
Wordcloud

![Most common keywords in Artificial Intelligence applied to biological sciences](https://github.com/user-attachments/assets/8a201db6-0aab-4c22-a3ce-643766225156)

[^1]: Contreras, M. (2014). Minería de texto: una visión actual. *Biblioteca Universitaria*. 17(2), pp. 129-138.

[^2]: Sarkar, D. (2016). Text Analytics with Python: A practical real-world approach to gaining actionable insights from your data. https://doi.org/10.1007/978-1-4842-2388-8
