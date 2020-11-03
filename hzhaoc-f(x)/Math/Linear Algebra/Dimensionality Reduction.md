## 1. Singular Value Decomposition
([MIT Tutorial](https://web.mit.edu/be.400/www/SVD/Singular_Value_Decomposition.htm))
$$X=U\Sigma V^T$$
where
$U^TU=V^TV=I$ (orthogonal matrix)
### property
- V, are eigenvectors of $X^TX$, such that $X^TX=V\Sigma^2 V^T$
- U are eigenvectors of $XX^T$, such that $XX^T=U\Sigma^2 U^T$

## 2. Eigenvalue Decomposition
A special case of SVD.
### PCA
-> $X^TX=V\Sigma^2 V^T$
-> $Z_k = U_k^TX$
-> $X_{approx} = U_kZ_k$
### PCA explained variance
$$EV = \frac{||X-X_{approx}||_2^2}{||X||_2^2}$$

## 3. CUR decomposition
Given a matrix A, find C, R, U such that $\Vert A-CUR \Vert$ is small. This works better to  decompose sparse matrix compared with SVD. C and R are samples of horizontal or vertical vectors from A.

If a sparse matrix is computationally cheaper than a dense matrix, CUR decomposition can be more efficient than SVD.

## 3. Tensor Factorization
### Tensor order, modes, rank
### CP decomposition
[Explain](https://www.zhihu.com/question/29788048)