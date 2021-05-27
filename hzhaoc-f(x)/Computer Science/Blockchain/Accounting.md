## Bitcoin: UTxO
In a UTXO model, the movement of assets is recorded in the form of a **directed acyclic graph** where the nodes are transactions and the edges are transaction outputs, where each additional transaction consumes some of the UTXOs and adds new ones. The users' wallets keep track of a list of unspent outputs associated with all addresses owned by the user, and calculate the users’ balance.

By checking and tracking the size, age, and amount of UTXOs being transferred around, one can extract accurate metrics about the blockchain’s usage and financial activity of the chain.

UTXO models offer other advantages. Better scalability and privacy, for example. Also, the transaction logic is simplified, as each UTXO can only be consumed once and as a whole, which makes transaction verification much simpler.

## Ethereum: Account/Balance
Account/Balance chains operate in a similar fashion to traditional bank accounts. The wallet's balance increases when coins are deposited, and decreases when coins are transferred elsewhere. The crucial difference here is that, unlike UTXOs, you can use your balance partially.
## Cardano Extended UTxO
https://cardanoupdates.com/docs/c0534b27-4545-4cc1-968b-22029ced0dd7
Settlement Layer/Main-chain: UTxO = value, validator script
Computing Layer/side-chain: Account model/Plutus Core expression. 