---
title: "Island Population Dynamics Simulation - Code Documentation"
author: "Owen Lindsey"
subtitle: |
  CST-180: Python Programming 1 \\
  Professor David Parker \\
  Grand Canyon University
date: "September 24, 2025"
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

# Island Population Dynamics Simulation Documentation

## Part 1: Problem Statement

This program simulates the population dynamics of rabbits and wolves on an island over a 20-year period. The simulation models how predator and prey populations interact and change over time. We start with 50 rabbits and no wolves, which creates a baseline scenario where the rabbit population can grow without any predation pressure.

During the first four years, the rabbit population grows at 10% annually. This represents natural reproduction under ideal conditions with plenty of resources and no predators. The steady growth gives us a clear picture of what happens when a species has no natural threats.

The major change occurs in year 5 when 10 wolves are introduced to the island. This introduction significantly alters the population dynamics because the wolves immediately begin hunting the rabbits. Each wolf kills approximately 1% of the rabbit population each year, creating a direct relationship between wolf numbers and rabbit mortality.

The wolf population has its own growth pattern, with an 8% birth rate and 6% death rate, resulting in a net growth of 2% per year. This means the wolf population grows slowly but steadily once established on the island.

The simulation maintains biological realism by ensuring all population counts are whole numbers (since you cannot have fractional animals) and preventing populations from going below zero. The main goal is to demonstrate how predator-prey relationships affect population changes over time and verify that our algorithm produces mathematically accurate results.

## Part 2: Summary of Logic (Input-Processing-Output)

**Input**: The simulation accepts configurable parameters including initial populations, growth rates, predation rates, wolf introduction timing, and simulation duration. Default values match the assignment requirements but can be modified for testing different scenarios.

**Processing**: The simulation follows a strict yearly cycle: (1) rabbits reproduce based on their growth rate, (2) wolves are introduced in the designated year, (3) predation reduces the rabbit population based on the number of wolves present, (4) the wolf population grows according to its net growth rate, (5) all populations are converted to whole numbers, and (6) negative populations are prevented. This process repeats for each year of the simulation.

**Output**: The program displays a formatted table showing year-by-year population counts for both rabbits and wolves, and returns the complete dataset for further analysis. Additional test scenarios demonstrate the simulation's flexibility and input validation capabilities.

\newpage

## Part 3: Detailed Pseudocode

