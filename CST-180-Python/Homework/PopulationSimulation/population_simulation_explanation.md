---
title: "Island Population Dynamics Simulation"
author: "Owen Lindsey"
subtitle: |
  CST-180: Python Programming 1 \\
  Professor David Parker \\
  Grand Canyon University
date: "September 14, 2025"
# APA 7th Edition Formatting
csl: Homework/PopulationSimulation/apa.csl
bibliography: Homework/PopulationSimulation/references.bib
# General Document Settings
lang: "en"
fontsize: 12pt
linestretch: 1.5 # One-and-a-half-spaced for readability
mainfont: "Times New Roman"
sansfont: "Arial"
monofont: "Courier New"
geometry: "margin=1in"
papersize: tabloid
header-includes: |
  \lstset{breaklines=true}
---
\newpage

## Part One: Algorithm Pseudocode


### Function Definition
```
// FUNCTION simulate_population
// This function simulates the population dynamics of rabbits and wolves on an island
// over a 20-year period, following the specific set of rules for population growth,
// predation, and death rates as defined by the project requirements.
```

### Constants
```
// SET Initial Rabbit Population to 50.
// This is the starting number of rabbits on the island.
SET INITIAL_RABBITS to 50

// SET Rabbit Growth Rate to 10% annually.
SET RABBIT_GROWTH_RATE to 0.10

// SET Wolf Growth Rate to 8% annually.
SET WOLF_GROWTH_RATE to 0.08

// SET Wolf Death Rate to 6% annually.
// The net growth rate for wolves is (8% - 6% = 2%).
SET WOLF_DEATH_RATE to 0.06

// SET Predation Rate to 1% of the rabbit population per wolf, per year.
SET PREDATION_RATE to 0.01

// SET the year wolves are introduced to year 5.
SET WOLF_INTRODUCTION_YEAR to 5

// SET the initial number of wolves introduced to 10.
SET INITIAL_WOLVES_COUNT to 10

// SET the total duration of the simulation to 20 years.
SET SIMULATION_YEARS to 20
```

### Initialization
```
// Initialize the current rabbit population.
SET rabbits to INITIAL_RABBITS
// Initialize the wolf population to zero before their introduction.
SET wolves to 0
```

### Initial Output
```
// Display a header for the results table for clarity.
PRINT "Year | Rabbits | Wolves"
PRINT "-----------------------"
// Display the initial state of the populations at Year 0.
PRINT "   0 |      50 |      0"
```

\newpage

### Simulation Loop
```
// Loop through each year of the simulation from 1 to 20.
FOR year FROM 1 TO SIMULATION_YEARS

    // 1. Calculate rabbit population growth for the year.
    // This calculation happens before predation.
    COMPUTE rabbits as rabbits * (1 + RABBIT_GROWTH_RATE)

    // 2. Introduce the initial wolf pack in the designated year.
    IF year IS EQUAL TO WOLF_INTRODUCTION_YEAR THEN
        SET wolves to INITIAL_WOLVES_COUNT
    ENDIF

    // 3. Calculate rabbit loss due to wolf predation.
    // This only occurs if there is a wolf population on the island.
    IF wolves > 0 THEN
        // Determine the total number of rabbits lost to predation.
        COMPUTE rabbit_loss as rabbits * PREDATION_RATE * wolves
        // Subtract the lost rabbits from the current population.
        COMPUTE rabbits as rabbits - rabbit_loss
    ENDIF

    // 4. Calculate wolf population change for the year.
    // This also only occurs after wolves have been introduced.
    IF wolves > 0 THEN
        // Determine the net growth rate for the wolf population.
        COMPUTE net_wolf_growth_rate as WOLF_GROWTH_RATE - WOLF_DEATH_RATE
        // Apply the net growth rate to the current wolf population.
        COMPUTE wolves as wolves * (1 + net_wolf_growth_rate)
    ENDIF

    // 5. Ensure population counts are whole numbers.
    // It is not possible to have a fraction of an animal.
    COMPUTE rabbits as INTEGER(rabbits)
    COMPUTE wolves as INTEGER(wolves)

    // 6. Prevent populations from becoming negative.
    // A population cannot fall below zero.
    IF rabbits < 0 THEN
        SET rabbits to 0
    ENDIF
    IF wolves < 0 THEN
        SET wolves to 0
    ENDIF

    // 7. Display the final population counts for the current year.
    PRINT year, rabbits, wolves
ENDFOR
// END FUNCTION
```
\newpage

## Part Two: Population Dynamics Chart
| Year | Rabbits | Wolves |
|:----:|:-------:|:------:|
| 0    | 50      | 0      |
| 1    | 55      | 0      |
| 2    | 60      | 0      |
| 3    | 66      | 0      |
| 4    | 72      | 0      |
| 5    | 71      | 10     |
| 6    | 70      | 10     |
| 7    | 69      | 10     |
| 8    | 67      | 10     |
| 9    | 65      | 10     |
| 10   | 63      | 10     |
| 11   | 62      | 10     |
| 12   | 61      | 10     |
| 13   | 60      | 10     |
| 14   | 59      | 10     |
| 15   | 57      | 10     |
| 16   | 55      | 10     |
| 17   | 54      | 10     |
| 18   | 53      | 10     |
| 19   | 52      | 10     |
| 20   | 51      | 10     |

### Analysis of Population Dynamics

- **Stable Wolf Population:** The number of wolves remains constant at 10 after their introduction. This is due to the net annual growth rate of 2% (8% growth minus 6% death) being insufficient to add a whole new wolf to the population from a starting base of 10 (`10 * 1.02 = 10.2`). Because population counts are treated as whole numbers (integers), the fractional growth is discarded each year.
- **Gradual Rabbit Decline:** After the wolves arrive, the rabbit population begins a steady decline. The rabbits' 10% growth rate is offset by the new predation from the 10 wolves (1% predation per wolf). Since the predation is calculated on the larger, post-growth rabbit numbers, it results in a slight net decrease in the rabbit population each year.
- **Initial Rabbit Boom:** For the first four years, the rabbit population grows without any predators, leading to a rapid increase in their numbers.
