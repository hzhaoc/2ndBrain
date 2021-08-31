Below is my work that implements a Matrix class which does matrix multiplication using a basic Strassen algorithm, a divide and conquer approach in a recursion flavor. See the `mult()` method.

Run time: $O(n^{\log_2^{7}})\approx{O(n^{2.8})}$

```python
class BaseMatrix:
	"""
	implement a matrix class that supports metrix relevant operations
	"""

	def inv(self, A):
		"""
		find inverse matrix of A
		@input: input square matrix A
		@output: inverse of A
		"""
		n = len(A)
		A, P = self._LUPDecompose(A, n)
		IA = [[0.0] * n for i in range(n)]
		# forward/backward substitution to solve IA from L/U and P
		for j in range(n):
			for i in range(n):
				IA[i][j] = 1.0 if P[i] == j else 0.0

				for k in range(i):
					IA[i][j] -= A[i][k] * IA[k][j]

			for i in range(n-1, -1, -1):
				for k in range(i+1, n):
					IA[i][j] -= A[i][k] * IA[k][j]

				IA[i][j] /= A[i][i]

		return IA

	def det(self, A):
		"""
		find determinant of square matrix A
		@input: input square matrix of size n
		@output: determinant of A
		"""
		n = len(A)
		A, P = self._LUPDecompose(A, n)
		det = A[0][0]
		
		for i in range(1, n):
			det *= A[i][i]
		
		return det if (P[n] - n)%2 == 0 else -det

	def mult(self, A, B): 
		""" 
		matrix multiplication with divide and conquer approach (Strassen Algorithm), recursive
		"""
		h, w = len(A), len(B[0])
		A, B = self._strassen_padding(A), self._strassen_padding(B)
		C_padded = self._strassen(A, B)
		C = [C_padded[i][:w] for i in range(h)]
		return C

	def add(self, A, B):
		"""matrix element-wise add"""
		if len(A) != len(B) or len(A[0]) != len(B[0]):
			raise ValueError("two matrixes should have same shape to perform element-wise oeprations")
		return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

	def sub(self, A, B):
		"""matrix element-wise subtract"""
		if len(A) != len(B) or len(A[0]) != len(B[0]):
			raise ValueError("two matrixes should have same shape to perform element-wise oeprations")
		return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

	def prod(self, A, B):
		"""matrix element-wise product"""
		if len(A) != len(B) or len(A[0]) != len(B[0]):
			raise ValueError("two matrixes should have same shape to perform element-wise oeprations")
		return [[A[i][j]*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

	def show(self, A):
		for i in A:
			print(i)

	def _strassen_base(self, A, B):
		"""
		base case for strassen algorithm, default is product of two numbers, 
		since its data structure is nested list, the product is represented by element-wise matrix product
		"""
		return self.prod(A, B)

	def _strassen_padding(self, A):
		w, h = len(A[0]), len(A)
		k = math.log(max(w, h), 2)
		if not k.is_integer():
			n = int(2**(k//1 + 1))
		else:
			n = int(2**k)
		return [A[i] + [0]*(n - w) if i < h else [0]*n for i in range(n)]

	def _strassen(self, A, B): 
	    """ 
	    matrix multiplication by divide and conquer approach, recursive
	    """
	  
	    # Base case when size of matrices is 1x1 
	    if len(A) == 1:
	    	return self._strassen_base(A, B)

	    # Split the matrices into blocks until base case is reached
	    a, b, c, d = self._split(A) 
	    e, f, g, h = self._split(B) 
	  
	    # Computing the 7 matrix multiplications recursively
	    m1 = self._strassen(a, self.sub(f, h))
	    m2 = self._strassen(self.add(a, b), h)         
	    m3 = self._strassen(self.add(c, d), e)         
	    m4 = self._strassen(d, self.sub(g, e))
	    m5 = self._strassen(self.add(a, d), self.add(e, h))
	    m6 = self._strassen(self.sub(b, d), self.add(g, h))   
	    m7 = self._strassen(self.sub(a, c), self.add(e, f))
	  
	    # Computing the values of the 4 blocks of the final matrix c
	    c11 = self.add(self.sub(self.add(m5, m4), m2), m6)
	    c12 = self.add(m1, m2)            
	    c21 = self.add(m3, m4)          
	    c22 = self.sub(self.sub(self.add(m1, m5), m3), m7)
	  
	    # Combining the 4 blocks into a single matrix by stacking horizontally and vertically
	    C = self._vstack(self._hstack(c11, c12), self._hstack(c21, c22))

	    return C

	def _split(self, mat): 
	    """ 
	    Splits a given matrix into 4 blocks 
	    """
	    h, w = len(mat), len(mat[0])
	    h2, w2 = h//2, w//2
	    return [mat[r][:w2] for r in range(h2)], \
	    	   [mat[r][w2:] for r in range(h2)], \
	    	   [mat[r][:w2] for r in range(h2, h)], \
	    	   [mat[r][w2:] for r in range(h2, h)]

	def _hstack(self, M1, M2):
		"""satck two matrixes into one horizontally"""
		w1, w2 = len(M1[0]), len(M2[0])
		h1, h2 = len(M1), len(M2)
		if h1 != h2:
			raise ValueError("two matrixes should have same height to be stacked horizontally")
		M0 = [[0 for x in range(w1+w2)] for y in range(h1)]
		i = 0
		while i < h1:
			M0[i] = M1[i] + M2[i]
			i+=1
		return M0

	def _vstack(self, M1, M2):
		"""satck two matrixes into one vertically"""
		w1, w2 = len(M1[0]), len(M2[0])
		h1, h2 = len(M1), len(M2)
		if w1 != w2:
			raise ValueError("two matrixes should have same width to be stacked vertically")
		M0 = [[0 for x in range(w1)] for y in range(h1+h2)]
		for i in range(h1+h2):
			if i < h1:
				M0[i] = M1[i]
			else:
				M0[i] = M2[i-h1]
		return M0

	def _LUPDecompose(self, A, n):
		"""
		LUP decomposition of matrix A
		@input
		A: input square matrix of dimension n
		@output
		A: matrix A is modified and contains a copy of both matrices L-E and U as A=(L-E)+U such that 
			it is a LUP decomposition where P*A=L*U. The permutation matrix is a integer list of size n+1
			containing column indexes of the represented permutation matrix P where the P has "1". The last 
			element P[n]=s+n, where s is the number of row exchanges of P from idendity matrix E, for the purpose 
			of computing determinant as det(P)=(-1)^S
		P: 1-d list of length n+1 representing permutation matrix and swap count
		"""
		
		if n!= len(A[0]):
			raise ValueError("input is not a square matrix")

		P = [i for i in range(n+1)]  # initiate P as an identity matrix with a permutation counter with initial value = n

		for i in range(n):
			maxA = 0.0
			imax = i

			for k in range(i, n):  # determine index of max value per column in A
				absA = abs(A[k][i])
				if absA > maxA:
					maxA = absA
					imax = k

			if imax != i:  # if max is not in diagonal, swap
				# swap P
				j = P[i]
				P[i] = P[imax]
				P[imax] = j
				# swap rows of A
				row = A[i]
				A[i] = A[imax]
				A[imax] = row
				# count swaps
				P[n]+=1

			for j in range(i+1, n):  # forward substitution for A=(L-E)+U so that P*A=L*U
				A[j][i] /= A[i][i]

				for k in range(i+1, n):
					A[j][k] -= A[j][i] * A[i][k]

		return A, P
```