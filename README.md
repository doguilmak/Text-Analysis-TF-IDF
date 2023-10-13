
<h1 align=center><b>Text Analysis and Information Retrieval with TF-IDF</b></font></h1>

<br>

<p align="center">
    <img src="https://viso.ai/wp-content/uploads/2022/07/natural-language-processing-nlp-viso-ai.png" height=450 width=2000 alt="European Commission">
</p>

<small>Picture Source: <a href="https://viso.ai/deep-learning/natural-language-processing/">viso.ai</a></small>

<br>

## Introduction

The TF-IDF (Term Frequency-Inverse Document Frequency) vectorization is a key concept in natural language processing (NLP) and information retrieval. It measures the importance of words within a document relative to a collection of documents (corpus). This project provides tools to:
- Extract unique words from a sentence using TF-IDF vectorization.
- Calculate word frequencies within a document.
- Merge and analyze multiple sentences to find the union of unique words and their frequencies.

<br>


<h2><b>Inner Product in Information Retrieval</b></h2>

- **Information Retrieval (IR):** Information retrieval is the process of obtaining relevant information from a vast collection of data. In IR, the most common scenario is searching for documents or text passages that are relevant to a user's query.

- **Vector Space Model (VSM):** In information retrieval, the Vector Space Model is a fundamental framework used to represent both documents and queries as vectors in a multi-dimensional space. Each dimension corresponds to a unique term (word) in the entire document collection.

- **Inner Product:** The inner product (also known as the dot product) is a mathematical operation that measures the similarity between two vectors. For text documents, the vectors represent the presence and frequency of terms (words) in the documents.

- **Scoring Documents:** To determine the relevance of documents to a user's query, the inner product is often used to calculate a similarity score. The higher the inner product between a document vector and a query vector, the more relevant the document is to the query.

- **Calculation:** The inner product is computed by taking the sum of the products of the corresponding components of two vectors.

The inner product produces a real number that serves as a relevance score. Documents with higher scores are considered more relevant to the query, making the inner product a key component of ranking algorithms used in information retrieval systems. The inner product is used in various information retrieval tasks, including document retrieval, web search engines, recommendation systems, and natural language processing applications. By the end of this project, you will have a practical understanding of TF-IDF, text analysis, and information retrieval.

$$ SC(Q, D_{i}) =  \sum_{j=1}^{n} w_{qj} \cdot d_{ij}$$

<br>

Formula used to calculate the similarity (or score) between a query and a document. Here's what each part of the formula represents:

- $SC(Q, D_i)$: This represents the similarity score (or similarity coefficient) between a query denoted as "$Q$" and a document denoted as "$D_i$."

- $\sum$: The summation symbol, indicating that we are summing the results of the products of the terms within the summation.

- $j=1$ and $n$: These specify the range of values for the index variable "j." The summation is performed for all "$j$" values from 1 to "$n$".

- $w_{qj}$: This represents the weight of the term (or word) "$j$" in the query "$Q$".

- $d_{ij}$: This represents the weight of the term "$j$" in the document "$D_i$."

<br>

## Usage

1. Clone the repository:

`git clone https://github.com/doguilmak/Text-Analysis-TF-IDF.git`

2. Run the notebook.

<br>

<h1>Contact Me</h1>
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
