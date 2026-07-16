import sqlite3
import matplotlib.pyplot as plt
import csv
import random

# =============================================================
# CONSTANTS (PEP8: UPPERCASE)
# =============================================================
DATABASE_NAME = "population_AC.db"
YEARS_TO_SIMULATE = 20
RANDOM_SEED = 42  # Ensures repeatability


# =============================================================
# Function: Reset database (repeatable program)
# =============================================================
def reset_database():
    """
    Drops the population table if it exists so the program
    can be run multiple times without duplicate data.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS population")
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Database reset error:", error)


# =============================================================
# Function: Create database and insert 2023 data
# =============================================================
def create_database():
    """
    Creates the population table and inserts 2023 population
    data for 10 Florida cities.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE population (
                city TEXT,
                year INTEGER,
                population INTEGER
            )
        """)

        cities_2023 = {
            "Miami": 449514,
            "Orlando": 316081,
            "Tampa": 409374,
            "Jacksonville": 971319,
            "Tallahassee": 204523,
            "St_Petersburg": 258308,
            "Hialeah": 220490,
            "Fort_Lauderdale": 187935,
            "Cape_Coral": 216606,
            "Sarasota": 57857
        }

        for city, pop in cities_2023.items():
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Database creation error:", error)


# =============================================================
# Function: Generate random growth rates (repeatable)
# =============================================================
def generate_growth_rates():
    """
    Generates random yearly growth/decline rates for 20 years.
    Uses a fixed seed to ensure repeatability.
    """
    random.seed(RANDOM_SEED)
    return [random.uniform(-0.02, 0.03) for _ in range(YEARS_TO_SIMULATE)]


# =============================================================
# Function: Simulate population changes
# =============================================================
def simulate_population():
    """
    Applies yearly growth/decline rates to each city and inserts
    the new population values into the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        rates = generate_growth_rates()

        cursor.execute("SELECT city, population FROM population WHERE year = 2023")
        base_data = cursor.fetchall()

        for city, pop in base_data:
            current_pop = pop
            year = 2024

            for rate in rates:
                current_pop = int(current_pop * (1 + rate))
                cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, current_pop))
                year += 1

        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Simulation error:", error)


# =============================================================
# Function: Get list of cities
# =============================================================
def get_city_list():
    """
    Retrieves a list of all cities stored in the database.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    conn.close()
    return cities


# =============================================================
# Function: Get population data for a city
# =============================================================
def get_city_population(city):
    """
    Retrieves all population records for a given city.
    Returns a list of (year, population) tuples.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT year, population 
        FROM population 
        WHERE city = ? 
        ORDER BY year
    """, (city,))

    data = cursor.fetchall()
    conn.close()
    return data


# =============================================================
# Function: Export data to CSV (bonus feature)
# =============================================================
def export_to_csv(city):
    """
    Exports population data for a city into a CSV file.
    """
    data = get_city_population(city)

    filename = f"{city}_population_export.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Population"])
        writer.writerows(data)

    print(f"Data exported to {filename}")


# =============================================================
# Function: Show summary statistics
# =============================================================
def show_summary(city):
    """
    Displays summary statistics for a city's population data.
    Includes highest, lowest, average, and total change.
    """
    data = get_city_population(city)
    populations = [row[1] for row in data]

    highest = max(populations)
    lowest = min(populations)
    average = sum(populations) / len(populations)
    total_change = populations[-1] - populations[0]

    print("\nSummary Statistics:")
    print(f"Highest Population: {highest}")
    print(f"Lowest Population: {lowest}")
    print(f"Average Population: {int(average)}")
    print(f"Total Change Over {YEARS_TO_SIMULATE} Years: {total_change}")


# =============================================================
# Function: Plot population growth (Academic Theme)
# =============================================================
def plot_city():
    """
    Plots population growth for a selected city using a clean,
    academic-style graph for readability and professionalism.
    """
    cities = get_city_list()

    print("\nPlease choose a city to visualize:")
    for index, city in enumerate(cities, 1):
        print(f"{index}. {city}")

    choice = input("\nEnter the number of the city: ")

    while not choice.isdigit() or not (1 <= int(choice) <= len(cities)):
        print("Invalid selection. Please enter a valid number.")
        choice = input("Enter the number of the city: ")

    selected_city = cities[int(choice) - 1]
    data = get_city_population(selected_city)

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    # Academic Theme: clean, simple, readable
    plt.figure(figsize=(10, 6))
    plt.plot(
        years,
        populations,
        color="black",        # Simple academic color
        linewidth=2,          # Slightly thicker line
        marker="o",
        markersize=5,
        markerfacecolor="white",
        markeredgecolor="black"
    )

    plt.title(f"Population Growth for {selected_city}", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()

    show_summary(selected_city)


# =============================================================
# Function: Menu system
# =============================================================
def menu():
    """
    Provides a menu system for user interaction.
    """
    while True:
        print("\n--- Population Database Menu ---")
        print("1. Plot City Population")
        print("2. Export City Data to CSV")
        print("3. Show Summary Statistics")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            plot_city()
        elif choice == "2":
            city = input("Enter city name exactly as shown: ")
            export_to_csv(city)
        elif choice == "3":
            city = input("Enter city name exactly as shown: ")
            show_summary(city)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# =============================================================
# Main function
# =============================================================
def main():
    """
    Runs the full program: resets DB, creates data, simulates
    growth, and launches the menu system.
    """
    reset_database()
    create_database()
    simulate_population()
    menu()


# =============================================================
# Run program
# =============================================================
if __name__ == "__main__":
    main()
