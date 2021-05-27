## [Cardano/ADA](https://iohk.io/en/projects/cardano/)
### Overview
- **Scalability**
	- TPS. Check [[Scalability]] and [[Smart Contracts]]
	done through **Ouroboros protocol with UTxO coin model, smart contract infra, and 2nd layer multi-heads  "Hydra"**
	- Network/Bandwidth
		-	RINA: Recursive internetwork architecture builds **a heterogeneous network**. 
	- Data Storage: Pruning, Subscriptions, Compression, Partitioning
- **interoperability**
Internet of blockchains. Internet of values. Kingmaker is the decentralized system that enables cross-chain or chain-to-fiat-currency transfer. First, side-chain effort that verify value from some blockchain in a very *compressed* way. Second, banks look at 1. meta data that may be very sensitive personal information to put into a public blockchain. 2. attribution. 3. compliance. Cardano seeks to look at a solution to provide these from blockchain to make transactions verifiable to banks.
- **Sustainability**
	- Treasury
	When rewarding occurs to miners or stake holders, Blockchain makes part of it go into a decentralized bank account, funded through inflation. There is a **democratic method** to vote on **funding proposals** on a ballot someone submitted, such as a new scientific research, or developing state channels to Ethereum. The treasury model should be developed in modular capacity so it can be upgraded independently. 
	- Development
		- Soft fork / Hard fork
		- Cardano improvement proposal method
	Similar to Treasury method. Makes a social protocol imbedded into a blockchain mechanically like its metadata. It should be machine understandable. 

### Governance
Peer Review method in research with university involvement, formal methods in engineering development. Aims at providing high assurance code.

