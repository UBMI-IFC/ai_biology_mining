# Crecimiento de la Inteligencia Artificial en las Ciencias Biológicas (2000-2025): Búsquedas semi-automatizadas en PubMed 🔬

## **Introducción**
El acceso a la información así como el desarrollo de nuevas herramientas han ido en aumento en las últimas décadas por lo que se ha transformado la manera en la que generamos y gestionamos el conocimiento científico presentando un desafío importante para los investigadores.
En este proyecto se realiza un análisis semiautomatizado para estudiar la evolución y crecimiento de la aplicación de la Inteligencia Artificial en diferentes campos de las ciencias biológicas, mediante el hace uso de la API de PubMed para extraer, procesar y visualizar datos de las publicaciones científicas. 

## **¿Qué se puede realizar con este código?**
Con la API de PubMed a través de Entrez E-Utilities, es posible:

- Realizar la extracción semiautomatizada de los metadatos de artículos científicos en PubMed mediante los términos de búsqueda relacionados con la inteligencia artificial aplicada a las ciencias biológicas.
- Analizar de palabras clave y su frecuencia de aparición en los textos, usando términos MeSH y en texto libre ([Title/Abstract]).
- Visualizar los términos clave en nubes de palabras, revelando patrones en grandes volúmenes de datos.
- Obtener las tendencias de las publicaciones por disciplina biológica entre 2000 a 2025.
- Generar gráficas donde se observa la distribución temporal de las menciones totales de la IA dentro las ciencias biológicas.
    
## **Metodología**

- Definición de términos de búsqueda: Combinación de términos de IA y campo de biología.
- Búsqueda y extracción de metadatos: Por medio del uso de la API de Pubmed, se procesaron los registros.
- Limpieza de datos: Eliminación de duplicados y homogeneización de los términos
- Análisis de palabras clave: Conteo de términos 
- Visualizacón: Generación de gráficos y nubes de palabras.

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

 - Dentro del código es posible encontrar listas para modificar las solicitudes de búsqueda y están divididos como:
   ```Campo de la biología: Bioinformática, Biología, Biomedicina, Ecología, Genética. Términos de la IA: Inteligencia Artificial, Machine Learning, Deep Learning.```
   - Las búsquedas se limitan a 500 artículos por combinación de términos, en un periodo de 2000-2025
   - Visualización de datos

**Palabras clave más frecuentes**
![common_keywords](https://github.com/user-attachments/assets/7579523f-c79f-43df-9175-a1814ec2b037)


**Nube de palabras**
![wordcloud_freq](https://github.com/user-attachments/assets/049f336a-6a3e-40aa-8f60-79e7eb4d83f4)

**Gráfica por disciplina biológica**
![barplot_count](https://github.com/user-attachments/assets/9cd08c01-c983-421f-9711-6c6c4844aafe)

**Total de menciones de IA**
![total_pub](https://github.com/user-attachments/assets/ecdf4228-a2dd-4617-83bf-7df776ea19be)

**Este proyecto fue desarrollado como parte del programa de servicio social en la Unidad de Bioinformática y Manejo de la Información del Instituto de Fisiología Celular, UNAM.**
