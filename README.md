# Image Compression using SVD (Singular Value Decomposition)

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)

这是一个基于 **SVD（奇异值分解）** 实现的数字图像压缩项目。该项目演示了如何利用线性代数中的低秩近似（Low-Rank Approximation）技术，提取图像的核心几何特征与光影基调，去除冗余的高频噪声，从而在保持画质清晰的同时实现大幅度的数据瘦身。

---

## 📌 项目核心原理

在计算机中，一张单通道灰度图片本质上是一个大小为 $m \times n$ 的二维矩阵 $A$。SVD 将该矩阵分解为三个矩阵的乘积：

$$A = U \Sigma V^T$$

- **$U$ (左奇异矩阵)**：尺寸为 $m \times m$，每一列（列向量）代表图像在**垂直方向**上的几何特征（即行对比度权重标尺）。
- **$\Sigma$ (奇异值对角阵)**：尺寸为 $m \times n$，对角线上的数值称为**奇异值**，严格按从大到小的顺序排列。它们代表各个特征分量的**能量权重**。
- **$V^T$ (右奇异矩阵转置)**：尺寸为 $n \times n$，每一行（行向量）代表图像在**水平方向**上的几何特征（即列对比度权重标尺）。

### 💡 为什么能压缩？（低秩近似）
图像的能量通常高度集中在前几个极大的奇异值中。通过截取前 $k$ 个奇异值及其对应的左右奇异向量（即 `经济型 SVD` 裁剪），我们可以用极少的数据量重构全尺寸的图像：

$$\text{img\_k} = U_k \cdot \text{diag}(\Sigma_k) \cdot V_k^T$$

本项目通过递增 $k$ 值 ($1, 5, 10, \dots, 500$)，直观地展示了图像从“极度模糊的能量光晕”过渡到“高保真写实风景”的物理全过程。

---

## 📂 项目文件结构

```text
.
├── Lab 2.py          # 图像压缩的核心 Python 源代码
├── sample.jpg        # 原始输入的风景图像（彩色/灰度均可）
└── README.md         # 项目说明文档