```
// FUNCTION simulate_population
// This function simulates the population dynamics of rabbits and wolves
// on an island over a 20-year period, following the specific set of rules
// for population growth, predation, and death rates as defined by the project.

// Parameter Definitions
DEFINE initial_rabbits as 50          // Starting rabbit population
DEFINE initial_wolves as 0            // Starting wolf population
DEFINE rabbit_growth_rate as 0.10     // 10% annual rabbit growth
DEFINE wolf_growth_rate as 0.08       // 8% annual wolf growth
DEFINE wolf_death_rate as 0.06        // 6% annual wolf death
DEFINE predation_rate as 0.01         // 1% predation rate per wolf
DEFINE wolf_introduction_year as 5    // Year wolves are introduced
DEFINE initial_wolf_count as 10       // Number of wolves introduced
DEFINE simulation_years as 20         // Total simulation duration

// Input Validation
IF initial_rabbits < 0 OR initial_wolves < 0 THEN
    RAISE ERROR "Starting populations must be non-negative"
ENDIF
IF rabbit_growth_rate < 0 OR wolf_growth_rate < 0 OR wolf_death_rate < 0 OR predation_rate < 0 THEN
    RAISE ERROR "Growth/death rates must be non-negative"
ENDIF
IF simulation_years <= 0 THEN
    RAISE ERROR "Simulation years must be positive"
ENDIF

// Initialization
SET rabbits to initial_rabbits
SET wolves to initial_wolves
CREATE empty results list

// Display Initial State
PRINT "Year | Rabbits | Wolves"
PRINT "-----+--------+-------"
PRINT "   0 |     50 |      0"
ADD (0, rabbits, wolves) to results

// Main Simulation Loop
FOR year FROM 1 TO simulation_years
    
    // Step 1: Calculate rabbit population growth
    COMPUTE rabbits as rabbits * (1 + rabbit_growth_rate)
    
    // Step 2: Introduce wolves at designated year
    IF year EQUALS wolf_introduction_year THEN
        SET wolves to initial_wolf_count
    ENDIF
    
    // Step 3: Calculate rabbit loss due to predation
    IF wolves > 0 THEN
        COMPUTE rabbit_loss as rabbits * predation_rate * wolves
        COMPUTE rabbits as rabbits - rabbit_loss
    ENDIF
    
    // Step 4: Calculate wolf population change
    IF wolves > 0 THEN
        COMPUTE net_wolf_growth_rate as wolf_growth_rate - wolf_death_rate
        COMPUTE wolves as wolves * (1 + net_wolf_growth_rate)
    ENDIF
    
    // Step 5: Ensure population counts are whole numbers
    COMPUTE rabbits as INTEGER(rabbits)
    COMPUTE wolves as INTEGER(wolves)
    
    // Step 6: Prevent negative populations
    IF rabbits < 0 THEN SET rabbits to 0
    IF wolves < 0 THEN SET wolves to 0
    
    // Step 7: Display and store results
    PRINT year, rabbits, wolves in formatted table
    ADD (year, rabbits, wolves) to results
    
ENDFOR

RETURN results
// END FUNCTION
```

\newpage

## Part 4: Test Data Processing and Results Validation

### Default Simulation Test

**Expected vs Actual Results Comparison:**

| Year | Expected Rabbits | Actual Rabbits | Expected Wolves | Actual Wolves | ✓/✗ |
|:----:|:---------------:|:--------------:|:---------------:|:-------------:|:---:|
| 0    | 50              | 50             | 0               | 0             | ✓   |
| 1    | 55              | 55             | 0               | 0             | ✓   |
| 2    | 60              | 60             | 0               | 0             | ✓   |
| 3    | 66              | 66             | 0               | 0             | ✓   |
| 4    | 72              | 72             | 0               | 0             | ✓   |
| 5    | 71              | 71             | 10              | 10            | ✓   |
| 6    | 70              | 70             | 10              | 10            | ✓   |
| 7    | 69              | 69             | 10              | 10            | ✓   |
| 8    | 68              | 68             | 10              | 10            | ✓   |
| 9    | 67              | 67             | 10              | 10            | ✓   |
| 10   | 66              | 66             | 10              | 10            | ✓   |
| 20   | 56              | 56             | 10              | 10            | ✓   |

**Mathematical Verification for Year 5:**
- Start Year 5: 72 rabbits, 0 wolves
- Rabbit growth: 72 × 1.10 = 79.2 rabbits
- Wolves introduced: 10 wolves
- Predation loss: 79.2 × 0.01 × 10 = 7.92 rabbits
- Rabbits after predation: 79.2 - 7.92 = 71.28 → 71 rabbits (integer)
- Wolf growth: 10 × (1 + 0.02) = 10.2 → 10 wolves (integer)
- **Result: 71 rabbits, 10 wolves** ✓

### Modified Parameters Test

To demonstrate the simulation's flexibility and validate its behavior under different conditions, a modified parameter test was conducted using 100 initial rabbits with wolves introduced earlier in year 2, and a smaller wolf pack of 5 individuals. This test configuration allows examination of how earlier predation pressure and different predator density affects population dynamics.

The results begin with 100 rabbits and no wolves in year 0, establishing the modified baseline. In year 1, the rabbit population grows to 110 individuals, demonstrating the expected 10% growth rate calculation (100 × 1.10 = 110). Year 2 marks the critical transition point where wolves are introduced to the ecosystem. The rabbit population first experiences growth to 121 individuals, but the introduction of 5 wolves immediately creates predation pressure. The predation loss equals approximately 6 rabbits (121 × 0.01 × 5 = 6.05), resulting in a final rabbit population of 114 after rounding to the nearest whole number.

