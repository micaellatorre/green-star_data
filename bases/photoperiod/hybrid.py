import pandas as pd

# Load the CSV files for photoperiod and automatic strains
photoperiod_df = pd.read_csv('photoperiod_updated.csv')
automatic_df = pd.read_csv('auto_updated.csv')

# Function to create hybrid data
def create_hybrid_strain(photoperiod_row, automatic_row):
    hybrid_row = {}
    hybrid_row['range'] = photoperiod_row['range']  # You can adjust this as needed
    hybrid_row['stage'] = photoperiod_row['stage']  # Adjust as needed
    hybrid_row['DLI'] = (photoperiod_row['DLI'] + automatic_row['DLI']) / 2
    hybrid_row['DLIwCO2'] = (photoperiod_row['DLIwCO2'] + automatic_row['DLIwCO2']) / 2
    hybrid_row['regCO2'] = (photoperiod_row['regCO2'] + automatic_row['regCO2']) / 2
    hybrid_row['boostCO2'] = (photoperiod_row['boostCO2'] + automatic_row['boostCO2']) / 2
    hybrid_row['time'] = photoperiod_row['time']  # Choose how to handle this
    hybrid_row['spectrum1'] = photoperiod_row['spectrum1']  # Or average
    hybrid_row['spectrum1Color'] = photoperiod_row['spectrum1Color']
    hybrid_row['spectrumRel'] = photoperiod_row['spectrumRel']
    hybrid_row['spectrum2'] = automatic_row['spectrum2']  # Or average
    hybrid_row['spectrum2Color'] = automatic_row['spectrum2Color']
    hybrid_row['distance'] = photoperiod_row['distance']
    hybrid_row['hex'] = photoperiod_row['hex']  # You can adjust this as needed

    return hybrid_row

# Create a new DataFrame for hybrid strains
hybrid_data = []

# Iterate through the rows of the photoperiod and automatic DataFrames
for idx in range(len(photoperiod_df)):
    # Create a hybrid strain from the corresponding rows (adjust if not one-to-one)
    hybrid_strain = create_hybrid_strain(photoperiod_df.iloc[idx], automatic_df.iloc[idx])
    hybrid_data.append(hybrid_strain)

# Convert the list of hybrid strains to a DataFrame
hybrid_df = pd.DataFrame(hybrid_data)

# Save the hybrid strains DataFrame to a new CSV file
hybrid_df.to_csv('hybrid.csv', index=False)

print("Hybrid strains CSV created successfully!")
