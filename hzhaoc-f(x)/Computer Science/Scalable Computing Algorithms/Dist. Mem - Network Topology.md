some definitions or properties of a network...
- **links**: number of node connections
- **diameter**: longest shortest path
	- the lower the better, the less delay
- **bisection width**: minimum number of edge/link cuts to cut network/graph in half
	- the higher, the better bandwidth, the less congestion

> improve diameter: 
> - linear -> ring
> - mesh -> torus
> -  ...

some types of network... (assume p nodes)
- linear
- ring
- mesh
- torus
- tree
- d-dimensional mesh or torus
	-	**many supercomputers (2021) use low dimensional meshes**
-	hyper cubes: logp dimensional torus
	-	high cost of wire, but high bisection width in return

Network Type | Links | Diameter | Bisection
------------ | ------------ | ------------ | ----------
Linear | p-1 | p-1 | 1
2-D Mesh | 2p | $2\sqrt{p}$ | $\sqrt{p}$
Fully Connected | $p(p-1)/2$ | 1 | $p^2/4$
Binary Tree | P | log(p) | 1
D-Dimensional Mesh | dP | $\frac{1}{2}dP^{1/d}$ | $2P^{(d-1)/d}$
Hypercube | plogp | logp | p/2

##### congestion concept
to  map a logical topological network to a physical one...
consider congestion:
- **congestion = maximum number of logical edges that map to a physical edge**

**lower bound of a congestion C = logical bisection / physical bisection**. If you know the congestion. you’ll know how much worse the cost of your algorithm will be on a physical network with a lower bisection capacity.