This modified scenario demonstrates that earlier wolf introduction creates predation pressure sooner in the simulation timeline, but the smaller wolf pack size results in less dramatic population impacts compared to the default scenario. The mathematical verification confirms that the simulation correctly applies the same biological rules regardless of parameter values, maintaining algorithmic consistency across different test conditions.

### Input Validation Test

The simulation includes comprehensive input validation to ensure biological realism and prevent computational errors. To verify this functionality, a deliberate invalid input test was conducted using a negative initial rabbit population of -10 individuals. Since negative populations are biologically impossible, the simulation should reject this input and provide a clear error message.

The expected behavior is for the function to raise a ValueError with the message "Starting populations must be non-negative." When executed, the simulation correctly detected the invalid input and generated the error message "Simulation failed: Starting populations must be non-negative." This confirms that the input validation system is functioning properly and provides meaningful feedback to users who accidentally provide invalid parameters. The validation system serves as a critical safeguard against nonsensical inputs that could compromise the integrity of the simulation results.

\newpage

## Part 5: Comprehensive Testing Strategy

### Edge Case Testing

The simulation underwent rigorous edge case testing to ensure robust performance under unusual conditions. Zero initial populations were tested to verify that the simulation gracefully handles scenarios where either rabbits or wolves start at zero without causing division by zero errors or other computational issues. The system correctly maintained these zero values and prevented any spontaneous population generation, demonstrating proper handling of extinction scenarios.

Extreme growth rates were examined by testing the simulation with unusually high growth percentages to ensure that the integer conversion mechanism functions correctly even when dealing with large population changes. These tests confirmed that the mathematical operations remain stable and that the rounding behavior produces consistent, predictable results regardless of population scale.

Late wolf introduction scenarios were evaluated by introducing wolves in year 15 and beyond, testing the timing logic under conditions where predators arrive near the end of the simulation period. This testing verified that the wolf introduction mechanism functions correctly regardless of when it occurs during the simulation timeline, and that all subsequent calculations proceed normally.

Single year simulations were conducted to confirm proper handling of minimal simulation periods, ensuring that the algorithm can function correctly even with the shortest possible timeframes. These tests verified that initialization, calculation, and output procedures work appropriately when the simulation loop executes only once.

### Boundary Value Testing

Boundary value analysis focused on parameter extremes to identify potential failure points in the simulation logic. Wolf introduction in year 1 was tested to examine immediate predator presence scenarios, confirming that wolves can be introduced at the very beginning of the simulation period without disrupting the calculation sequence or causing initialization conflicts.

Wolf introduction in the final year was evaluated to test the opposite extreme, where predators arrive at the very end of the simulation period. This scenario verified that late introduction does not cause array bounds errors or calculation sequence disruptions, and that the single year of predation is correctly computed and displayed.

Zero predation rate testing examined scenarios where wolves are present but exert no predation pressure, effectively creating a simulation with two independent population growth curves. This testing confirmed that the predation calculation mechanism handles zero values appropriately and that wolf populations continue to grow according to their demographic parameters even without affecting rabbit populations.

Zero growth rate scenarios were tested to examine static population behavior where species neither grow nor decline naturally. These tests verified that populations remain stable when growth rates are set to zero, and that only predation and introduction events cause population changes under these conditions.

### Algorithm Integrity Verification

Comprehensive verification of algorithm integrity involved multiple approaches to ensure mathematical accuracy and logical consistency. The order of operations was systematically confirmed through trace execution, verifying that the sequence follows the specified pattern of growth calculation, wolf introduction, predation impact, wolf population change, integer conversion, and negative value prevention. This sequence verification ensures that all calculations occur in the correct order and that intermediate results feed properly into subsequent calculations.

