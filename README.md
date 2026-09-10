# NLP Lab 04 - Bag of Words & Cosine Similarity

This repository contains my work for **NLP Lab 04**. In this lab, I worked with **Bag of Words (BoW)** and **Cosine Similarity** to represent text as numerical vectors and compare documents.

## Student Information

- **Name:** Fatima Channa
- **Roll Number:** 2K24/Ai/25
- **Course:** Natural Language Processing
- **University:** University of Sindh, Jamshoro

---

## Task 1 - Bag of Words Matrix Construction

In Task 1, I used three customer reviews to create a **Bag of Words matrix**.

I used `CountVectorizer` from Scikit-learn with English stop words removed. The program extracts the vocabulary from the reviews and converts the words into numerical values based on their frequency.

The resulting matrix shows the occurrence of each word in the three reviews.

### Task 1 Output

![Task 1 Output](task1_output.png)

---

## Task 2 - Document Search Engine & Relevance Ranking

In Task 2, I created a simple document search engine using **Bag of Words** and **Cosine Similarity**.

The documents and search query are converted into numerical vectors using `CountVectorizer`. Cosine Similarity is then used to compare the query with each document.

The documents are ranked from the highest similarity score to the lowest similarity score.

The query used was:

```text
machine learning algorithms for data
