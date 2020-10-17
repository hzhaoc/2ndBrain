# Inspiration
From human brains of neural nets:
![[brain_neurons.png]]

# Structure
A basic structure of neural network is 1 input layer, 1 hidden layer, and 1 output layer. For each arrow in the below illustration example, it's a [[Logistic Regression]]; each activation neuron is an binary output from each logistic regression.
![[neural_network.png]]

# Forward Propagation
In the above example, each layer of activation neurons (input can be viewed as the $0_{th}$ layer of activation neuron) is an input to each logistic regression to output next layer of neurons, until the final output of binary or multiclass.

Formally, the forward propagation does the following:
$a_1^{(2)}=g(\Theta_{10}^{(1)}x_0 + \Theta_{11}^{(1)}x_1 + \Theta_{12}^{(1)}x_2 + \Theta_{13}^{(1)}x_3)$
$a_2^{(2)}=g(\Theta_{20}^{(1)}x_0 + \Theta_{21}^{(1)}x_1 + \Theta_{22}^{(1)}x_2 + \Theta_{23}^{(1)}x_3)$
$a_3^{(2)}=g(\Theta_{30}^{(1)}x_0 + \Theta_{31}^{(1)}x_1 + \Theta_{32}^{(1)}x_2 + \Theta_{33}^{(1)}x_3)$
$h_\Theta(x)=g(\Theta_{10}^{(2)}a_0^{2} + \Theta_{11}^{(2)}a_1^{2} + \Theta_{12}^{(2)}a_2^{2} + \Theta_{13}^{(2)}a_3^{2})$
where
- $a_{i}^{(j)}$ is $j_{th}$ layer $i_{th}$ activation neuron;
- $\Theta_{ij}^{(k)}$ is $k_{th}$ layer $i_{th}$ neuron $j_{th}$ coefficient, in the illustration example, $\Theta_{0j}^{(k)}$ is bias / intercept term and $x_0=0$;
- $h_\Theta(x)$ is the final output, here it's binary 0  or 1.

## FP Intuition
![[nn_fp.png]]

# Cost Function
We know each activation function in the network is a single [[Logistic Regression]] who input from last layer neurons, and output to next layer neurons. 

Formally, for a multiclass network network, total cost including L2 [[Norm]] is:
$$J(\theta)=-\frac{1}{m}\sum_{i=1}^{m}\sum_{k=1}^{K}[y_k^{(i)}log(h_\Theta(x^{(i)}))_k + (1-y_k^{(i)})log(1-log(h_\Theta(x^{(i)}))_k)] + \frac{\lambda}{2m}\sum_{l=1}^{L-1}\sum_{i=1}^{s_l}\sum_{j=1}^{s_{l+1}}(\Theta_{ji}^{(l)})^2$$
where
- $K$ is number of classes in output layer (including input and output)
- $h_\Theta(x^{(i)}))_k$ is the **whole** binary-output function on $k_{th}$ output class, for the $i_{th}$ training example. (**Not just logistic regression to output to last layer**)

# Backward Propagation
## Notation
![[neural_network2.png]]
Given above NN structure, denote, refer to [[Logistic Regression]]:
- $a^{(1)}=x$
- $z^{(2)}=\Theta^{(1)}a^{(1)}$
- $a^{(2)}=g(z(^{(2)}))$
- $z^{(3)}=\Theta^{(2)}a^{(2)}$
- $a^{(3)}=g(z(^{(3)}))$
- $z^{(4)}=\Theta^{(3)}a^{(3)}$
- $a^{(4)}=g(z(^{(4)}))=h_\Theta(x)$

## Gradient Computation
### 'Error' term
Intuition: $\delta_j^{(l)}$ is the 'error' of node $j$ in layer $l$.

For each output unit ($.*$ is element wise vector multiplication):
- $\delta_j^{(4)}=a_j^{(4)}-y_j$
- $\delta_j^{(3)}=(\Theta^{(3)})^T\delta^{(4)}.*g'(z^{(3)})$ where $g'(z^{(3)})=a^{(3)}.*(1-a^{(3)})$
- $\delta_j^{(2)}=(\Theta^{(2)})^T\delta^{(3)}.*g'(z^{(2)})$
- No $\delta_j^{(1)}$


### Gradient
Likely to prove:[^1] 
$\frac{\partial}{\partial\Theta_{ij}^{(l)}}J(\Theta)=a_j^{(l)}\partial_i^{(l+1)}$ (ignore regularization)

### Backward propagation
Set $\Delta_{ij}^{(l)}=0$ as error vectors for all layers
For $i=1$ to $m$:
- Set $a^{(1)}=x^{i}$
- Perform forward propagation to compute $a^{(l)}$ for all layers all neurons
- Perform backward propagation to compute $\partial$ for all layers all neurons
- $\Delta_{ij}^{(l)}:=\Delta_{ij}^{(l)} + a_j^{(l)}\partial_i^{(l+1)}$

Finally:
- $D_{ij}^{(l)}:=\frac{1}{m}\Delta_{ij}^{(l)} + \lambda\Theta_{ij}^{(l)}$ if $j\neq0$ (contains regularization term)
- Or $D_{ij}^{(l)}:=\frac{1}{m}\Delta_{ij}^{(l)}$  if  $j = 0$ (bias term)
- $\frac{\partial}{\partial\Theta_{ij}^{(l)}}J(\Theta)=D_{ij}^{(l)}$ <- now you have the gradient (likely to prove[^2])

## Intuition
![[nn_bp.png]]
$\delta_{j}^{(l)}$ is the 'error' of cost for $a_{j}^{(l)}$

formally:
$\delta_{j}^{(l)}=\frac{\partial}{\partial{z_{j}^{(l)}}}cost(i)=(\Theta^{(l)})^T\delta^{(l+1)}.*g'(z^{(l)})$
where
- $cost(i)=y^{(i)}log(h_\Theta(x^{(i)})) + (1-y^{(i)})log(1-log(h_\Theta(x^{(i)})))$
- $i$ is $i_{th}$ training sample

# Other activation functions
![[nn_activate_func.png]]

# Summary
The key idea of gradient descent to optimize $\Theta$ in neural network for $m$ training samples, is to **understand error term and gradient in backward propagation**



[^1]:[derivation](http://neuralnetworksanddeeplearning.com/chap2.html), [cornell CS](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://www.cs.cornell.edu/courses/cs5740/2016sp/resources/backprop.pdf), [Swarthmore](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://www.cs.swarthmore.edu/~meeden/cs81/s10/BackPropDeriv.pdf)
[^2]: Same above