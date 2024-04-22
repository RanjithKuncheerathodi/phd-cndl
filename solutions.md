# Ranjith K

## Three major results from the Ranjan et al study

1. Seizure activity initiates in the cortico-thalamic circuit.
2. Proposed algorithm identifies key nodes primarily in the cortex driving the hypersynchronous activity.
3. Role of network structures in shaping the seizure dynamics and techniques developed can work well with patient specific data. 

## Key nodes involved in the propagation of synchronization

List them here.

## Basic model simulation (single iteration)

### How many transitions do you see in a single simulation run?
Write a single number here. Also include a plot of the entire timeseries.

### How do you define the transition time?
Transition time is the time taken by a system or process to move from one state to another. In the context of this example, it specifically denotes the time taken for various brain regions to transition from a desynchronized state to a synchronized state.

To identify these transitions, a threshold is set based on the mean of the global synchrony measure. When the global synchrony value surpasses this threshold, it signifies a synchronized state, whereas a value below it indicates a desynchronized state. The moment when this state changes from desynchronization to synchronization is regarded as a state transition.

To calculate the transition time, the start time of the state change (desynchronization to synchronization) is recorded, along with the peak time of the transition just before it begins to decline. The transition time is then determined as the difference between the peak time and the start time. This process is repeated for all observed transitions.

### What is the average transition time you observe? Include units!
Write a single number here.(Epileptic seizures can range from several seconds to several minutes!).
You can include a plot that shows all transitions superimposed, aligned to the start time of the transition.

### Include a box plot of the transition times for a single experiment below.
Include the plot here.


## Basic model simulation (different initial conditions)

### Include two box plots below, one for number of transitions and another for transition time
Include the plots here.

## Advanced simulations

### Box plot for number of events
Include the plot here.


### Box plot for transition time
Include the plot here.

## Interpreting results

Provide your answer here.
