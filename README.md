
<h1 align=center><b>Text Analysis and Information Retrieval with TF-IDF</b></font></h1>

<br>

<p align="center">
    <img src="https://images.pexels.com/photos/1309899/pexels-photo-1309899.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" height=450 width=2000 alt="European Commission">
</p>

<small>Picture Source: <a href="https://www.pexels.com/@jimbear/">Jimmy Chan</a></small>

<br>

## Introduction

The TF-IDF (Term Frequency-Inverse Document Frequency) vectorization is a key concept in information retrieval and extraction. It measures the importance of words within a document relative to a collection of documents (corpus). This project provides tools to:
- Extract unique words from a sentence using TF-IDF vectorization.
- Calculate word frequencies within a document.
- Merge and analyze multiple sentences to find the union of unique words and their frequencies.

<br>

## Keywords  

- TF-IDF Analysis 
- Bayesian Probabilistic Retrieval 
- Text Analysis - Information Retrieval 
- Probabilistic Models

<br>

## Information Retrieval

Information retrieval is the process of obtaining relevant information from a vast collection of data. In information retrieval, the most common scenario is searching for documents or text passages that are relevant to a user's query. It involves various techniques and models to assess and rank the relevance of documents to a given query.

**Reference**: [Information Retrieval](https://www.google.com.tr/books/edition/Information_Retrieval/65oACAAAQBAJ?hl=en&gbpv=0) By David A. Grossman, Ophir Frieder · 2004

<br>

### Text Analysis and Information Retrieval with TF-IDF

This project, "Text Analysis and Information Retrieval with TF-IDF," focuses on leveraging TF-IDF vectorization to perform text analysis and information retrieval. TF-IDF is a numerical statistic that reflects the importance of a word within a document relative to a collection of documents (corpus).

#### Content

In this project, TF-IDF is used to:

1. Extract unique words from a sentence: TF-IDF is employed to identify and extract unique words from a given text. This process is crucial for understanding the vocabulary and content of the document.

2. Calculate word frequencies within a document: TF-IDF is used to calculate the importance of each word in a document by considering its frequency in the document and its prevalence in the entire document collection.

3. Merge and analyze multiple sentences: The project combines and analyzes multiple sentences to find the union of unique words and their frequencies. This is essential for identifying common terms across different documents.

The inner product produces a real number that serves as a relevance score. Documents with higher scores are considered more relevant to the query, making the inner product a key component of ranking algorithms used in information retrieval systems. The inner product is used in various information retrieval tasks, including document retrieval, web search engines, recommendation systems, and natural language processing applications. By the end of this project, you will have a practical understanding of TF-IDF, text analysis, and information retrieval.

<br>

$$ SC(Q, D_{i}) =  \sum_{j=1}^{n} w_{qj} \cdot d_{ij}$$

<br>

Formula used to calculate the similarity (or score) between a query and a document. Here's what each part of the formula represents:

- $SC(Q, D_i)$: This represents the similarity score (or similarity coefficient) between a query denoted as $Q$ and a document denoted as $D_i$.

- $\sum$: The summation symbol, indicating that we are summing the results of the products of the terms within the summation.

- $j=1$ and $n$: These specify the range of values for the index variable $j$. The summation is performed for all $j$ values from 1 to $n$.

- $w_{qj}$: This represents the weight of the term (or word) $j$ in the query $Q$.

- $d_{ij}$: This represents the weight of the term $j$ in the document $D_i$.

<br>

Here you can find relevant notebook of the project: [TF_IDF_InfRetrieval.ipynb](Bayesian%20Probabilistic%20Retrieval%20Strategy)

<br>

### Bayesian Probabilistic Retrieval Strategy

The second project, "Bayesian Probabilistic Retrieval Strategy," delves into the probabilistic approach to information retrieval. It leverages probability theory to assess the relevance of documents to a user's query.

#### Content

In this project, Bayesian probabilistic retrieval is employed to:

1. Represent documents and queries as probabilistic models: Documents and queries are represented as probabilistic models that capture the likelihood of observing particular terms within them. These models help estimate the relevance of documents.

2. Incorporate prior information: The Bayesian approach allows for the incorporation of prior knowledge or beliefs about the likelihood of documents being relevant. This enables a more personalized retrieval process.

3. Score documents based on probabilities: Documents are scored based on the probability that they are relevant given the observed terms in the query. Documents with higher probability scores are considered more relevant.

4. Combine probabilities for ranking: Bayesian probabilistic retrieval combines the probabilities associated with each term in the query to calculate an overall document relevance score. This approach takes into account both the presence and absence of terms in documents.

By understanding Bayesian probabilistic retrieval, you gain insights into how information retrieval can be approached as a probabilistic decision-making process, allowing for more nuanced and accurate retrieval results using weights. 

<br>

In the realm of Bayesian probabilistic retrieval, the process of determining the relevance of documents to a user's query is a multifaceted task, and the calculated weights play a pivotal role in this endeavor. We employ four distinct weight calculation schemes, namely w1, w2, w3, and w4, each tailored to address specific aspects of relevance assessment.

<br>

$$
w_1 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R + 1}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} + 1}{N + 2}\right)
$$

<br>

$$
w_2 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R + 1}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} - r_{\text{rel}} + 0.5}{N - R + 1}\right)
$$

<br>

$$
w_3 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R - r_{\text{rel}} + 0.5}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} + 1}{N - n_{\text{doc}} + 1}\right)
$$

<br>

$$
w_4 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R - r_{\text{rel}} + 0.5}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} - r_{\text{rel}} + 0.5}{(N - n_{\text{doc}}) - (R - r_{\text{rel}}) + 0.5}\right)
$$

<br>

Here you can find relevant notebook of the project: [TF_IDF_InfRetrieval_Bayesian.ipynb](Bayesian%20Probabilistic%20Retrieval%20Strategy)

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