### [[Consensus Protocol|Consensus]]: Ouroboros
Ouroboros is the first provably secure proof-of-stake protocol, and the first blockchain protocol to be based on peer-reviewed research. Ouroboros combines unique technology and mathematically-verified mechanisms - which, in turn, combine behavioral psychology and economic philosophy - to ensure the **security** and **sustainability** of the blockchains that depend upon it. The result is a protocol with proven security guarantees able to facilitate the propagation of global, permissionless networks with **minimal energy requirements** (**scalability**) - of which Cardano is the first. <br> 
At the heart of Ouroboros is the concept of infinity. Global networks must be able to grow sustainably and ethically: to provide greater opportunities to the world while also preserving it. This becomes possible with Ouroboros. <br> 
Ouroboros facilitates the creation and fruition of distributed, permissionless networks capable of sustainably supporting new markets.<br>
Ouroboros also has very rigorous security standards in terms of theoretical foundations and implementation, which means when more capabilities are developed into the protocol, they are securely composable, whereas other systems has to prove additional capability to be secure on a case-to-case basis.<br>
Ouroboros are intended to be [quantum resistant](https://en.wikipedia.org/wiki/Post-quantum_cryptography). Work in progress?
	
- Features
	- **Provably secure**
		Ouroboros features mathematically verifiable security against attackers. The protocol is guaranteed to be secure so long as 51% of the stake – in the case of Cardano, ada – is held by honest participants, which, in addition to other novel concepts, is achieved through random leader selection. The protocol continues to evolve through new iterations and rigorous security analysis.

	- **Incentives & Rewards**
		To ensure the sustainability of the blockchain networks using Ouroboros, the protocol features an incentive mechanism that rewards network participants for their participation. This can either be operating a stake pool or delegating a stake in ada to a stake pool. Rewards (in the form of ada) can be earned by completing either of these activities.
		
	- **Stake delegation and stake pools**
		Ouroboros is a proof-of-stake protocol. It distributes network control across stake pools: node operators with the infrastructure required to ensure a consistent and reliable connection to the network. For each slot, a stake pool is assigned as the **slot leader**, and is rewarded for adding a block to the chain. Ada holders may delegate their stake to a specific stake pool, increasing its chance of being selected as the slot leader, and share in the stake pool’s rewards.
		
	- **Energy efficient**
		Ouroboros solves the greatest challenge faced by existing blockchains: the need for more and more energy to achieve consensus. Using Ouroboros, Cardano is able to securely, sustainably, and ethically scale, with up to [four million times the energy efficiency of bitcoin](https://iohk.io/en/blog/posts/2020/03/23/from-classic-to-hydra-the-implementations-of-ouroboros-explained/).
		
- How it works?
	 Ouroboros processes transaction blocks by dividing chains into epochs, which are further divided into time slots. A slot leader is elected for each time slot and is responsible for adding a block to the chain. To protect against adversarial attempts to subvert the protocol, each new slot leader is required to consider the last few blocks of the received chain as transient: only the chain that precedes a prespecified number of transient blocks is considered settled. This is also referred to as the settlement delay, and is the mechanism through which the ledger is securely passed between participants.<br>
	 Ouroboros is a meld of innovative technology and philosophy. Its research explores how we behave as a society, to discover an ideal balance - defined through game theory - between individual and collective interests. Ouroboros’ incentive mechanism rewards participants for their honest participation, and disincentivizes dishonest actors. It is a stable and sustainable foundation for permission networks that are built to endure: the infrastructures of the future.<br>
	 **slot leaders** function similarly to **miners** in [[Crypto Bitcoin|Bitcoin]] but are way computationally cheaper.  A slot leader can maintain multiple blockchains simultaneously, a consensus of a set of blockchains.  Additionally, epochs can be run in parallel, meaning the more computationally capable users, the more types of blockchains can be held among parallel epochs, allowing for scalability. 

### [Cardano’s benefits for DeFi applications](https://forum.cardano.org/t/what-will-decentralized-finance-look-like-on-cardano/45531)

Soon, through the Mary hardfork, token forging and a multi-asset ledger will be available on the Cardano blockchain. In turn, this will pave the way for decentralized applications (DApps), native tokens, and DeFi use cases.

But why might a DeFi project choose to run on Cardano, rather than one of our peer protocols? Let’s break it down to some simple areas where the Cardano blockchain could excel for DeFi projects.

##### 1\. Lower transaction fees

Although the complex topic of gas fees is outside the scope of this article, we can summarize that high gas fees have been, and continue to be, a huge issue and stumbling block for DeFi protocols. Gas fees on some protocols have become so high due to increased network demand, that users have reported paying [exorbitant fees to process a single transaction 109](https://cointelegraph.com/news/using-a-defi-protocol-now-costs-more-than-50-as-ethereum-fees-skyrocket).

Not only do rising gas fees cost the DeFi protocols themselves more when moving value and executing smart contract code, but they also present another barrier to entry for new users.

As we know, if we are to attract the biggest potential user group of decentralized finance products—those in [emerging economies 265](https://forum.cardano.org/t/how-cardano-could-fast-track-financial-inclusion-in-emerging-economies/44032)—we must ensure that we can keep costs low. Similar to paying high fees for banking services, many users who desperately need new financial infrastructure simply won’t explore DeFi solutions if the costs are too high.

On Cardano, transactions between native tokens and assets [do not incur execution fees 115](https://iohk.io/en/blog/posts/2020/12/09/native-tokens-on-cardano-core-principles-and-points-of-difference/), owing to the way they are deployed on-chain. We will discuss this in more detail below, but the bottom line is that DeFi has the potential to be much more affordable through Cardano.

##### 2\. Token and smart contract security

Tokens are an essential part of most existing DeFi protocols, used for governance, utility, or yield distribution. On other chains, such as Ethereum, tokens require smart contracts to run, and often necessitate the deployment of complex purpose-written code in the token contract.

We could say that these tokens are ‘non-native’—in other words, they are [not supported on the underlying ledger 68](https://iohk.io/en/blog/posts/2020/12/08/native-tokens-on-cardano/#:~:text=Cardano%20supports%20user%2Ddefined%20tokens,tracked%2C%20sent%20and%20received.). Tokens on Cardano, on the other hand, are ‘native’. This means that tokens representing assets on Cardano use token logic that runs directly on Cardano’s ledger, rather than using smart contracts. By removing the need for smart contracts to deploy tokens, Cardano removes the large burden of gas costs associated with interacting with a token smart contract.

Generating custom code for each token launched through a smart contract requires an extreme amount of confidence in that code. Human error is a real risk in smart contract-based tokens, despite many of these contracts being responsible for potentially billions of dollar’s worth of on-chain value. As a result, bugs in token smart contracts have already cost users millions of dollars in value over the years, with smart contract exploits happening [somewhat regularly 39](https://forum.openzeppelin.com/t/list-of-ethereum-smart-contracts-post-mortems/1191).

Instead, as [Cardano supports user-defined native tokens 68](https://iohk.io/en/blog/posts/2020/12/08/native-tokens-on-cardano/#:~:text=Cardano%20supports%20user%2Ddefined%20tokens,tracked%2C%20sent%20and%20received.), DeFi tokens could be [forged 31](https://forum.cardano.org/t/an-introduction-to-tokenization/39609)without the need for custom code. The only required custom code is a minting policy, which is [permanently hash-associated with its respective tokens 115](https://iohk.io/en/blog/posts/2020/12/09/native-tokens-on-cardano-core-principles-and-points-of-difference/), and there’s no way to change the policy.

Cardano does this while also supporting fungible and non-fungible tokens without the need for specialized contracts—paving the way to represent a whole host of real world assets on-chain securely and affordably.

If serious institutional entities are exploring launching DeFi products, then tokens which solve the inherent vulnerabilities and dangers of custom-coded smart contracts could prove very attractive.

##### 3\. Cardano community power—the ultimate DeFi Catalyst?

This section is about you.

Cardano’s community is immensely powerful. Together, we have achieved feats that other protocols have long aspired to—near full decentralization through community led stake pools, a thriving staking and delegation ecosystem, and bustling community channels.

More recently, the community helped Cardano achieve another major milestone through [Project Catalyst 227](https://iohk.io/en/blog/posts/2021/01/06/project-catalyst-blasts-off-into-2021/), one that is of critical importance to attracting DeFi developer talent and funding new solutions on Cardano.

With over 3,000 people already signed-up to vote and [US$500,000 in funding available through Fund3 227](https://iohk.io/en/blog/posts/2021/01/06/project-catalyst-blasts-off-into-2021/), Project Catalyst is one of the largest community-led funding initiatives on any blockchain to date.

By pushing power to the edges of the Cardano community, there has already been a successfully funded DeFi proposal, one of the first projects that will launch atop Cardano, and our community made it happen. Going forward, our community stands to be a driving force for development and adoption of the Cardano blockchain for all kinds of solutions.

With Mary on the horizon, we are now looking forward to seeing more ideas flourish through Catalyst, and we anticipate some of these will include more DeFi proposals.

### Native Tokens
When Cardano was in its infancy it existed as a single asset ledger, supporting only the ada digital token through the Byron value layer. With the advent of the Mary hard fork at the end of February, Cardano will instead be transitioning to a [multi-asset ledger 28](https://iohk.io/en/research/library/papers/utxoma-utxo-with-multi-asset-support/).

This will extend the current accounting infrastructure of Cardano’s ledger, growing to accommodate transactions that can use a range of assets simultaneously. We can describe these assets as ‘user-defined’ tokens, as they are built and deployed by independent developers, individuals, and teams on top of Cardano.

‘User-defined’ may be self-explanatory, but why do we refer to these assets as ‘native’ tokens? This is a result of [native tokens 40](https://iohk.io/en/blog/posts/2021/02/04/native-tokens-to-bring-new-utility-to-life-on-cardano/)’ design principles, which allow them to be deployed using the same token logic as the underlying Cardano protocol. This is somewhat different from tokens that rely on custom-code through smart contracts, such as those on Ethereum. As a result, native tokens on Cardano offer different security guarantees and functionality.

You can read more about these differences [here 94](https://forum.cardano.org/t/what-will-decentralized-finance-look-like-on-cardano/45531), but it’s important to remember that unlike a smart contract-based token where token logic and behaviors are written into a token contract, native tokens on Cardano have different native components that serve a similar purpose. Let’s explore these in more detail.

#### How can you mint new tokens on Cardano?

Creating, or ‘minting’, new tokens on Cardano currently requires familiarity with the Cardano CLI, however as we have discussed, this will change in the near future.

At the moment, you will be required to configure a relay node through the CLI to connect to the Cardano native tokens pre-production environment before you can create a native token. You can read more about working with the Cardano CLI to mint native tokens from IOHK [here 349](https://iohk.io/en/blog/posts/2021/02/18/building-native-tokens-on-cardano-for-pleasure-and-profit/). Instead, we will explore the lifecycle of native tokens below.

![](https://aws1.discourse-cdn.com/business4/uploads/cardano/optimized/3X/a/f/af2228c4a6b6559330d29838cc00bb40d8eacdb4_2_614x157.png)


To create a token, you will need to set a minting policy. In the token lifecycle diagram above, this falls under ‘Define monetary policy script’. Token minting policies, defined by the asset controllers, are a set of rules that govern how the native tokens scoped under it are managed—for example, setting token burn parameters or specifying the epoch in which token distribution should end.

Tokens may only be scoped under one minting policy. This asset or token can never change its minting policy. In this way, assets on Cardano remain immutable. A single minting policy determines the minting and burning conditions of all tokens scoped under it.

#### Transacting and transferring native tokens on Cardano

Native tokens can be transferred or sent to anyone with an ada wallet, much in the same way that ada can. Any user can send or receive native tokens.

A key difference between native tokens on Cardano and that of other blockchains is that different tokens can be ‘bundled’ and sent in a single transaction. Any tokens can be bundled together, and token bundles can be used to organize tokens into particular data structures (i.e. fungible or non-fungible). You can read more about the practical implementation of token bundles [here 10](https://developers.cardano.org/en/development-environments/native-tokens/multi-asset-tokens-explainer/).

To send a native token on Cardano, some ada must be sent alongside it to cover the transaction fee. This fee is fundamentally different from Ethereum’s gas fees, as it is not a smart contract execution fee and it is not subject to the same network congestion considerations.

Instead, the transaction fee requires a ‘min-ada-value’ which changes according to how many tokens are included in a single output. The min-ada-value increases with an increased number of different tokens included in a transaction.

Native tokens can also be ‘redeemed’, which is the process of sending the tokens back to the issuer. There is no requirement to offer compensation for redeemed tokens, and this can be specified in the minting policy. Or, tokens can be burned (destroyed forever). Burning tokens could either be part of a buy-back event or when tokens no longer serve a purpose.

#### Cardano native token vs Ethereum ERC20
https://cardano-ledger.readthedocs.io/en/latest/explanations/features.html

### Others
#### Current Developers
- Cardano Foundation
For education, regulation network, etc.
- [Input Output Hong Kong](https://iohk.io/en/) (IOHK)
For engineering, development, research.
- Emburgo
Japanese enterprise. For business network.
#### [Roadmap](https://roadmap.cardano.org/en/goguen/)
#### code
commits report: https://cardanoupdates.com/reports/