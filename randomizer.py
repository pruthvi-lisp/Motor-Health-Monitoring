import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Select the motor name properly
motor_name = "Agri-Fusion"


np.random.seed(0)  # For reproducibility
base_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
timestamps = [base_time + timedelta(seconds=120*i) for i in range(1000)]

# Generate random values for voltage and horsepower appropriately
np.random.seed(0)  # For reproducibility
voltage_values = np.random.uniform(low=225, high=230, size=1000)
horsepower_values = np.random.uniform(low=2.6, high=3, size=1000)
speed_values = np.random.uniform(low=48, high=50, size=1000)
# Create a new dataframe with the generated data
new_motor_data = pd.DataFrame({
    'Timestamp': timestamps,
    'Motor Name': motor_name,
    'Voltage': voltage_values,
    'Horsepower': horsepower_values,
    'Speed': speed_values
})


# Save the new dataframe to a CSV file
#new_motor_data.to_csv('randomized_motor_data.csv', index=False)

print("CSV file 'Horizontal AC_randomized_motor_data.csv' has been generated.")


# Save the new dataframe to a CSV file
new_output_path = 'G:Agri-Fusion.csv'
new_motor_data.to_csv(new_output_path, index=False)

new_output_path