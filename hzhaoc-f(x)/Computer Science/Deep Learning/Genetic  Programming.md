# Automatic Algorithm Design
Hua Zhao, MS in CS, GaTech

# Concept
With genetic algorithms, each new generation is created through mating/mutation of individuals in the previous population (then their fitness is evaluated). Through numerous operations of this process, it will eventually produce the best individual - one whose fitness is better than everyone else’s in the population and cannot get any better

![[gp_flow.png]]

Key words:
- Individual
- Population
- Objective
- Fitness
- Evaluate
- Selection
- Mate / Crossover
- Mutate
- Algorithms (various evolutionary algorithms)

**Individual**: one specific candidate in the population (with properties such as DNA)
  
**Population**: group of individuals whose properties will be altered

**Objective**: a value used to characterize individuals that you are trying to maximize or minimize (usually the goal is to increase objective through the evolutionary algorithm)
  
**Fitness**: relative comparison to other individuals; how well does the individual accomplish a task relative to the rest of the population?

**Evaluation**: a function that computes the objective of an individual

## Selection
   
Selection: represents ‘survival of the fittest’; gives preference to better individuals, therefore allowing them to pass on their genes

- **Fitness** Proportionate: the greater the fitness value,  
the higher the probability of being selected for mating

- **Tournament**: several tournaments among individuals  
(number of individuals in each tournament is  
dependent on tournament size); winners are selected for mating

### Tournament
#### Nondominated Sorting Genetic Algorithm II  (NSGA II)
- Population is separated into nondomination ranks
- Individuals are selected using a binary tournament
- Lower Pareto ranks beat higher Pareto ranks
- For example, an individual on the blue front will beat out an individual on the orange front
- Ties on the same front are broken by crowding distance
- Summation of normalized Euclidian distances to all points within the front
- Higher crowding distance wins
#### Strength Pareto Evolutionary Algorithm 2 (SPEA2)
- Each individual is given a strength S
- S is how many others in the population it dominates
- Each individual receives a rank R
- R is the sum of S’s of the individuals that dominate it
- Pareto individuals are nondominated and receive an R of 0
- A distance to the kth nearest neighbor (𝛔k) is calculated and a fitness of R + 1/(𝛔k + 2) is obtained

## Mate/Mutate
-  Mate/Crossover: represents mating between individuals
-  Mutate: introduces random modifications; purpose is to maintain diversity

## Algorithm
Algorithms: various evolutionary algorithms to create a solution or best individual
```
1.Randomly initialize population
2.Determine fitness of population
3.Repeat… 
	1.select parents from population
	2.perform crossover on parents creating population
	3.perform mutation of population
	4.determine fitness of population
… until best individual is good enough.
```

## Individual  representation
We can represent a program as a tree structure. The tree is converted to a **lisp preordered parse** tree.

- **Nodes** are called **primitives** and represent **functions**
- **Leaves** are called **terminals** and represent **parameters**
- The input can be thought of as a particular type of terminal.
- The output is produced at the root of the tree.
![[gp_tree.png]]

## Pareto Frontier
- An individual is Pareto if there is no other individual in the population that outperforms the individual on all objectives
- The set of all Pareto individuals is known as the Pareto frontier
- These individuals represent unique contributions
- We want to drive selection by favoring Pareto individuals
- But maintain diversity by giving all individuals some probability of mating
![[gp_pareto_frontier.png]]

## Current  GP engine
### [DEAP](https://github.com/deap/deap)
a novel evolutionary computation framework for rapid prototyping and testing of ideas.
### [EMADE](https://github.gatech.edu/emade/emade)
Evolutionary Multi-objective Algorithm Design Engine.
- Distributed computing
	- boss-worker mode
- auto-algo-design 

A school project at GaTech, part of [VIP](https://www.vip.gatech.edu/) project.

## Example
[my example](https://github.com/hzhaoc/AAD)