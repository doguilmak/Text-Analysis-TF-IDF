# -*- coding: utf-8 -*-
"""TF-IDF_InfRetrieval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSZwdSZZmBptI954Bdgc13FipvaFMcmm

<h1 align=center><b>Text Analysis and Information Retrieval with TF-IDF</b></font></h1>

<br>

<p align="center">
    <img src="https://viso.ai/wp-content/uploads/2022/07/natural-language-processing-nlp-viso-ai.png" height=450 width=2000 alt="European Commission">
</p>

<small>Picture Source: <a href="https://viso.ai/deep-learning/natural-language-processing/">viso.ai</a></small>

<br>

 In the context of information retrieval, the inner product refers to the mathematical operation that measures the similarity or relevance between two vectors, often used to compare documents or text to a query.

<br>

<h2><b>Inner Product in Information Retrieval</b></h2>

- **Information Retrieval (IR):** Information retrieval is the process of obtaining relevant information from a vast collection of data. In IR, the most common scenario is searching for documents or text passages that are relevant to a user's query.

- **Vector Space Model (VSM):** In information retrieval, the Vector Space Model is a fundamental framework used to represent both documents and queries as vectors in a multi-dimensional space. Each dimension corresponds to a unique term (word) in the entire document collection.

- **Inner Product:** The inner product (also known as the dot product) is a mathematical operation that measures the similarity between two vectors. For text documents, the vectors represent the presence and frequency of terms (words) in the documents.

- **Scoring Documents:** To determine the relevance of documents to a user's query, the inner product is often used to calculate a similarity score. The higher the inner product between a document vector and a query vector, the more relevant the document is to the query.

- **Calculation:** The inner product is computed by taking the sum of the products of the corresponding components of two vectors.

The inner product produces a real number that serves as a relevance score. Documents with higher scores are considered more relevant to the query, making the inner product a key component of ranking algorithms used in information retrieval systems. The inner product is used in various information retrieval tasks, including document retrieval, web search engines, recommendation systems, and natural language processing applications. By the end of this project, you will have a practical understanding of TF-IDF, text analysis, and information retrieval.

<br>

**TIP: If you are going to add more documents ($d_n)$ for the query, please spesify query at the end of the dictionary.**

Example:

```
d_1 = "shipment of gold damaged in a fire"
d_2 = "delivery of silver arrived in a silver truck"
d_3 = "shipment of gold arrived in a truck"
query = "gold silver truck"
```

<br>

<h2><b>Keywords</b></h2>
<ul>
  <li>TF-IDF Analysis</li>
  <li>Natural Language Processing (NLP)</li>
  <li>Text Document Similarity</li>
  <li>Information Retrieval</li>
  <li>Word Frequency Analysis</li>
</ul>

<br>

<h2><b>Table of Contents</b></h2>

<div class="alert alert-block alert-info" style="margin-top: 20px">
<li><a href="">Importing Libraries</a></li>
<li><a href="">Building Unique Words List Using TF-IDF Vectorization</a></li>
<li><a href="">Calculating Frequency and Log Frequency of the Unique Words</a></li>
<li><a href="">Calculating Inner Product</a></li>

<br>

## **Importing Libraries**
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import math
import pandas as pd

"""## **Building Unique Words List Using TF-IDF Vectorization**

The **TfidfVectorizer** is a component of the scikit-learn library used for text analysis and natural language processing. *TF-IDF* stands for *Term Frequency-Inverse Document Frequency* which is a numerical statistic that reflects the importance of a word within a document relative to a collection of documents (corpus).

### Creating Funtions for DRY
"""

def get_unique_words(sentence):
    sentence = sentence.lower()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([sentence])
    unique_words = vectorizer.get_feature_names_out()
    return unique_words

def get_words(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    return words

def calculate_word_frequencies(document):
    words = get_words(document)
    word_frequencies = {word: words.count(word) for word in words}
    return word_frequencies

def create_word_frequencies_df(unique_words, word_frequencies_dict):
    df = pd.DataFrame(index=word_frequencies_dict.keys(), columns=unique_words)

    for index, row in df.iterrows():
        document_name = index
        word_frequencies = word_frequencies_dict.get(document_name, {})

        for column in df.columns:
            if column in word_frequencies:
                row[column] = word_frequencies[column]
            else:
                row[column] = 0

    df = df.fillna(0)

    return df

d_1 = "shipment of gold damaged in a fire"
d_2 = "delivery of silver arrived in a silver truck"
d_3 = "shipment of gold arrived in a truck"
query = "gold silver truck"
# Add more documents here as needed!

d_1_unique = get_unique_words(d_1)
d_2_unique = get_unique_words(d_2)
d_3_unique = get_unique_words(d_3)
query_unique = get_unique_words(query)
# Add more documents here as needed!

query_unique

d_1_unique

d_2_unique

d_3_unique

"""## **Calculating Frequency and Log Frequency of the Unique Words**

