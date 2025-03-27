# Growth of Artificial Intelligence in biological sciences: Pubmed automation 🔬
## **Introduction**
 *smart words-primero en español, ai dont spik a inglich*
 El uso de nuevos métodos para 
 
**Text mining phases**[^1][^2]
1. Study purpose
   - Identificate and label biological search terms
2. Information recovery
   - Recolect, identify,pick and validate information
3. Text processing
   - Lexicon analysis
4. Data analysis and extraction
5. Data display
   - Storage information
   - Plotting
     - Subplot
     - Barplot
   - Wordcloud

# Study purpose 

# Information recovery

# Text processing 

# Data analysis

# Data display

## **Subplot**
<ins>Used libraries:</ins>

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
```

(![Subplot AI and Bio](![barAI00_25](![sub300_25](![subplots](https://github.com/user-attachments/assets/524f911a-fece-4605-83f0-61e4a6f66cb2)
)

## **Barplot**


(![Artificial Intelligence and Biology fields](![barAI00_25](https://github.com/user-attachments/assets/24e4b05b-a203-42a7-b56d-903c9a5cc8e1))


(![Machine Learning and Biology fields](![barAI00_25](![barML00_25](https://github.com/user-attachments/assets/d4e41fd9-e075-4da6-a7fd-3e99e612124b)
)

(![Deep Learning and Biology fields](![barAI00_25](![barDL00_25](https://github.com/user-attachments/assets/2d33a91d-2515-49c9-9700-4f9b5116c139)
)

## **Lineplot**
(![Growth of Artificial Intelligence research in biology fields (2000-2025)](![barAI00_25](![lineevoAI00_25](https://github.com/user-attachments/assets/bc416514-b021-4f88-b954-176a58f4e093)


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

![Most common keywords in Artificial Intelligence applied to biological sciences](![wccc](![wc00_25](![wc00_25](https://github.com/user-attachments/assets/8a201db6-0aab-4c22-a3ce-643766225156)

[^1]: Contreras, M. (2014). Minería de texto: una visión actual. *Biblioteca Universitaria*. 17(2), pp. 129-138.

[^2]: Contreras, M. (2014). Minería de texto: una visión actual. *Biblioteca Universitaria*. 17(2), pp. 129-138.
