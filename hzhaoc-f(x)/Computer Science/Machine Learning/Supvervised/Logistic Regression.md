# Hypothesis: Sigmoid / Logistic Regression
$$h_\theta(X)=g(\theta^TX)=\frac{1}{1+e^{-\theta^TX}}=\frac{1}{1+e^{-z}}=P(y=1|x)$$
where
$$z=\theta^TX$$
![[sigmoid.png]]

# Cost Function
$$J(\theta)=\frac{1}{m}\sum_{i=1}^{m}Cost(h_\theta(X^{(i)}), y^{(i)})$$
$$J(\theta)=-\frac{1}{m}\sum_{i=1}^{m}[y^{(i)} * log(h_\theta(X^{(i)})) + (1-y^{(i)}) * log(1-h_\theta(X^{(i)}))]$$
## Proof with MLE (maximum likelihood estimation)
According to likelihood:
$$L(\theta)=\prod_{i=1}^{m}P(y^{(i)}|X^{(i)})$$
obviously (see [[Bernoulli Distribution]])
$$L(\theta)=\prod_{i=1}^{m}[h_{\theta}(X^{(i)})^{y^{(i)}}(1-h_{\theta}(X^{(i)}))^{1-y^{(i)}}]$$
log both sides:
$$l(\theta)=\sum_{i=1}^{m}[y^{(i)}*log(h_{\theta}(X^{(i)})) + (1-y^{(i)})*log(1-h_{\theta}(X^{(i)}))]$$
total cost is to maximize $$l(\theta)$$
or to minimize $$J(\theta)=-\frac{1}{m}l(\theta)$$
done

## Gradient Descent
if negative log-likelihood is: (just a different form from above $J(\theta)$)
$$NLL\left (D, \mathbf{w} \right ) = -\sum_{i=1}^{N} \left [ \left ( 1 - y_i \right ) \log(1-\sigma(\mathbf{w}^T\mathbf{x}_i)) + y_i\log \sigma(\mathbf{w}^T\mathbf{x}_i)  \right ]$$

gradient descent process is 
$$\mathbf{w_t} = \mathbf{w_{t-1}} - \eta\frac{\mathrm{d}NLL(D, \mathbf{w})}{\mathrm{d}\mathbf{w}}$$

gradient is 
$$\eta\frac{\mathrm{d}NLL(D, \mathbf{w})}{\mathrm{d}\mathbf{w}}$$
where 
$\eta$ is the learning rate

then $\forall\mathbf{w}_j \in [1, 2, ..., m]$:
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= -\frac{\partial\sum_{i=1}^{n}[(1-y_i)log(1-\sigma(\mathbf{W}^TX_i)) + y_ilog\sigma(\mathbf{W}^TX_i)]}{\partial\mathbf{W}_j}$$
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= -\sum_{i=1}^{n}[(y_i)\frac{1}{\sigma(\mathbf{W}^TX_i)}\frac{\partial\sigma(\mathbf{W}^TX_i)}{\partial\mathbf{W_j}} - (1-y_i)\frac{1}{1-\sigma(\mathbf{W}^TX_i)}\frac{\partial\sigma(\mathbf{W}^TX_i)}{\partial\mathbf{W_j}}]$$
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= -\sum_{i=1}^{n}[(y_i)\frac{1}{\sigma(\mathbf{W}^TX_i)} - (1-y_i)\frac{1}{1-\sigma(\mathbf{W}^TX_i)}]\frac{\partial\sigma(\mathbf{W}^TX_i)}{\partial\mathbf{W_j}}$$
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= -\sum_{i=1}^{n}[(y_i)\frac{1}{\sigma(\mathbf{W}^TX_i)} - (1-y_i)\frac{1}{1-\sigma(\mathbf{W}^TX_i)}]\sigma(\mathbf{W}^TX_i)(1-\sigma(\mathbf{W}^TX_i))\frac{\partial\mathbf{W}^TX}{\partial\mathbf{W_j}}$$
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= -\sum_{i=1}^{n}[(y_i)(1-\sigma(\mathbf{W}^TX_i)) - (1-y_i)(\sigma(\mathbf{W}^TX_i))]X_i^j$$
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= -\sum_{i=1}^{n}[y_i - \sigma(\mathbf{W}^TX_i)]X_i^j$$
$$\frac{\partial NLL(D, \mathbf{W})}{\partial\mathbf{W}_j}= \sum_{i=1}^{n}[\sigma(\mathbf{W}^TX_i) - y_i]X_i^j$$
where 
$X_i^j$ denotes $j$th feature of the $i$th patient training vector, $\mathbf{W}$ is coefficient vector.

### Stochastic Gradient Descent (SGD)
update $\mathbf{w_t}$ based on a single pair of $X, y$ , SGD is:
$$\mathbf{w_{t}} = \mathbf{w_{t-1}} - \eta(\sigma(\mathbf{w}^T\mathbf{x}_t) - y_t)\mathbf{x}_t$$

with L2 [[Norm]] regularization ($J= NLL + \mu\Vert{\mathbf{W}}\Vert_2^2$), SGD is:
$$\mathbf{w_{t}} = (1-2\eta\mu)\mathbf{w_{t-1}} - \eta(\sigma(\mathbf{w}^T\mathbf{x}_t) - y_t)\mathbf{x}_t$$