# Growth of Artificial Inteligence in biology through text mining 🔬
## **Introduction**
 *smart words*
 
**Text mining phases**[^1]
1. Study purpose
   - Identificate and label biological search terms
2. Information recovery
   - Recolect, identify,pick and validate information
3. Text processing
   - Lexicon analysis
5. Data analysis and extraction
6. Data display?
   - Storage information

 
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

![Most common keywords in Artificial Intelligence applied to biological sciences](![wccc](https://github.com/user-attachments/assets/dde6f712-3586-4ad8-9b20-338cdedbb3b8)


[^1]: Contreras, M. (2014). Minería de texto: una visión actual. *Biblioteca Universitaria*. 17(2), pp. 129-138.
