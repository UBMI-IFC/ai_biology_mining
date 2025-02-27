# Growth of Artificial Inteligence in biology through text mining 🔬
## **Introduction**
 *smart words*
 
**Text mining phases**[¹]
1. Study purpose
   _Identificate and label biological search terms
2.Information recovery
   _Recolect, identify,pick and validate information
3. Text processing
   _Lexicon analysis
5. Data analysis and extraction
6. Data display?
   _Storage information

 
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

We like circle forms, but it can be change to whatever we want. This time for educational purposes is just a circle, a deformed one

![wceje](https://github.com/user-attachments/assets/df19b753-d636-47cb-93b4-f6ebb7a2895b)


[¹]: Contreras, M. (2014). Minería de texto: una visión actual. *Biblioteca Universitaria*. 17(2), pp. 129-138.
