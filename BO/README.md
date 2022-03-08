# BO
The simulation class of the multi-channel field synthesiser and the Bayesian optimisation code.

1) ErrorCorrectionFunction_integrate - Function used in BO to optimise the field synthesiser to match a chosen goal pulse shape.
2) bossfunction - The BO function used to run Bayesian optimisation of the simulation.
3) subtargetfunctions - Figures of merit used in BO as a goal for the optimisation.

## Miscellaneous
1) BO_first_test - Testing the Bayesian optimisation class to minimise difficult functions.
2) fails - Old BO classes
3) initial optimisation tests - Trial optimisations of our simulation for different figures of merit.

## Validity_check
Test how BO optimises a parameter for a given number of inital points and interations.

## examples
Example code to show how the BO class can be used.

## synthesiser_simulation_classes
The field synthesiser class which is used to simulate multi-channel laser field synthesis by combining multiple pulses.
1) chirp - pulse defined in frequency-domain with GDD
2) fails - old field synthesiser classes

## tests
Test scripts to run BO for different simulations and different figures of merit.
1) difficult_functions - optimising functions using BO that are hard to optimise
2) real_synth_channels - running BO of the synthesiser with real synthesiser parameters
3) shapes - running BO to match the synthesised field to different shapes

