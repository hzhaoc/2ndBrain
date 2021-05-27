## The DeFi Perspective

The decentralized finance perspective requires some in-depth research into the stablecoin and DEX landscape as a whole, so while this section may be lengthy, bare with me. It is important to build a foundation understanding of the space to better understand Ergo's unique position in DeFi.

We break this section into 2 main pillars:

1.  StableCoins & the AgeUSD Protocol
2.  Decentralized Exchanges & Automated Market Makers

![](https://thecryptodrip.com/content/images/2021/04/Screenshot_2021-04-14-Earn-up-to-8--on-DAI--PAX--USDC--Compounding-Daily-and-Secured-by-Custodial-Insurance.png)

### StableCoins

Perhaps surprisingly, the introduction of [stablecoins](https://www.investopedia.com/terms/s/stablecoin.asp) into crypto brought a modicum of distrust in investor sentiment, which largely influenced its sidelining during the [2017 ICO boom](https://www.gemini.com/cryptopedia/initial-coin-offering-explained-ethereum-ico).

Speculators and investors alike cycled out of [altcoins](https://thecryptodrip.com/tag/altcoins) and into Ethereum, Bitcoin and cash, some never to return again. As [regulations](https://www.forbes.com/sites/vipinbharathan/2020/12/20/stable-coin-regulation-with-a-focus-on-the-stableact/?sh=6d6794d33e5a) and sentiment shifted in favor toward the big stablecoin protocols like Tether (formerly RealCoin) and USDC, the option to sell your profits into a stablecoin and earn a yield became useful.

It's my prediction that this current bull-run will not see the exodus to cash much like we did in 2017 but a shift to stay within the crypto ecosystem via stablecoins.  
  
As it stands, the current stablecoin environment is broken into 4 pillars:

1.  Off-chain-collateralized
2.  On-chain-collateralized
3.  Un-collateralized
4.  Hybrid

To be understand the nuances, its helpful to get some real-world examples of each:

#### Off-Chain Collateralized

Tether ($USDT) is an example an off-chain collateralized stablecoin as it is pegged to the dollar deposited in central banks.

The un-collateralized algorithmic stablecoin narrative is building momentum as its counterparts have notable flaws. Off-chain fiat collateralized stablecoins are counter-intuitive to the ethos that underpins the crypto industry, yet they currently dominate.

They are also subject to centralization, counter-party risks, and regulatory constraints which was tangibly evident in the latest round of [regulation bouts between the SEC](https://medium.com/coinmonks/tether-settles-with-sec-john-mcafee-indicted-for-crypto-pump-17066483266b) and Tether.

#### On-Chain Collateralized

MakerDAO ($DAI) is an example of an on-chain-collateralized stablecoin as it is backed by deposits of other cryptocurrencies.

![](https://thecryptodrip.com/content/images/2021/04/Screenshot_2021-04-14-MakerDAO-What-Doesn-t-Kill-It--Makes-It-Stronger.png)

On-chain-collateralized stablecoins also have major flaws which stem from the volatility of the crypto markets. This volatility can cause events much like [Black Thursday](https://medium.com/@whiterabbit_hq/black-thursday-for-makerdao-8-32-million-was-liquidated-for-0-dai-36b83cac56b6), a massive liquidation event in the MakerDAO protocol due to the black swan liquidity crisis caused by Covid-19.

Absolutely colossal amounts of ETH were liquidated from MakerDAO vaults with ZERO auction-bids (_i.e._ free ETH due to network congestion), oracle price discrepancy, and the sharp Ethereum sell-off. The amount of ETH gamed from MakerDAO from ‘keepers’ who took advantage of the volatility in a non-competitive auction is equal to $130 million dollars with today's current ETH prices.

Uncollateralized stablecoins are typically smart contracts on the blockchain and therefore require an oracle to feed data to the smart contract to govern the algorithms, which leaves them open to manipulation.

#### Un-collateralized

NuBits ($NBT) is an example of an un-collateralized stablecoin as its price is stabilized via [algorithms](https://insights.deribit.com/market-research/stability-elasticity-and-reflexivity-a-deep-dive-into-algorithmic-stablecoins/) that respond to price volatility.

In the interest of brevity, let's simply say these are mainly experimental.

#### Hybrid

[AgeUSD protocol](https://github.com/Emurgo/age-usd) is an example of a hybrid stablecoin that is algorithmically stabilized _and_ collateralized on-chain (_i.e._ crypto-backed).

But, before we discover how the novel AgeUSD protocol works I would like to preface that AgeUSD is not a solution to all the above problems. But, using sound mathematics instead of dynamic transaction handling, AgeUSD aims to provide a higher assurance alternative than existing counterparts.

With that said, we believe it's a serious contender in the pursuit of true stablecoins in the cryptocurrency space. Because of that, we look deeper into what it has to offer and why its uniquely positioned to work well on the Ergo blockchain.
