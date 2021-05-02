# perlin-noise
a short malubale perlin noise function in python

no one likes the bumpyness of a sequence of random numbers so i took it upon myself to create a smooth but still random sequence.

my first idea was to take a sequence of random numbers and almost streatching it out like how you might do with a crumpled piece of string but i relized this would make the perlin noise at a certain point dependent of all the points before and after it which would take an insain amout of computing power. So i thought that the simpilist smooth function i could think of was a sin function so if i just layer them a ton then we'll be golden.
