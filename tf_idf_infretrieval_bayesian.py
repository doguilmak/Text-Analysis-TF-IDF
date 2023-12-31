# -*- coding: utf-8 -*-
"""TF_IDF_InfRetrieval_Bayesian.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1la8LHLZeG1jEnoXR2NXjkNnCn3aZbYNB

<h1 align=center><b>Bayesian Probabilistic Retrieval Strategy</b></font></h1>

<br>

<p align="center">
    <img src="https://images.pexels.com/photos/1309899/pexels-photo-1309899.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" height=450 width=2000 alt="European Commission">
</p>

<small>Picture Source: <a href="https://www.pexels.com/@jimbear/">Jimmy Chan</a></small>

<br>

<h2><b>Bayesian Probabilistic Retrieval Strategy</b></h2>

- **Information Retrieval (IR):** Information retrieval is a fundamental process for extracting pertinent information from extensive data repositories. It primarily involves searching for documents or text segments that are relevant to a user's query.

- **Bayesian Probabilistic Retrieval:** Bayesian probabilistic retrieval is a significant framework within information retrieval that employs probability theory to assess document relevance to a user's query. It is based on the concept that information retrieval can be approached as a probabilistic decision-making process.

- **Document and Query Representation:** In Bayesian probabilistic retrieval, documents and queries are represented as probabilistic models. These models capture the likelihood of observing particular terms within documents and queries, and they help in estimating the relevance of documents.

- **Incorporating Prior Information:** The Bayesian approach allows for the incorporation of prior knowledge or prior beliefs about the likelihood of documents being relevant. This enables a more nuanced and personalized retrieval process.

- **Scoring Documents:** In this strategy, documents are scored based on the probability that they are relevant given the observed terms in the query. Documents with higher probability scores are considered more relevant.

- **Combining Probabilities:** Bayesian probabilistic retrieval combines the probabilities associated with each term in the query to calculate an overall document relevance score. This approach takes into account both the presence and absence of terms in documents.

- **Ranking Documents:** The final step involves ranking documents based on their relevance scores. This ranking is used to present the most relevant documents to the user.

<br>

Bayesian probabilistic retrieval offers a principled and flexible approach to information retrieval by explicitly modeling the uncertainty and probabilistic nature of the retrieval process. It is widely employed in various information retrieval applications, including search engines, recommendation systems, and text classification. By understanding Bayesian probabilistic retrieval, you gain insights into how information retrieval can be approached as a probabilistic decision-making process, allowing for more nuanced and accurate retrieval results.

<br>


**Reference:** **[Information Retrieval](https://www.google.com.tr/books/edition/Information_Retrieval/65oACAAAQBAJ?hl=en&gbpv=0)** By David A. Grossman, Ophir Frieder · 2004

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
  <li>Bayesian Probabilistic Retrieval</li>
  <li>Text Analysis</li>
  <li>Information Retrieval</li>
  <li>Probabilistic Models</li>
</ul>

<br>

<h2><b>Table of Contents</b></h2>

<div class="alert alert-block alert-info" style="margin-top: 20px">
<li><a href="">Importing Libraries</a></li>
<li><a href="">Building Unique Words List Using TF-IDF Vectorization</a></li>
<li><a href="">Calculating Weights</a></li>
<li><a href="">Document Weights</a></li>

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

def combine_calculations(query_unique, doc_list, N_doc, R_doc, doc_indices_to_search=None):
    result_dict = {}

    for idx, document in enumerate(doc_list):
        for value in query_unique:
            if value not in result_dict:
                result_dict[value] = [0] * len(doc_list)
            if value in document:
                result_dict[value][idx] += 1

    df = pd.DataFrame(result_dict, columns=query_unique)
    summary = df.sum(axis=0).to_frame().T
    summary.index = ['n-document']

    df.loc['N'] = N_doc
    df.loc['R'] = R_doc
    df = pd.concat([df, summary])

    if doc_indices_to_search is not None:
        r_relation = [sum(df[col][doc_indices_to_search]) for col in df.columns]
        df.loc['r-relation'] = r_relation

    df = df.loc[['n-document', 'N', 'r-relation', 'R']]

    return df

def calculate_w(r_rel, R, n_doc, N, case):
    if case == 1:
        numerator = ((r_rel + 0.5) / (R + 1))
        denominator = ((n_doc + 1) / (N + 2))
    elif case == 2:
        numerator = ((r_rel + 0.5) / (R + 1))
        denominator = ((n_doc - r_rel + 0.5) / (N - R + 1))
    elif case == 3:
        numerator = ((r_rel + 0.5) / (R - r_rel + 0.5))
        denominator = ((n_doc + 1) / (N - n_doc + 1))
    elif case == 4:
        numerator = ((r_rel + 0.5) / (R - r_rel + 0.5))
        denominator = ((n_doc - r_rel + 0.5) / ((N - n_doc) - (R - r_rel) + 0.5))
    else:
        raise ValueError("Invalid case")

    return round(math.log10(numerator / denominator), 3)

"""## **Get Unique Words with TF-IDF**"""

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

"""### **Assumptions**"""

doc_list = [
    d_1_unique,
    d_2_unique,
    d_3_unique,
]

