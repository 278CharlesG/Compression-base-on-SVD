# Image Compression using SVD (Singular Value Decomposition)

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)

This project demonstrates digital image compression implemented via **SVD (Singular Value Decomposition)**. It showcases how to leverage low-rank approximation from linear algebra to extract core geometric features and lighting bases from an image, discarding redundant high-frequency noise to achieve significant data reduction while keeping the visual output clear.

---

## 📌 Core Principles

In computing, a single-channel grayscale image is essentially an $m \times n$ two-dimensional matrix $A$. SVD decomposes this matrix into the product of three distinct matrices:

$$A = U \Sigma V^T$$

- **$U$ (Left Singular Matrix)**: Dimension $m \times m$. Each column  represents the geometric features of the image in the **vertical direction** (acting as a row contrast weight scale).
- **$\Sigma$ (Singular Value Diagonal Matrix)**: Dimension $m \times n$ . The values along the diagonal are called **singular values**, strictly sorted in descending order. They represent the energy weight of each feature component.
- **$V^T$ (Right Singular Matrix Transposed)**: Dimension $n \times n$ . Each row  represents the geometric features of the image in the **horizontal direction** (acting as a column contrast weight scale).

## Compression Ratio:                  

$$\text{Ratio} = \frac{k \times (1 + m + n)}{m \times n} \times 100\%$$

Compression Ratio: Measures the percentage of data retained in the truncated matrices ($U_k$, $\Sigma_k$, and $V_k^T$) relative to the original image size; a lower percentage indicates higher data savings and greater storage efficiency
