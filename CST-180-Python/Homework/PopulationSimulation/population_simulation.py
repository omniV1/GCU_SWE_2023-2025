# Owen Lindsey
# Rabbits and Wolves
# Due: 09/28/2025

def simulate_population(
    initial_rabbits=50,         # Rabbits at year 0
    initial_wolves=0,           # Wolves at year 0 (introduced later)
    rabbit_growth_rate=0.10,    # 10% rabbit growth
    wolf_growth_rate=0.08,      # 8% wolf growth
    wolf_death_rate=0.06,       # 6% wolf death
    predation_rate=0.01,        # 1% total predation rate when wolves present
    wolf_introduction_year=5,   # Year wolves are introduced
    initial_wolf_count=10,      # Number of wolves introduced
    simulation_years=20         # Total years to simulate
):
    """
    Simulates rabbit and wolf population dynamics.
    Returns a list of (year, rabbits, wolves).
    Raises ValueError if invalid parameters are provided.
    """

    # Validate inputs
    if initial_rabbits < 0 or initial_wolves < 0:
        raise ValueError("Starting populations must be non-negative.")
    if rabbit_growth_rate < 0 or wolf_growth_rate < 0 or wolf_death_rate < 0 or predation_rate < 0:
        raise ValueError("Growth/death rates must be non-negative.")
    if simulation_years <= 0:
        raise ValueError("Simulation years must be positive.")

    # Initialize state
    rabbits = initial_rabbits
    wolves = initial_wolves
    results = []

    # Print header
    print(f'{"Year":^6}{"Rabbits":^12}{"Wolves":^12}')
    print('-' * 30)

    # Year 0
    print(f'{0:^6}{rabbits:^12}{wolves:^12}')
    results.append((0, rabbits, wolves))

    # Simulation loop
    for year in range(1, simulation_years + 1):
        # 1. Rabbit population growth
        rabbits = rabbits * (1 + rabbit_growth_rate)
        
        # 2. Wolf introduction and population change
        if year == wolf_introduction_year:
            wolves = initial_wolf_count
            # Apply death rate immediately upon introduction
            wolves = wolves * (1 - wolf_death_rate)
        elif wolves > 0:
            # Net growth: 8% growth - 6% death = 2% net growth
            wolves = wolves * (1 + wolf_growth_rate - wolf_death_rate)

        # 3. Rabbit loss due to predation (1% total when wolves present)
        if wolves > 0:
            rabbits = rabbits * (1 - predation_rate)

        # 5. Ensure population counts are whole numbers
        rabbits = int(rabbits)
        wolves = int(wolves)

        # 6. Prevent negative populations
        rabbits = max(rabbits, 0)
        wolves = max(wolves, 0)

        # Print and store results
        print(f'{year:^6}{rabbits:^12}{wolves:^12}')
        results.append((year, rabbits, wolves))

    return results


# --- Testing with Expected Results ---
try:
    # Default run (rabbits grow until year 5, then wolves arrive)
    print("\nDefault Simulation Run:\n")
    default_results = simulate_population()

    # EXPECTED (first few years, rounded to ints):
    # Year 0: Rabbits=50, Wolves=0
    # Year 1: Rabbits=55, Wolves=0
    # Year 2: Rabbits=60, Wolves=0
    # Year 3: Rabbits=66, Wolves=0
    # Year 4: Rabbits=72, Wolves=0
    # Year 5: Rabbits drops after wolves introduced (approx 79 → 71), Wolves=10
    # Year 6: Rabbits ~70, Wolves grow slightly (~10.2 → 10)
    # By Year 20, wolves stabilize around teens, rabbits keep shrinking under predation.

    # Modified run with more wolves earlier
    print("\nModified Simulation Run (100 rabbits, wolves at year 2, 5 wolves):\n")
    mod_results = simulate_population(initial_rabbits=100, wolf_introduction_year=2, initial_wolf_count=5)

    # EXPECTED:
    # Year 0: Rabbits=100, Wolves=0
    # Year 1: Rabbits=110, Wolves=0
    # Year 2: Wolves introduced, Rabbits drop (121 → ~115), Wolves=5
    # Year 3: Rabbits continue but under pressure, Wolves grow (~5.1 → 5)
    # By Year 10, rabbits much lower than default run.

    # Invalid run (should fail)
    print("\nInvalid Test Run (expect error):\n")
    simulate_population(initial_rabbits=-10)  # invalid input

except ValueError as e:
    # Catch intended validation errors
    print(f"Simulation failed: {e}")

except Exception as e:
    # Catch unexpected errors
    print(f"Unexpected error: {e}")
