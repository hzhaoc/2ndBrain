# I. Classical
## 1. K-means
Complexity: $O(mKnt)$ 
where 
m: data dimension
K: cluster #
n: number of data
t: number of iterations

## 2. Hierarchical clustering
Two methods:
- Agglomerative (bottom-up), usually more efficient
- Divisive (top-down)

## 3. Gaussian mixture model
### PDF
Model assumes vector variable $X$ follows $K$ interdependent multivariate Gaussian distributions. PDF is as follows:
$$p(x)=\sum_{k=1}^{K}\pi_{k}N(x|\mu_{k},\Sigma_{k})$$
where
$\pi_k$ is the weight for the $k_{th}$ probability of $x$ and $\sum_{k=1}^{K}\pi_k=1$

### EM (parameters convergence process)
#### Step 0: Initialize $\pi_k$, $\mu_k$, $\Sigma_k$
*(recommended)*
$\mu_k$ = $\mu_k$ = $(\mu_{k,1},\mu_{k,2},...,\mu_{k,m})$ ($(1,2,..m)$ is for dimensions of data $X$) from K-means results.

$\Sigma_k$=covariance of $X_k$ from same K-means results. (See [[Gaussian Distribution]] for detail)

$\pi_k$=$\frac{sizeof(k)}{n}$ where $n$ is total number of training data $X$

#### Step 1: E 
Assign each point $X_i$ a score $\gamma_{ik}$ for each cluster $k$:
$$\gamma_{ik}=\frac{\pi_k\mathcal{N}(x_i|\mu_k,\Sigma_k)}{\sum_{j=1}^{K}\pi_j\mathcal{N}(x_i|\mu_j,\Sigma_j)}$$
The denominator here is to normalize this score to $[0,1]$. Obviously $\sum_j^K\gamma_{ij}=1$, and $\sum_i^n\sum_j^k\gamma_{ij}=n$, $\forall{i}\in{[1,n]}$, where $n$ is total number of $X$.

#### Step 2: M
Update $\pi_k$, $\mu_k$, $\Sigma_k$, using $\gamma_{ik}$ for each cluster $k$:
- $\mathcal{N}_k=\sum_i^n\gamma_{ik}$, $n$ is total number of $X$, intuitively this is the 'size' of cluster $k$
- $\mu_k=\frac{\sum_i^n\gamma_{ik}X_i}{\mathcal{N}_k}$, intuitively this is the new center of cluster $k$.
- $\Sigma_k=\frac{\sum_i^n\gamma_{ik}(X_i-\mu_k)^T(X_i-\mu_k)}{\mathcal{N}_k}$, intuitively this is score-weighted covariance matrix $\Sigma_k$ from all $X$ for cluster $k$.
- $\pi_k=\frac{\mathcal{N}_k}{n}$, intuitively this is the portion of $X$ that belongs to cluster $k$.

#### Step 3: Check convergence. 
If not convergent, go back to **Step 1**.

#### Step 4: Return
End.

### GMM vs. K-means
|     						| K-means     | GMM     |
| :------------- | :----------:	| -----------: |
|  Clustering	  | hard   			| soft    |
| params   		   | $\mu_k$ 	| $\pi_k$, $\mu_k$, $\Sigma_k$|
| algo   			  | EM 				| EM      |

# II. Scalable

## 1. Mini batch k-means
### params
k: # of cluster centers
t: # of iterations
b: batch size
d: dimensionality of data

### steps
1.	Initialize K centers as C
2.	Iterate t times
	1.	Sample b data points as a batch M
	2.	assign points in M to the closest center in C
	```
	for each point x in M:
		d[x] = closest cneter in C to x
	```
	4.	update C based on assignments in M
		1. cache center from `d[x]` for each point x in M
		2. increment center count: `v[c]+=1`
		3. set step size $\eta=\frac{1}{v[c]}$
		4. update center $c=(1-\eta)c+\eta*x$, intuitively it moves old center towards the data point by some step size.
		Note as center count in step 2 increases, step size is becoming smaller and smaller, eventually the center update in 4. will be stablized.
### complexity
$O(dKbt)$
where params as denoted as above.
		
## 2. DBScan (graph algorithm)
Density-Based Spatial Clustering of Applications with Noise. Main intuition is to define clusters as areas of high density separated by areas of low density. 
Clusters found by DBScan can be any shape.
![[dbscan.png]]

### key concepts
- density
density at point p = # of points within a certain distance **d** to p

- point p in dense region or not
point p in dense region = Density at point p $\geq$ some threshold value

- Core
points in dense region

- border
points with exactly distance **d** to a core point

- noise
points outside **d** to all core points

### steps
1. for each core point c, create edges to points with d radius (create the graph) ![[dbscan_step1.png]]
2. N: all nodes in the graph (all data X)
3. there exists core points in N?:
	1. False: **done** (exit)
	2. True:
		1. Pick a random core point c in N ![[dbscan_randompick.png]]
			1. find all connected component X from c
			2. update nodes N by **removing all points in X**. ![[dbscan_stepremove.png]]
4. go back to 3. 

## 3. Power Iteration Clustering (PIC)
[Spark PIC Doc](http://spark.apache.org/docs/2.3.0/mllib-clustering.html#power-iteration-clustering-pic)

# Clustering evaluation metrics
## 0. Purity (to be added)
- [R code document](https://www.rdocumentation.org/packages/NMF/versions/0.20.6/topics/purity)
- [Formula](https://stats.stackexchange.com/questions/95731/how-to-calculate-purity)
## 1. rand index
![[clustering_randindex.png]]
## 2. [[Informatics|Mutual Information]]
![[mutualinformation.png]]
## 3. silhouette coefficient
This metric doesn't require ground truth that rand index and mutual information do.
![[silhouette coefficient.png]]
Coefficients is between -1 and 1. -1 means worse, 1 means best, 0 means **overlapping cluster**. Intuitively the larger the coefficient, the better the clustering. 

## 4. Jaccard coefficient
Evaluate similarities between two sets.
[Wikipedia](https://en.wikipedia.org/wiki/Jaccard_index)

## Reference
[Evaluation of clustering](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html)
### limitation
-	assume **spherical clusters**