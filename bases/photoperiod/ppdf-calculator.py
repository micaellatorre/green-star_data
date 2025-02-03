import pandas as pd

# Load the CSV file
df = pd.read_csv('hybrid.csv')

# Function to calculate PPFD based on DLI and time (using the highest value in the time range)
def calculate_ppfd(dli, time_range):
    try:
        # Get the highest number in the time range (hours per day)
        time_hours = int(time_range.split('-')[1])
        # Calculate PPFD (PPFD = DLI / (hours per day * 3600)) and round to 2 decimals
        ppfd = dli / (time_hours * 3600) * 1e6  # Convert from μmol/m²/day to μmol/m²/s
        return round(ppfd, 2)  # Truncate to 2 decimal places
    except:
        return None  # In case of missing or incorrect data

# Apply the PPFD calculation to the DLI and DLIwCO2 columns
df['PPFD'] = df.apply(lambda row: calculate_ppfd(row['DLI'], row['time']), axis=1)
df['PPFDwCO2'] = df.apply(lambda row: calculate_ppfd(row['DLIwCO2'], row['time']), axis=1)

# Save the updated CSV file
df.to_csv('hybrid_updated.csv', index=False)

print("auto.csv updated successfully with PPFD and PPFDwCO2 columns (values truncated to 2 decimals)!")
