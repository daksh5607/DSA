# Step 1: Define the Weather Record ADT
class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature

# Step 2: Implement a 2D array-based data storage system
class WeatherDataStorage:
    def __init__(self, years, cities):
        # Using a 2D list to represent the 2D array
        self.data = [[None for _ in cities] for _ in years]
        self.years = {year: i for i, year in enumerate(years)}
        self.cities = {city: i for i, city in enumerate(cities)}

    # Method to insert a new weather record
    def insert(self, record):
        try:
            year = int(record.date.split('/')[-1])
            year_index = self.years.get(year)
            city_index = self.cities.get(record.city)

            if year_index is not None and city_index is not None:
                self.data[year_index][city_index] = record.temperature
                print(f"Record for {record.city} on {record.date} inserted successfully.")
            else:
                print("Error: Year or City not found in the storage system.")
        except (ValueError, IndexError):
            print("Error: Invalid date format. Please use day/month/year.")

    # Method to retrieve temperature data for a specific city and year
    def retrieve(self, city, year):
        year_index = self.years.get(year)
        city_index = self.cities.get(city)

        if year_index is not None and city_index is not None:
            temperature = self.data[year_index][city_index]
            if temperature is not None:
                print(f"Temperature for {city} in {year}: {temperature}°C")
                return temperature
            else:
                print(f"No data available for {city} in {year}.")
                return None
        else:
            print("Error: Year or City not found in the storage system.")
            return None

    # Step 3: Develop row-major and column-major access methods
    def rowMajorAccess(self):
        print("\nAccessing data in row-major order:")
        for row in self.data:
            print(row)

    def columnMajorAccess(self):
        print("\nAccessing data in column-major order:")
        num_rows = len(self.data)
        if num_rows > 0:
            num_cols = len(self.data[0])
            for j in range(num_cols):
                column = [self.data[i][j] for i in range(num_rows)]
                print(column)

    # Step 4: Handle sparse data using sentinel values
    def handleSparseData(self):
        print("\nSparse data is handled by using 'None' as a sentinel value.")

    # Step 5: Analyze and document time and space complexity
    def analyzeComplexity(self):
        print("\n--- Complexity Analysis ---")
        print("Space Complexity: O(Y * C) where Y is the number of years and C is the number of cities.")
        print("Time Complexity:")
        print("  - Insertion: O(1) on average for map lookups and list assignment.")
        print("  - Retrieval: O(1) on average for map lookups and list access.")

# Example Usage
if __name__ == "__main__":
    years_list = [2023, 2024, 2025]
    cities_list = ["Delhi", "Kolkata", "Chennai"]

    weather_system = WeatherDataStorage(years_list, cities_list)

    # Create and insert some weather records
    weather_system.insert(WeatherRecord("14/09/2023", "Delhi", 25.5))
    weather_system.insert(WeatherRecord("15/09/2024", "Kolkata", 28.0))
    

    # Attempt to insert a record for a year not in the system
    weather_system.insert(WeatherRecord("17/09/2026", "Delhi", 19.5))

    # Retrieve data
    weather_system.retrieve("Delhi", 2023)
    weather_system.retrieve("Kolkata", 2025)
    weather_system.retrieve("Chennai", 2024)
    
    # Display array content and analysis
    weather_system.rowMajorAccess()
    weather_system.columnMajorAccess()
    weather_system.handleSparseData()
    weather_system.analyzeComplexity()