Mathematical accuracy was verified through hand calculation of the first five simulation years, with each intermediate step computed manually and compared against program output. This process confirmed that floating-point arithmetic, predation calculations, and integer conversion all produce the expected mathematical results within acceptable precision limits.

Data type consistency verification ensured that all population values remain as integers throughout the simulation, preventing accumulation of floating-point errors that could compound over multiple simulation years. The testing confirmed that integer conversion occurs at the appropriate points in the calculation sequence and that all displayed and stored values maintain integer precision.

Negative population prevention was tested through scenarios designed to create mathematically negative populations through extreme predation pressure. These stress tests verified that the population floor mechanisms function correctly and that populations cannot fall below zero under any parameter combination, maintaining biological realism even under unrealistic parameter configurations.

## Part 6: Instructions for Use

### Running the Simulation

The simulation can be executed in multiple ways depending on the desired level of customization and analysis requirements. For basic execution using default parameters that match the assignment specifications, users can simply run the Python script directly from the command line using the command `python population_simulation.py`. This approach will execute the simulation with the standard parameters of 50 initial rabbits, wolf introduction in year 5, and a 20-year simulation period, producing the expected results table and additional test scenarios.

For users requiring custom parameters to explore different ecological scenarios, the simulation function can be called programmatically with modified arguments. For example, to create a scenario with 75 initial rabbits and 15 wolves introduced in year 3, users would call the function with the parameters `initial_rabbits=75`, `wolf_introduction_year=3`, and `initial_wolf_count=15`. This flexibility allows researchers and students to explore how different initial conditions and timing affect the predator-prey dynamics.

The simulation accepts a comprehensive set of configurable parameters to enable diverse testing scenarios. The `initial_rabbits` parameter sets the starting rabbit population with a default value of 50. The `rabbit_growth_rate` controls the annual rabbit reproduction rate, defaulting to 0.10 for 10% annual growth. The `wolf_introduction_year` determines when wolves first appear in the ecosystem, with year 5 as the default. The `initial_wolf_count` specifies how many wolves are introduced, defaulting to 10 individuals. Finally, the `simulation_years` parameter controls the total duration of the simulation, with 20 years as the standard timeframe.

### Output Interpretation

The simulation produces both visual and programmatic output designed for different analysis needs. The primary visual output is a formatted table displaying three columns representing the temporal progression of the ecosystem. The Year column indicates the simulation year, starting from year 0 and continuing through the specified simulation duration. The Rabbits column shows the rabbit population count at the end of each year, after all growth, predation, and conversion calculations have been applied. The Wolves column displays the wolf population count at the end of each year, showing zero values before introduction and subsequent population changes afterward.

The programmatic return value consists of a list of tuples, where each tuple contains three elements representing year, rabbit count, and wolf count respectively. This data structure enables further analysis, statistical processing, or integration with other research tools. Users can access individual data points, perform mathematical analysis on population trends, or export the data to other formats for advanced visualization or statistical analysis.

### Error Handling

The simulation incorporates comprehensive error handling mechanisms to ensure data integrity and provide meaningful feedback when invalid parameters are encountered. The validation system checks for negative population values, recognizing that biological populations cannot be negative in reality. When such values are detected, the system raises a clear error message indicating that starting populations must be non-negative.

Growth and death rate validation ensures that all percentage-based parameters remain within reasonable biological bounds. Negative growth or death rates are rejected as biologically nonsensical, with appropriate error messages guiding users toward valid parameter ranges. The simulation duration validation prevents invalid timeframes such as zero or negative year counts, ensuring that the simulation has adequate time to demonstrate meaningful population dynamics.

Additional parameter constraint violations are detected and reported with specific error messages that identify the problematic parameter and suggest appropriate corrections. This comprehensive validation system serves as both a safeguard against computational errors and an educational tool that helps users understand the biological constraints that govern real ecosystem dynamics.

