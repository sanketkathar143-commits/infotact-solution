import pandas as pd
import matplotlib.pyplot as a plt
data = pd.read_csv("data/climate_data.csv")

# Display the first five records
print("Climate Dataset:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Calculate average temperature
if "temperature" in data.columns:
    avg_temp = data["temperature"].mean()
    print("\nAverage Temperature:", round(avg_temp, 2))

    # Plot temperature changes
    data["temperature"].plot(
        title="Climate Temperature Analysis",
        xlabel="Record",
        ylabel="Temperature"
    )

    plt.tight_layout()
    plt.show()
else:
    print("The dataset must contain a 'temperature' column.")
