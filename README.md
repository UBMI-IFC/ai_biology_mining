# Growth of Artificial Intelligence in Biological Sciences (2000-2025): Semiautomated PubMed searches 🔬

## **Introduction**
The development of new tools, such as artificial intelligence (AI), has gained significant popularity in recent decades, eventually being applied across various aspects, including the biological sciences. However, not all areas within this field show the same level of integration of these tools. 
For this reason, this project was developed to create a tool that enables semiautomated literature searches using the PubMed API to explore the connection between AI and five areas of biological sciences. This allows us to visualize part of their evolution and growth through the extraction, processing and analysis of large volumes of information.

## **What can be accomplished with this script?**
Using the PubMed API through Entrez E-Utilities, it is possible to:

- Perform semiautomated extraction of metadata from scientific articles in PubMed using search terms related to AI applied to biological sciences.
- Analyze keywords and their frequency of appearance in texts through MeSH terms and text ([Title/Abstract]).
- Visualize key terms in wordclouds.
- Identify publication trends by biological discipline over the period from 2000-2025.
- Generate graphs showing the temporal distribution of total AI mentions within biological sciences.
- Process large volumes of information, reducing the need of extensive manual review.
    
## **Methodology**

- *Search term definition*
   - Combine AI terms ```Machine Learning, Deep Learning and Artificial Intelligence``` with biological fields ```biology, biomedicine, genetics, ecology and bioinformatics```.
- *Search and metadata extraction*
   - Using the PubMed API, records from 2000-2025 were processed with searches limited to [Title/Abstract] and showing a maximum of 500 articles per term combination.
- *Data cleaning*
   - Duplicates were removed based on PMIDs, and information was integrated.
- *Keyword analysis*
   - Frequency count of terms found in MeSH and text.
- *Visualization*
   - Generation of trend graphs and wordclouds based on the obtained data. 

## **Installation** 

*Libraries*

**The script was developed in a Google Colab environment and the following Python libraries were installed:**

```pip install Biopython pandas matplotlib seaborn wordcloud numpy``` 

You can also access the notebook in [Google Colab bio mining](https://colab.research.google.com/drive/1Jf52G462JOr1qgynk2Ae74ImTkltIbHo?usp=sharing)

*Configure your email*

To access the PubMed API, it's recommended to register an email address as contact information to receive usage alerts if necessary.

```
Entrez.email = "youremail@example.com"
```

## Results

**Most frequent keywords**
![common_keywords](https://github.com/user-attachments/assets/7579523f-c79f-43df-9175-a1814ec2b037)


**Wordcloud**
![wordcloud_freq](https://github.com/user-attachments/assets/049f336a-6a3e-40aa-8f60-79e7eb4d83f4)

**Biological discipline graph**
![barplot_count](https://github.com/user-attachments/assets/9cd08c01-c983-421f-9711-6c6c4844aafe)

**Total AI mentions**
![total_pub](https://github.com/user-attachments/assets/ecdf4228-a2dd-4617-83bf-7df776ea19be)


*Este proyecto fue desarrollado como parte del programa de servicio social en la Unidad de Bioinformática y Manejo de la Información del Instituto de Fisiología Celular, UNAM.*
