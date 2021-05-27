## Bitcoin
[Bitcoin scalability problem](https://en.wikipedia.org/wiki/Bitcoin_scalability_problem)
on-chain transaction processing capacity is limited by
- average block creation time of 10 minutes
- he block size limit of 1 megabyte

Bitcoin [[Consensus Protocol]] is PoW. average bitcoin TPS is **3.3-7 **

## Ethereum
ETH [[Consensus Protocol]] is PoW and is moving to PoS. TPS is ~13 currently, after rollup it'll be ~5000, after phase 1, it may be max 10,000

## Cardano
PoS TPS is usually a few hundred TPS. ADA's scalability solution is UTxO model and smart contract infrastructure of the first layer, and "side-chain" or second layer or heads called **Hydra**. 

Hydra is the second layer solution on top of the Cardano first layer where PoS consensus is used. Hydra is designed in a way that fits well with a stake pool model. The IOHK team introduced an extended UTxO model that allows sharding of stake space without the need to shard ledger itself. It is still possible to shard on the ledger level and Hydra is a complementary part of the whole scaling solution. Every pool can create a new Hydra’s head so adding more pools mean that more head can be added. So by adding new heads to the protocol nearly linear scaling can be achieved. Simulations have been done and the results are great. Each Hydra head can process around 1000 TPS and there is room for further optimization. So with 1000 pools, Cardano could be theoretically able to scale up to 1 million TPS and the finality of transactions will be very fast.

### **What is the relationship between blockchain and Hydra**?

The **first layer** options will always be limited in terms of the number of transactions processed in a given period of time. If decentralization is not to be sacrificed, throughput will never be sufficient to allow a large number of people to use a consensual distributed network. The solution may be to create a **second layer** above the first layer. The first layer is what we call **blockchain**. It is the most secure and decentralized network with lower throughput. Above this first layer, it is possible to create a quasi-independent network, a second layer. The second layer is built to scale as high as possible and make transactions fast and cheap. So Hydra is the second layer solution for Cardano’s first layer.

Because the security of the first layer is ensured by blockchain and distributed consensus, we say that transactions are processed **on-chain**. Users will be able to transfer funds to the second layer. Transactions in the second layer are thus processed **off-chain**, meaning outside the blockchain. So the first layer does not verify transactions that take place in the second layer.

Let’s show it by example. Alice, Bob, and Carol each have 10 ADA coins in the blockchain, in the first layer. Altogether 30 coins. There is a special mechanism that allows transferring of coins into the second layer. In our case, into Hydra. To be more precise, the **Hydra’s head is opened**. In the Hydra’s head, all participants exchange coins through transactions. The first layer does not verify these transactions. Once Hydra’s head is closed, the blockchain will only take over the last valid coin distribution from the second layer. We will discuss the transferring of coins between layers later.

Blockchain can easily verify that from the Hydra’s head expected 30 ADA coins are returned back to the blockchain. So exactly the same amount that was transferred to blockchain during opening Hydra’s head. Coin ownership may have changed in the second layer, with Alice now having 20 coins and Bob with Carol 5 coins. The advantage is that a large number of fast transactions between many users can take place in the second layer and the blockchain does not have to worry about it directly.

![[Cardano 2nd layer Hydra for scalability.png]]

Alice, Bob, and Carol can communicate with each other directly in the Hydra’s head. It happens in a way that it is possible to forget the history of transactions. Parties update each other about local states and once it is confirmed among all of them the transaction history can be deleted. Only the last valid state is maintained in Hydra’s head and used when funds are to be transferred back to the blockchain. We will also discuss it in more detail later.

#### Hydra's state channels
Hydra uses **state channels**, that extends the concept of **payment channels**. Parties maintain state channels to keep **common state** and they are able to agree on it without interaction with the blockchain.

Hydra is not only about **transferring funds, but also about the execution of smart contracts**. It is necessary to work with **states**. For example, it is possible to create a smart contract in the first layer and transfer it into the Hydra’s head where can be executed.

You can imagine a smart contract as **a program or sequence of certain operations that are executed conditionally**. This means that an operation is only performed if an expected event has occurred. If not, another operation may be performed. We can talk about the event-driven execution of a smart contract. The smart contract is in a certain state at any moment, which gradually changes conditionally as long as it is active and the events trigger the changes.

Imagine a betting office where people can bet on the outcome of matches. The smart contract will be able to lock the deposits of all participants and then fairly distribute winnings based on the results of the matches. If we simplify it, the contract will be in several states per match.

1.  Collecting deposits and tips of participants before a match.
2.  Stop accepting deposits shortly before the match begins.
3.  Waiting for the match result.
4.  Processing the match result and calculating winnings.
5.  Distribution of winnings among winners.

The smart contract can be executed in Hydra and can be used for more matches in a row. Thus, blockchain cannot store all transactions related to bettings. History can be forgotten in Hydra. After the winnings are distributed to winners after the match, all states and transactions can be deleted. Except for the final state, of course. Let’s assume that the smart contract was created for a football season. Once the season ends, the Hydra’s head can be closed and all that will be stored in the blockchain is the final fund's distribution of bettors.

The concept of state channels is not new and there already are some existing implementations. However, they have some **serious disadvantages**. The biggest disadvantage is that the first layer infrastructure and smart contract code, that is written for the first layer infrastructure, **cannot be used within the second layer without changes**. These changes, that are needed for the transfer of funds and smart contracts between layers, might be very **dangerous**.

For example, the blockchain usually uses the **UTxO** model (Unspent Transaction Output). UTxO is basically an **abstraction of coins**. Each UTxO represents a chain of ownership implemented as a chain of digital signatures where the owner uses Private Key to sign a transaction that transfers ownership of their UTXO to the receiver’s Public Key. As we said, for simplicity, you can imagine UTxO as a representation of coin. Your coin holdings are defined by the number of UTxO you have in your wallet sitting on your addresses.

UTxO model is considered as a **very secure** way how to manipulate with funds within the blockchain. **Current second-layer solutions are not able to work directly with UTxO. Coins are thus represented in a completely different way. The current second layers thus lose an important security element. The same is true for executing smart contracts where a conversion of information representation must occur. And it can be very dangerous.**

Hydra **significantly simplifies** the second layer solutions. Hydra is able to adopt the first layer solution. **Extended-UTxO** **model and the whole smart contract infrastructure of the first layer can be used within Hydra**. Hydra’s transactions work directly with UTxO to change ownership. A smart contract, that is deployed in the blockchain, can be executed as-is in Hydra’s head and there is no data conversion.

To see the difference more clearly, we can have a look at Ethereum. Ethereum uses Solidity for writing a smart contract in the first layer. When the contract is to be transferred to the second layer it must be converted since the second layer is not able to work directly with Solidity. To allow the conversion the Solidity smart contract itself must be adapted. The scripting language of blockchain and the second layer **differ significantly**. So the conversion is necessary.

In Hydra, no conversion is needed since **both layers are able to use the same scripting system**. Hydra introduces **isomorphic multi-party state channels**. It basically means that the scripting language of the underlying ledger is used by state channels. Hydra inherits the scripting language from Cardano blockchain.

State channels allow **parallel processing** of transactions and smart contracts, that happens **off-chain**. It is possible to open more Hydra’s head. So Hydra can be **multi-headed**. Every newly opened head represents a new parallel unit. Once a state channel is closed, the head state can be seamlessly absorbed by the blockchain. It is an easy and straightforward task since the same smart contract code is used on-chain and off-chain. It is even possible to create a smart contract in Hydra without registration in the blockchain. Blockchain is able to take over the smart contract and continue with execution on-chain.

![[cardano hydra multiheads.png]]

Thanks to Hydra, Cardano can scale nearly linearly. It means that when new resources are added into the network then more transactions and smart contracts can be processed. Performance increases. It is not always the case for blockchain. At least, it is not so easy.

#### Extended UTxO
Using the UTxO model in both layers is not for free and **both layers must be prepared for it**. Using isomorphic state channels require the ability to take a part of the blockchain state, process it independently outside in the Hydra, and finally be able to merge it back into the blockchain. UTxO is well suited for that and can represent the on-chain and the off-chain state. However, **the traditional Bitcoin’s UTxO model is difficult to use for off-chain processing** because of its limited scripting capabilities. IOHK introduced an **Extended UTxO** (EUTxO) model and support for a general **state machine** (we will discuss it later). The Extended UTxO model and the state machine allows a secure transfer between layers without scripting restrictions.

Transfer of UTxOs from the blockchain into Hydra’s head is coordinated by multiple parties. We talk about the opening of Hydra’s head. **Head** itself is the name of the **second-layer protocol**. In the beginning, after the transfer, there is an **initial head state**, that evolves in the Head protocol independently of the blockchain. Parties send transactions, execute smart contracts, and collectively maintain the **common state**. Due to the isomorphic nature, the same transaction validation, rules, and script execution can be used on-chain and off-chain.

Any party might wish to terminate the off-chain Head protocol. In this case, parties transfer the **final head’s state** back into the blockchain. Thus, the blockchain state is updated accordingly and is consistent with the final head’s state.

Hydra enables **incremental commits and decommits**. It means that UTxO can be added to or removed from Hydra’s head without closing and reopening the Head. It is very handy since there might be more parties involved and it would be unnecessary overhead to close the Head just because one participant needs to add or remove funds.

#### State machine
You might not be familiar with the term **state machine**. Put it simply, it is a mathematical model of computation. It is an abstract machine that can be in exactly **one of a finite number of states** at any given time. The state machine can change from one state to another in **response to some inputs.** The change from one state to another is called a **transition**. It is used within the Cardano first layer to be absolutely sure that the transfer of UTxO between layers is reliable and secure as there is only one valid state at every moment and transition to the next state is deterministic.

The blockchain part of Hydra must ensure two things:

1.  It takes care of the locking of UTxOs in the blockchain as the UTxOs are transferred to the Head. The UTx0s stay locked in the blockchain while the Head is active. It happens when the Head is to be opened.
2.  When the Head is to be closed, it facilitates the settlement of the final Hydra’s state. It ensures that UTxOs are securely transferred back to the blockchain and decommited. It happens when the Head is to be closed.

![[cardano hydra state machine.png]]

There are **four states** used within Hydra’s state machine: **Initial**, **Open**, **Closed**, and **Final** and we will have a closer look at it right below**.**

It is probably unnecessary to deal with the state machine more deeply. It is important to know that the transfer of UTxO between layers is strictly and securely defined. A particular UTxO can be handled either by blockchain or by Hydra’s head.** Never by both layers simultaneously.**

#### Summary

Hydra will enable what is absolutely necessary for further adoption of cryptocurrencies, and that is high scalability. Without this feature, the global system is basically unusable, because once people want to start using it, they will find it has to wait a long time for a transaction settlement. And often also pay extra. Hydra is a gamechanger. In addition to sending transactions, it also enables the execution of smart contracts. Moreover, everything is very safe compared to the competition thanks to the direct use of UTxO.
