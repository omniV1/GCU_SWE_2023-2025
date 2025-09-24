"""
This script simulates the population dynamics of rabbits and wolves on an island
over a period of 20 years.
"""

def simulate_population():
    """
    Simulates and prints the population of rabbits and wolves for 20 years.
    """
    # --- Simulation Parameters ---
    initial_rabbits = 50
    initial_wolves_year = 5
    initial_wolves_count = 10
    num_years = 20
    
    rabbit_growth_rate = 0.10
    wolf_growth_rate = 0.08
    rabbit_predation_rate = 0.01
    wolf_death_rate = 0.06

    # --- Initial Conditions ---
    rabbits = initial_rabbits
    wolves = 0

    # --- Print Table Header ---
    print("Year | Rabbits | Wolves")
    print("-----|---------|-------")
    print(f"{0:4} | {rabbits:7} | {wolves:6}")

    # --- Simulation Loop ---
    for year in range(1, num_years + 1):
        # Introduce wolves at the start of year 5
        if year == initial_wolves_year:
            wolves = initial_wolves_count

        # Store populations at the start of the year for calculation
        rabbits_at_start_of_year = rabbits
        wolves_at_start_of_year = wolves

        # --- Population Updates ---
        
        # Rabbits: grow, then get eaten
        rabbits_after_growth = rabbits_at_start_of_year * (1 + rabbit_growth_rate)
        
        rabbits_eaten = 0
        if wolves_at_start_of_year > 0:
            # Predation reduces the rabbit population
            rabbits_eaten = rabbits_after_growth * rabbit_predation_rate

        rabbits = rabbits_after_growth - rabbits_eaten

        # Wolves: grow and die
        if wolves_at_start_of_year > 0:
            wolves_born = wolves_at_start_of_year * wolf_growth_rate
            wolves_died = wolves_at_start_of_year * wolf_death_rate
            wolves += (wolves_born - wolves_died)

        # Ensure populations are integers
        rabbits = int(rabbits)
        wolves = int(wolves)
        
        # Print the state at the end of the year
        print(f"{year:4} | {rabbits:7} | {wolves:6}")

if __name__ == "__main__":
    simulate_population()