doc_indices_to_search = [1, 2] # Specify the indices of the documents you want to search.
                               # It is starting from 0!

N_doc = 3 # @param {type:"number"}
R_doc = len(doc_indices_to_search)

result_df = combine_calculations(query_unique, doc_list, N_doc, R_doc, doc_indices_to_search)
result_df

"""## **Calculating Weights**

In the realm of Bayesian probabilistic retrieval, the process of determining the relevance of documents to a user's query is a multifaceted task, and the calculated weights play a pivotal role in this endeavor. We employ four distinct weight calculation schemes, namely w1, w2, w3, and w4, each tailored to address specific aspects of relevance assessment. These calculations involve intricate considerations, taking into account parameters such as binary relevance, document frequencies, and prior beliefs. For w1 and w2, we scrutinize the term's presence in relevant and non-relevant documents, while w3 and w4 delve into the balance between relevance and non-relevance. The resulting weights serve as a quantitative measure of a document's likelihood to satisfy a user's information needs. By dissecting the complexities of these weight calculations, we gain deeper insights into the nuances of document ranking and retrieval within a Bayesian probabilistic framework.

### **Calculating W1**

In the context of Bayesian probabilistic retrieval, $w1$ represents the weight assigned to a term based on the binary relevance ($r_{rel}$) of a document, the total number of relevant documents ($R$), the number of documents containing the term ($n_{doc}$), and the total number of documents in the collection ($N$). The formula calculates the weight by considering the term's relevance in terms of its presence in relevant documents and adjusts it based on the overall document frequency of the term.

<br>

$$
w_1 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R + 1}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} + 1}{N + 2}\right)
$$
"""

w1 = []

for column in result_df.columns:
    r_rel = result_df.loc['r-relation', column]
    R = result_df.loc['R', column]
    n_doc = result_df.loc['n-document', column]
    N = result_df.loc['N', column]
    w_1 = calculate_w(r_rel, R, n_doc, N, case=1)
    w1.append(w_1)
    print(f'{column}: {w_1}')

"""### **Calculating W2**

W2 is another weight in Bayesian probabilistic retrieval, and it takes into account binary relevance, document frequency, and the overall collection statistics. The formula accounts for the presence of the term in both relevant and non-relevant documents ($r_{rel}$ and $n_{doc} - r_{rel}$), and it adjusts the weight based on the number of relevant documents ($R$) and the total collection size ($N$).

<br>

$$
w_2 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R + 1}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} - r_{\text{rel}} + 0.5}{N - R + 1}\right)
$$
"""

w2 = []

for column in result_df.columns:
    r_rel = result_df.loc['r-relation', column]
    R = result_df.loc['R', column]
    n_doc = result_df.loc['n-document', column]
    N = result_df.loc['N', column]
    w_2 = calculate_w(r_rel, R, n_doc, N, case=2)
    w2.append(w_2)
    print(f'{column}: {w_2}')

"""### **Calculating W3**

'w3' introduces a different weighting approach by considering the term's relevance in relation to its non-relevance and adjusting the weight accordingly.
This formula is based on the idea that the presence of a term in non-relevant documents ($R - r_{rel}$) may also provide valuable information for ranking documents.

<br>

$$
w_3 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R - r_{\text{rel}} + 0.5}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} + 1}{N - n_{\text{doc}} + 1}\right)
$$
"""

w3 = []

for column in result_df.columns:
    r_rel = result_df.loc['r-relation', column]
    R = result_df.loc['R', column]
    n_doc = result_df.loc['n-document', column]
    N = result_df.loc['N', column]
    w_3 = calculate_w(r_rel, R, n_doc, N, case=3)
    w3.append(w_3)
    print(f'{column}: {w_3}')

"""### **Calculating W4**

'w4' further refines the weighting strategy by considering both relevant and non-relevant documents while taking into account the term's presence in the collection. It balances the relevance and non-relevance of the term in documents, ensuring that it captures the subtleties in the document-term relationship.

<br>

$$
w_4 = \log_{10}\left(\frac{r_{\text{rel}} + 0.5}{R - r_{\text{rel}} + 0.5}\right) \cdot \log_{10}\left(\frac{n_{\text{doc}} - r_{\text{rel}} + 0.5}{(N - n_{\text{doc}}) - (R - r_{\text{rel}}) + 0.5}\right)
$$
"""

w4 = []

for column in result_df.columns:
    r_rel = result_df.loc['r-relation', column]
    R = result_df.loc['R', column]
    n_doc = result_df.loc['n-document', column]
    N = result_df.loc['N', column]
    w_4 = calculate_w(r_rel, R, n_doc, N, case=4)
    w4.append(w_4)
    print(f'{column}: {w_4}')

data = {
    'w1': w1,
    'w2': w2,
    'w3': w3,
    'w4': w4,
}

df = pd.DataFrame(data, index=query_unique)
df

"""These 'w' values play a crucial role in Bayesian probabilistic retrieval, helping to determine the relevance and ranking of documents within an information retrieval system. They provide a sophisticated framework for document ranking by considering both term presence and relevance information.

<h1>Contact Me</h1>
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")