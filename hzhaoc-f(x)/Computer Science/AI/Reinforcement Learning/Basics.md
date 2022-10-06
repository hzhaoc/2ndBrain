S### what does RL do
- *action* affect *state*, state in return thru a policy gets mapped into new action for next step...
- **policy** can be model-based or model-free?
- policy gets updated thru feedback (or learns from errors) and aims to choose best action that maximizes benefits for its serving agent for each state it faces.

### concepts
- policy: a mechanism that maps a given state to "best" possible action to take (best is usually based on reward)
- **reward**: immediate reward an agent receives for choosing an action (i.e., reward at current step)
- **value**: "long-term" benefit of an agent receives for choosing an action and following actions based upon
- **value-based**: given a state, chooses best action that maximizes value
- $Q(a^*) = \sum_{r}p(r|a)r$
	- value of action $a^*$ is expected reward which is sum of each reward times its probability for each future action
- **episode**: each episode start is independent of any other episode end. end of episode is end of agent-environment interaction.
- **meta-RL**: train a reward function at individual level - those who have good reward mechanism pass down it.
- **Markov Decision Process (MDP)**: stochastic process where future state depends only on current state, not past state.
- State-value: value given a state, under a policy
- Action-value: value given a state, then action, under a policy

### sample-method 
value of one action is estimated at historical sample rewards' average for that action
$Q_{n+1}=\frac{1}{n}\sum_{i=1}^{n}R_i=Q_n+\frac{1}{n}(R_n-Q_n)$ (incremental update)
- $\frac{1}{n}$ here can be step size in other methods

### exploitation vs exploration
- acting on explored data is exploitation
- acting to explore new data is exploration
- needs balance. such as epsilon-greedy:
	- $argmax Q_t(a), \ probability \ 1-\epsilon$
	- random draw from action space

### initial optimistic value
a high initial optimistic value makes an agent explore more **at start**

### discounted value/return
$$G_t = R_{t+1}+\gamma R_{t+2}+...$$
    $$ G_t = R_{t+1} + \gamma G_{t+1}$$
    note: $\sum_{k=1}^{n}{\gamma^k}$ is capped at $\frac{1}{1-y}$


### policy
- deterministic policy
$$\pi(s)=a$$
- stochastic policy
$$\sum_{a}\pi(a|s)=1$$
$\pi$ stands for a specific policy

### value functions
- return 
$$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$$
R as variable stands for reward at some future time. $r$ as constant stands for reward for a particular state.

- state-value
$$v_{\pi}(s)=E_{\pi}[G_t|S_t=s]$$
$$=$$
expected return for a given state is its state-value

- action-value
$$q_{\pi}(s,a)=E_{\pi}[G_t|S_t=s,\ A_t=a]$$
expected return for a given state and action is its action-value

