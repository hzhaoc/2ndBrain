# Cryptocurrency + smart contracts/dApps
## [EVM](https://ethereum.org/en/developers/docs/evm/) (Ethereum Virtual Machine)
> The EVM’s physical instantiation can’t be described in the same way that one might point to a cloud or an ocean wave, but it does _exist_ as one single entity maintained by thousands of connected computers running an Ethereum client.

The Ethereum protocol itself exists solely for the purpose of keeping the continuous, uninterrupted, and immutable operation of this special state machine; It's the environment in which all Ethereum accounts and smart contracts live. At any given block in the chain, Ethereum has one and only one 'canonical' state, and the EVM is what defines the rules for computing a new valid state from block to block.
## ETH 1
- Smart contract platform
- high transaction fee
## ETH 2
- base layer scaling would likely be focusing on data blocks, not on-chain computation or IO operations.
- layers 2 protocols should be built in to wallet, not webpage-like dApps. 
### [Roadmap](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698/47)  
#### All for **SCALABILITY**
#### Layer 1 gas fee stay high, layer 2 rollups/sidechains? split expensive on-chain computations from base layer and gas fee will be low, in turn likely lowering layer 1 gas fee
-   Today, Ethereum has ~15 TPS.
-   If everyone moves to layer 2 rollups, we will soon have ~3000 TPS.
-   Once phase 1 comes along and rollups move to eth2 sharded chains for their data storage, we go up to a theoretical max of ~100000 TPS.
-   Eventually, phase 2 will come along, bringing eth2 sharded chains with native computations, which give us… ~1000-5000 TPS.
-  Will probably end up before phase 2 come. 

> https://hackmd.io/@benjaminion/wnie2_210213#fnref1
> Rollups are like a turbo-charger for Ethereum’s engine, the EVM. The EVM is underpowered because it is starved of the data that is its fuel. In part this is deliberate to avoid massive state bloat. Rollups act like a turbo, compressing the fuel–air mix, the data, and forcing it under pressure into the EVM. They also take care of the state, outside the protocol.
> But rollups are completely independent of Eth2. They are in development and running on Eth1 today, and already beginning to deliver on their scalability promise.


> Some quick advantages of the new approach:
> -   Rollups allow us to decouple the move to proof of stake (the merge) from sharding, and we can deliver the merge quickly in the form of the [executable Beacon Chain](https://ethresear.ch/t/executable-beacon-chain/8271?u=benjaminion). This design allows the move to PoS to be minimally disruptive to current dapps, tooling, and users.
> -   We have a choice as to whether to deliver sharding first or the merge first, which reduces risk in case we find an issue with one of them. The overall time to deliver is shorter (but we’re delivering less).
> -   The layer 1 protocol is greatly simplified. No more worrying about cross-shard transactions and all that jazz. They are now somebody else’s problem. This is generally [a good thing](https://vitalik.ca/general/2018/08/26/layer_1.html).

> Some things that make me nervous:
> -   Rollup technology is in its infancy, and there’s no guarantee that it will work out well. In the worst case, we would probably need to bring back executable shards into Eth2.
> -  A rollup-centric world—a world in which lots of protocol type stuff is kicked out of the protocol—will be much more chaotic in the short term. However, not being part of the base layer will enable it to iterate rapidly, and market forces should eventually lead to the adoption of standards for interoperability, tooling, tracking, and so on. But in the mean time, it’s going to be a bumpy ride.
> - Cheap layer 1 transactions are probably gone for good, and Eth2 as currently planned is not going to change that. This will be surprising and disappointing news to many people.