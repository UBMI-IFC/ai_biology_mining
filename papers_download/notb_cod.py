#Create WordCloud

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

#Append keywords lists from dF 
keywords_text = []
text="".join(all_results_df["Manual_Keywords"].str.lower())
keywords_text.append(text)
text="".join(all_results_df["MeSH_Keywords"].str.lower())
keywords_text.append(text)

stopwords=([""]) + list(STOPWORDS)

wordcloud = WordCloud(max_words=100, stopwords=stopwords, width=1600, height=800, background_color="black", max_font_size=90, collocations= True).generate(text)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud.recolor(colormap="tab20b", random_state=17), interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
