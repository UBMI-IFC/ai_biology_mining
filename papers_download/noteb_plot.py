import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Numeric years
all_results_df['Year']=pd.to_numeric(all_results_df['Year'], errors='coerce')
all_results_df = all_results_df[(all_results_df['Year'] >= 2000) & (all_results_df['Year'] <= 2025)]

#Check year distribution
year_distribution=all_results_df.groupby(["Year"]).size()
print("Distribution:")
print(year_distribution)

#Combine col/Terms to string 
all_results_df['Term_List']=all_results_df['Term_List'].astype(str)
all_results_df['Count']=all_results_df.groupby(["Year", "Bio_Term","Term_List"])["PMID"].transform("count")
all_results_df=all_results_df.drop_duplicates(subset=["Year", "Term_List", "Bio_Term"])

#Iterate search terms lists/Create barplot
for ai_term in aipai:
      ai_data = all_results_df[all_results_df['Term_List'].str.contains(ai_term, case=False)]
      bio_counts = ai_data.groupby('Bio_Term')['Count'].sum().reset_index()

      plt.figure(figsize=(18, 8))
      sns.set_theme(style="darkgrid")
      ax=sns.barplot(x='Bio_Term', y='Count', hue='Term_List', data=all_results_df.drop_duplicates(subset=['Bio_Term', 'Term_List']), palette='mako')

      plt.title('Publications of Artificial Intelligence in the biological sciences (2000-2025)', fontsize=16)
      plt.xlabel('Biological Field', fontsize=12)
      plt.ylabel('Count', fontsize=12)
      plt.xticks(rotation=45)


      #Checar esta parte
      for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),  ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=13)

      plt.tight_layout()
      plt.show()


#Create subplot
sns.set_theme(style="darkgrid")

g=sns.FacetGrid(all_results_df, col="Term_List", row="Bio_Term", margin_titles=True, height=3.5, aspect=1.8, sharey=False)
g.map_dataframe(sns.lineplot, x="Year", y="Count", marker='o', markersize=7, linewidth=2)
g.set_axis_labels("Year", "Publication count")
g.set_titles(col_template="{col_name}".strip("[]'"), row_template="{row_name}")
g.fig.suptitle("Biological fields and Artificial Intelligence publications (2000-2025)", fontsize=16, y=1.02)


g.set(xticks=np.arange(2000, 2026, 3))

g.savefig("subplots.png")
plt.tight_layout()
plt.show()

#Create lineplot/Count summary
summary_df = all_results_df.groupby(['Year', 'Term_List'])['Count'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Count', hue='Term_List', data=summary_df, markers= True, dashes=False, linewidth=2.5)

plt.title("Total of publicated files for Artificial Intelligence in the biological sciences (2000-2025)", fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(sorted(all_results_df['Year'].unique()))
plt.legend(title='IA field', fontsize=10)

plt.tight_layout()
plt.show()
