# Image Compression using SVD (Singular Value Decomposition)

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)

This project demonstrates digital image compression implemented via **SVD (Singular Value Decomposition)**. It showcases how to leverage low-rank approximation from linear algebra to extract core geometric features and lighting bases from an image, discarding redundant high-frequency noise to achieve significant data reduction while keeping the visual output clear.

---

## 📌 Core Principles

In computing, a single-channel grayscale image is essentially an $m \times n$ two-dimensional matrix $A$. SVD decomposes this matrix into the product of three distinct matrices:

$$A = U \Sigma V^T$$

- **$U$ (Left Singular Matrix)**: Dimension $m \times m$ (or $m \times r$ in economic SVD). Each column (column vector) represents the geometric features of the image in the **vertical direction** (acting as a row contrast weight scale).
- **$\Sigma$ (Singular Value Diagonal Matrix)**: Dimension $m \times n$ (or an array of length $r$ in code implementation). The values along the diagonal are called **singular values**, strictly sorted in descending order. They represent the energy weight of each feature component.
- **$V^T$ (Right Singular Matrix Transposed)**: Dimension $n \times n$ (or $r \times n$ in economic SVD). Each row (row vector) represents the geometric features of the image in the **水平方向** (acting as a column contrast weight scale).

# Compression Ratio:                                                        $$\text{Ratio} = \frac{k \times (1 + m + n)}{m \times n} \times 100\%$$
