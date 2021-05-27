## Cardano
Imagine a betting office where people can bet on the outcome of matches. The smart contract will be able to lock the deposits of all participants and then fairly distribute winnings based on the results of the matches. If we simplify it, the contract will be in several states per match.

1.  Collecting deposits and tips of participants before a match.
2.  Stop accepting deposits shortly before the match begins.
3.  Waiting for the match result.
4.  Processing the match result and calculating winnings.
5.  Distribution of winnings among winners.

The smart contract can be executed in Hydra and can be used for more matches in a row. Thus, blockchain cannot store all transactions related to bettings. History can be forgotten in Hydra. After the winnings are distributed to winners after the match, all states and transactions can be deleted. Except for the final state, of course. Let’s assume that the smart contract was created for a football season. Once the season ends, the Hydra’s head can be closed and all that will be stored in the blockchain is the final fund's distribution of bettors.
