# NLP Lab 04 - Bag of Words & Cosine Similarity

This repository contains the work for **NLP Lab 04**.  
The lab covers **Bag of Words (BoW)** and **Cosine Similarity** for representing and comparing text documents.

## Student Information

- **Name:** Fatima Channa
- **Roll Number:** 2K24/Ai/25
- **Course:** Natural Language Processing
- **University:** University of Sindh, Jamshoro

---

## Task 1: Bag of Words

In Task 1, three customer reviews were converted into numerical form using the **Bag of Words** technique.

### Method Used

- Created a corpus of customer reviews.
- Used `CountVectorizer` from Scikit-learn.
- Removed English stop words.
- Generated the vocabulary.
- Created a word-frequency matrix.

### Output
<img width="688" height="110" alt="task1_output" src="https://github.com/user-attachments/assets/0fab11a2-c856-4ea3-b178-9d2043253f6c" />


---

## Task 2: Cosine Similarity

In Task 2, a simple document search system was created using **Bag of Words** and **Cosine Similarity**.

### Method Used

- Created four documents.
- Created a search query.
- Converted documents and query into numerical vectors.
- Calculated cosine similarity.
- Ranked documents from highest to lowest similarity.

### Query

`machine learning algorithms for data`

### Output

<img width="708" height="210" alt="task2_output" src="https://github.com/user-attachments/assets/900b528b-ffe3-4b43-af40-c5fc5375ab45" />

---

## Viva Questions

### 1. Why does Bag of Words ignore word order?

Bag of Words only counts the occurrence of words. It does not consider the order of words.

For example:

- `Dog bites man`
- `Man bites dog`

can have the same Bag of Words representation even though their meanings are different.

### 2. What is sparsity?

Sparsity occurs when a large vocabulary is used but each document contains only a few of those words. As a result, the matrix contains many zero values.

For example, a vocabulary of 100,000 words can create a large matrix with many zeros.

### 3. Why can cosine similarity be zero?

Cosine similarity can be zero when the query and a document have no common words. Their vectors have no overlapping non-zero values.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Cosine Similarity

---

## Files

- `Task_1_solution.py` - Task 1 solution
- `Task2_solution.py` - Task 2 solution
- `README.md` - Project documentation

---

## Conclusion

This lab helped in understanding how **Bag of Words** represents text numerically and how **Cosine Similarity** can be used to compare documents and rank them according to their similarity.
