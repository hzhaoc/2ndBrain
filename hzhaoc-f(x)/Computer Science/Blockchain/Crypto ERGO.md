## Overview
1.  Ergo will bring all the advantages of Proof of Work to users of the Cardano ecosystem.
2.  Ergo is the first blockchain to adopt smart contract language similar to the UTxO model Cardano uses, bringing compatibility with Proof of Work to a whole new level.
3.  Long-term scalability of dApps with the ability of parallelization of dApps.
4.  More advanced cryptography with sigma protocols — highly flexible and composable cryptographic signatures.
5.  The Ergo headless dApps framework.
6.  Oracle pools — layered pools of pools of oracles with deviation checking consensus opening a whole new world of applications.
7.  Local Exchange Trading System on top of Ergo.
## Mining
Linux 18.04 + GPU (AMD/Nvidia) with 6GB min RAM 
-  https://www.reddit.com/r/ergonauts/comments/lxkhcy/ergo_mining_set_up_question/
- https://ergonaut.space/en/Mining
## Consensus - PoW: Autolykos
Favors memory-hard CPU/GPU miners which store a table size of ~2G which gradually increase by time.

https://www.ergoforum.org/t/autolykos-v-2-details/480
https://www.docdroid.net/mcoitvK/ergopow-pdf

is memory-hard PoW algorithm resistant to attackers like ASIC which is compute-bound? Memory-hard PoW may be a solution. Or change Consensus algo periodically to make attackers like ASIC uncommercially

some introduction: https://thecryptodrip.com/ergo-deep-dive/

## Accounting: EUTxO

## DeFi ecosystem
#### AgeUSD protocol
AgeUSD’s hybrid model stands on the stablecoin itself (**SigmaUSD**) and the reserve coin (**SigmaRSV**). SigmaUSD is the first and only algorithmic stablecoin to run on the EUTxO model.
#### exchange/DeDex: ErgoDex
- Use EUTxO to have a match mechanism to enable low transaction fee.
- Support Atomic Swap (swap token across blockchains without using wrapped assets, gateways or trust-based bridges)
- support buyback orders to reduce risk for ICO/IDO investors
#### The Oracle Perspective
Oracle is a private company that provides Chainlink as a DeDex. ERGO partners with EMURGO to provide **oracle pool framework**, where data computed on-chain instead of side-chain like Chainlink.


## Other
#### Wrapped token
A wrapped token is a cryptocurrency token pegged to the value of another crypto. It’s called a wrapped token because the original asset is put in a wrapper, a kind of digital vault that allows the wrapped version to be created on another blockchain.
