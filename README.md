# Crecimiento de la Inteligencia Artificial en las Ciencias Biológicas (2000-2025): Búsquedas semi-automatizadas en PubMed 🔬

## **Introducción**
El desarrollo de nuevas herramientas, como lo es la inteligencia artificial (IA), han ido adquiriendo gran popularidad en las útlimas décadas, terminando por ser aplicados en distintos ámbitos de la vida cotidiana, incluyendo las ciencias biológicas. Sin embargo, no todas las áreas dentro de este campo presentan el mismo nivel de integración de estas herramientas.
Por ello, se realizó este proyecto donde se desarrolló una herramienta que permite realizar búsquedas bibliográficas semiautomatizadas para explorar la vinculación entre la IA y cinco áreas de las ciencias biológicas. Permitiendo visualizar parte de su evolución y crecimiento mediante la extracción, procesamiento y análisis bibliográfico de grandes volúmenes de información, utilizando la API de PubMed. 

## **¿Qué se puede realizar con este código?**
Con la API de PubMed a través de Entrez E-Utilities, es posible:

- Realizar la extracción semiautomatizada de los metadatos de artículos científicos en PubMed mediante los términos de búsqueda relacionados con la IA aplicada a las ciencias biológicas.
- Analizar de palabras clave y su frecuencia de aparición en los textos, por medio de los términos MeSH y en el texto ([Title/Abstract]).
- Visualizar los términos clave en nubes de palabras.
- Identificar tendencias de las publicaciones por disciplina biológica en el periodo de 2000 a 2025.
- Generar gráficas donde se muestra la distribución temporal de las menciones totales de la IA dentro las ciencias biológicas.
- Procesar un gran volumen de información, disminuyendo la necesidad de una revisión manual extensiva.
    
## **Metodología**

- *Definición de términos de búsqueda*
   - Combinación de términos de IA (Machine Learning, Deep Learning y Artificial Intelligence) y campos de la biología (biology, biomedicine, genetics, ecology, bioinformatics).
- *Búsqueda y extracción de metadatos*
   - Por medio del uso de la API de Pubmed, se procesaron los registros del período 2000-2025, donde además las búsquedas limitaron en [Title/Abstract] y muestran un máximo de 500 artículos por combinación de términos.
- *Limpieza de datos*
   - Eliminación de duplicados basado en PMIDs únicos y se homogeneizó la información.
- *Análisis de palabras clave*
   - Conteo de frecuencias de los términos encontrados en MeSH y en el texto.
- *Visualización*
   - Generación de gráficos de tendencias y nubes de palabras con los datos obtenidos.

## **Instalación** 

*Bibliotecas*

**El codigo se realizó en un entorno de Google Colab y se instalaron las siguientes bibliotecas de Python**

```pip install Biopython pandas matplotlib seaborn wordcloud numpy``` 

*Configura tu email*

Para ingresar a la API se sugiere registrar un correo electrónico como contacto y así recibir alertas de uso en caso de ser necesario.

```
Entrez.email = "youremail@example.com"
```

## Resultados

**Palabras clave más frecuentes**
![common_keywords](https://github.com/user-attachments/assets/7579523f-c79f-43df-9175-a1814ec2b037)


**Nube de palabras**
![wordcloud_freq](https://github.com/user-attachments/assets/049f336a-6a3e-40aa-8f60-79e7eb4d83f4)

**Gráfica por disciplina biológica**
![barplot_count](https://github.com/user-attachments/assets/9cd08c01-c983-421f-9711-6c6c4844aafe)

**Total de menciones de IA**
![total_pub](https://github.com/user-attachments/assets/ecdf4228-a2dd-4617-83bf-7df776ea19be)


*Este proyecto fue desarrollado como parte del programa de servicio social en la Unidad de Bioinformática y Manejo de la Información del Instituto de Fisiología Celular, UNAM.*