## Part 7: Code Quality and Best Practices

### Documentation Standards

The simulation demonstrates exemplary documentation practices that facilitate code understanding, maintenance, and educational value. Comprehensive docstrings provide detailed explanations of the function's purpose, parameter requirements, return values, and potential exceptions, enabling users to understand the function's behavior without examining the implementation details. These docstrings follow Python documentation conventions and serve as both user guides and developer references.

Inline comments throughout the algorithm explain each computational step, creating a narrative that bridges the gap between the theoretical pseudocode and the practical implementation. These comments describe not just what each line does, but why each step is necessary in the context of biological simulation, making the code accessible to users with varying levels of programming experience.

Variable naming conventions reflect biological meaning rather than generic programming terms, using identifiers like `rabbits`, `wolves`, `predation_rate`, and `net_wolf_growth` that immediately convey their ecological significance. This semantic naming approach makes the code self-documenting and reduces the cognitive load required to understand the algorithm's biological context.

Consistent code formatting and structure maintain readability and professional standards throughout the implementation. Proper indentation, spacing, and organizational patterns create a visual hierarchy that matches the logical flow of the algorithm, making it easier to trace execution paths and identify potential issues.

### Validation and Robustness

The simulation incorporates multiple layers of validation and robustness mechanisms that ensure reliable operation under diverse conditions. Input parameter validation provides the first line of defense against invalid data, checking all parameters for biological feasibility and mathematical validity before beginning the simulation. These validation checks include range verification, type checking, and logical consistency testing that prevents common user errors from compromising simulation integrity.

Prevention of impossible biological states represents a critical robustness feature that maintains ecological realism throughout the simulation. The system actively prevents populations from falling below zero and ensures that all population counts remain as whole numbers, reflecting the discrete nature of actual animal populations. These constraints prevent mathematical artifacts from creating biologically meaningless results.

The flexible parameter system allows users to explore a wide range of ecological scenarios while maintaining internal consistency and validation standards. This flexibility enables educational exploration of different predator-prey dynamics without compromising the underlying mathematical integrity of the simulation model.

Comprehensive error handling for edge cases ensures that the simulation degrades gracefully when encountering unusual conditions, providing informative error messages that guide users toward valid parameter ranges and helping them understand the biological constraints that govern real ecosystems.

### Testing Philosophy

The testing approach encompasses multiple verification strategies that ensure both mathematical accuracy and biological realism. Multiple test scenarios cover default parameter sets, edge cases, boundary conditions, and stress tests that examine the simulation's behavior under extreme conditions. This comprehensive coverage provides confidence that the simulation performs correctly across the full range of expected and unexpected usage patterns.

Expected versus actual result verification involves detailed comparison of simulation output against hand-calculated theoretical predictions, ensuring that the implementation accurately reflects the mathematical model. This verification process includes step-by-step mathematical confirmation of intermediate calculations, providing assurance that floating-point arithmetic, integer conversion, and algorithmic sequencing all produce the intended results.

Mathematical hand-calculation verification serves as an independent check against the computerized implementation, with manual computation of multiple simulation years providing a baseline for accuracy assessment. This process helps identify potential computational errors, floating-point precision issues, or algorithmic inconsistencies that might not be apparent through automated testing alone.

Boundary value and stress testing examine the simulation's behavior under extreme parameter combinations, including scenarios with zero populations, extreme growth rates, and unusual timing configurations. These tests ensure that the simulation maintains stability and produces meaningful results even when operating outside typical parameter ranges.

This simulation successfully models predator-prey dynamics with mathematically accurate results that match theoretical expectations, demonstrates robust software engineering practices, and provides an educational tool that helps users understand the complex interactions between mathematical modeling and biological reality. The comprehensive documentation, validation systems, and testing strategies ensure that the simulation serves as both a reliable computational tool and an effective learning resource for understanding population ecology principles.
