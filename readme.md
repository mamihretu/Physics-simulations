
# Physics simulations

## Ising model
A statistical model used to estimate the average internal energy and magnetization of a single domain of ferromagnet


Note on ferromagnets:

As the name signifies, ferromagnets are materials with a magnetic property but despite the presence of magnetization this materials do not behave like common magnets. This is because, unlike common magnets, magnetic alignment within the ferromagnet occurs locally within microscopic domains. Globally each of this domains point in random directions and tend cancel out the effect of others, hence no magnetization is observed at large scale.

The ising model focuses on one domain and tries to model how it's magnetization occurs. This is done by simulating a simplified dynamics where only one magnetic dipole is flipped at a time based on a sampling algorithm called Metropolis algorithm.

Metropolis algorithm: 

Whether or not to flip the dipole is decided by the metropolis algorithm where a dipole is chosen randomly and the effect it would have on the internal energy is checked. If change in internal energy is negative the dipole is flipped, whereas if the change is positive, the boltzaman factor of the energy is compared with a random number between 0-1, if the factor is larger than the random number the dipole is flipped, otherwise, it is not 


## Graphical output from eight runs of the ising program, at successively lower temperatures. Each black square represents an "up" dipole and each white square represents a "down" dipole. T is temperature in units of E/k

![monte-carlo-multiple](https://user-images.githubusercontent.com/71546703/140597209-49b9c263-69d2-45ea-80b1-668f5d60c0de.JPG)





## Alternate uses

This algorithm can be used for any project where all scenarios can not be sampled, in this case instead of being sampled randomly states are sampled using the metropolis algorithm


## How to run

### option 1,
simply download and run .py file

### option 2,
see real time implementation on https://michael-mihretu.herokuapp.com/ising

## needed modules for python implementation
1. turtle
2. numpy
