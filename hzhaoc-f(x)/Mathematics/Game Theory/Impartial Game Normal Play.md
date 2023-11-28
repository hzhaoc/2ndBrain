$$g(x) = mex\{g(x_1), g(x_2), g(x_3), ..., g(x_k)\}$$
where `x` is current state of the game, `x1, x2, ..., xk` are next possible states. `g` is grundy value. `g!=0` means winning hand for current player.
`mex` is minimum excludant / minimum non-negative exclusive integer.

$$g(sub_1, sub_2, ..., sub_k) = g(sub_1) \oplus g(sub_2) \oplus g(sub_3) \oplus ... \oplus g(sub_k)$$
where $\oplus$ is logical XOR. $sub_i$ is sub game of the current game.