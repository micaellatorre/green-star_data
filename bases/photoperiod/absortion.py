import pandas as pd

# Load the CSV file
df = pd.read_csv('hybrid_updated.csv')

# Dynamically get the max values for PPFD, PPFDwCO2, regCO2, and boostCO2 from the dataset
# max_ppfd = df['PPFD'].max()
max_ppfdwco2 = df['PPFDwCO2'].max()
# max_reg_co2 = df['regCO2'].max()
max_boost_co2 = df['boostCO2'].max()

# Function to calculate regAbsortion
def calculate_reg_absorption(ppfd, reg_co2):
    try:
        # Ensure PPFD and regCO2 values are valid
        if pd.notna(ppfd) and pd.notna(reg_co2):
            # Dynamically calculate absorption, capped at 100%
            absorption = (ppfd / max_ppfdwco2) * (reg_co2 / max_boost_co2) * 100
            return min(int(absorption), 100)  # Cast to int and ensure it doesn't exceed 100%
        else:
            return None
    except:
        return None

# Function to calculate boostAbsortion
def calculate_boost_absorption(ppfdw_co2, boost_co2):
    try:
        # Ensure PPFDwCO2 and boostCO2 values are valid
        if pd.notna(ppfdw_co2) and pd.notna(boost_co2):
            # Dynamically calculate absorption, capped at 100%
            absorption = (ppfdw_co2 / max_ppfdwco2) * (boost_co2 / max_boost_co2) * 100
            return min(int(absorption), 100)  # Cast to int and ensure it doesn't exceed 100%
        else:
            return None
    except:
        return None

# Apply the absorption calculations
df['regAbsortion'] = df.apply(lambda row: calculate_reg_absorption(row['PPFD'], row['regCO2']), axis=1)
df['boostAbsortion'] = df.apply(lambda row: calculate_boost_absorption(row['PPFDwCO2'], row['boostCO2']), axis=1)

# Save the updated CSV file
df.to_csv('hybrid_updated.csv', index=False)

print("auto.csv updated successfully with regAbsortion and boostAbsortion columns!")
