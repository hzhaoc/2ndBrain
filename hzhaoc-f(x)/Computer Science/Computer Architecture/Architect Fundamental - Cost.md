# Trends in Cost
- *learning-curve* drives down manufacturing cost by time even without technology improvement. Technology iteration.
- If demand & supply are balanced, and there's sufficient market competition, price & cost track closely.
- economic scaling.
- commodity business in PC compete and gain manufacturing efficiency with scaling at very limited profit. 
- DRAM, SSD, monitors, etc are pretty standardized and thus commoditized; processors vary. Thus integrated circuits cost are important among peers for computers.

# Cost of an [[Integrated Circuit]]
basic process of silicon manufacture is unchanged: a wafer is tested and chopped into dies that are packaged. Cost of an packaged IC is:
- $$Cost\ of \ IR \ = \ \frac{Cost\ of\ die \ + \ Cost \ of \ testing \ die \ + \ Cost \ of \ packaging \ and \ final \ test }{final \ test \ yield}$$

- $$Cost \ of \ die = \ \frac{cost \ of \ wafer}{dies \ per \ wafer \ X \ die \ yield}$$

- $$$dies \ per \ wafer \ = \ \frac{\pi*(wafer \ diameter/2)^2}{die \ area}-\frac{\pi * wafer \ diameter}{\sqrt{x*die \ area}}$$

In the third formula, first term is ratio of wafer area to die area, second compensates for "square peg in a round hole" approximately.

- $$Die \ yield \ = \ wafer \ yeild \ * 1/(1+\ defects \ per \ unit \ area * die \ area)^N$$

This is Bose-Einstein empirical model. N is a manufacturing process complexity. 

## just some facts
- DRAMs include redundant memory cells for fault-tolerant -> higher manufacturing yield, lower cost.
- TSMC 2020 300mm wafer at 5nm at ~ $17K cost.
- I/O pins plus functions determine die size.
- testing add prior cost by 50%!
- for low volume IR manufacturing, [[Photomask]] can be a non-negligible cost.