$$D_i = <d_{i1}, d_{i2}, ..., d_{in}> $$

<br>

$$Q = <w_{q1}, w_{q2}, ..., w_{qn}> $$

<br>

In this process, we start by alphabetically listing all words present in the documents. We then calculate the frequency of each word within the documents. Next, we calculate word weights based on a logarithmic transformation using a base of 10, achieved by dividing the number of documents by the word frequency values.

$$ \log_{10}(\frac{3}{frequency}) $$

<br>
"""

combined_text = f"{d_1_unique} {d_2_unique} {d_3_unique}" # Add more documents here as needed!
unique_words = get_unique_words(combined_text)
word_frequencies = {word: combined_text.count(word) for word in unique_words}

log_freq = []

for i, (word, frequency) in enumerate(sorted(word_frequencies.items()), start=1):
    log_frequency = round(math.log10(3 / frequency), 3)
    log_freq.append(log_frequency)
    print(f"{i}. {word}\nFrequency: {frequency}\nLog frequency: {log_frequency}\n")

word_frequencies_d1 = calculate_word_frequencies(d_1)
word_frequencies_d2 = calculate_word_frequencies(d_2)
word_frequencies_d3 = calculate_word_frequencies(d_3)
word_frequencies_query = calculate_word_frequencies(query)
# Add more documents here as needed!

word_frequencies_dict = {
    "d_1_unique": word_frequencies_d1,
    "d_2_unique": word_frequencies_d2,
    "d_3_unique": word_frequencies_d3,
    "query_unique": word_frequencies_query,
    # Add more documents here as needed!
}

df = create_word_frequencies_df(unique_words, word_frequencies_dict)

df

"""$$d_{ij} = tf_{ij} \cdot idf_{j} $$"""

for i in range(len(unique_words)):

  column_name = unique_words[i]
  constant = log_freq[i]

  if column_name in df.columns:
      df[column_name] = df[column_name] * constant

df

"""### Inverted Index

In information retrieval and text/document similarity, an inverted index is a data structure that allows for the quick and efficient retrieval of documents that contain specific words or terms.
"""

df.T

"""## Calculating Inner Product

$$ SC(Q, D_{i}) =  \sum_{j=1}^{n} w_{qj} \cdot d_{ij}$$

<br>

Formula used to calculate the similarity (or score) between a query and a document. Here's what each part of the formula represents:

- $SC(Q, D_i)$: This represents the similarity score (or similarity coefficient) between a query denoted as "$Q$" and a document denoted as "$D_i$."

- $\sum$: The summation symbol, indicating that we are summing the results of the products of the terms within the summation.

- $j=1$ and $n$: These specify the range of values for the index variable "j." The summation is performed for all "$j$" values from 1 to "$n$".

- $w_{qj}$: This represents the weight of the term (or word) "$j$" in the query "$Q$".

- $d_{ij}$: This represents the weight of the term "$j$" in the document "$D_i$."

<br>

Essentially, the formula computes the similarity score between a query and a document by summing the products of the weights of corresponding terms in both the query and the document. This is often used in information retrieval and text search to rank documents based on their relevance to a given query. The higher the similarity score, the more relevant the document is considered to be to the query.
"""

last_row = df.iloc[-1, :]
dot_products = []

for i, row in df.iterrows():
    if i != df.index[-1]:
        dot_product = sum(last_row * row)
        dot_products.append(round(dot_product, 3))

dot_product_series = pd.Series(dot_products)

dot_product_series

"""As we can see from the dot product, **document 2 is giving the best result for our query with  0.486 value.**

<h1>Contact Me</h1>
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")