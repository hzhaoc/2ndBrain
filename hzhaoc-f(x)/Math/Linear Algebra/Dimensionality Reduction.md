## 1. Singular Value Decomposition
$$X=U\Sigma V^T$$
where
$U^TU=V^TV=I$
### property
- V are eigenvectors of the covariance matrix $X^TX$
- U are eigenvectors of the covariance matrix $XX^T$

## 2. Eigenvalue Decomposition
A special case of SVD.

## 3. CUR decomposition
Given a matrix A, find C, R, U such that $\Vert A-CUR \Vert$ is small. This works better to  decompose sparse matrix compared with SVD. C and R are samples of horizontal or vertical vectors from A.

If a sparse matrix is computationally cheaper than a dense matrix, CUR decomposition can be more efficient than SVD.

## 3. Tensor Factorization
### Tensor order, modes, rank
### CP decomposition
[Explain](https://www.zhihu.com/question/29788048)