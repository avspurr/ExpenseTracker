import pandas as pd
import os
from datetime import datetime

# Function to change negative values to positive in a column
def change_negative_to_positive(df, column):
    df[column] = df[column].abs()
    return df

# Function to combine CSV files in the directory by column name
def combine_csv_files(directory):
    # Get list of CSV files in directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    
    # Initialize an empty DataFrame to store combined data
    combined_df = pd.DataFrame()
    
    # Iterate over each CSV file
    for file in csv_files:
        # Read the CSV file
        df = pd.read_csv(os.path.join(directory, file))
        
        # Change negative values to positive in column C
        df = change_negative_to_positive(df, 'Amount')
        
        # Concatenate the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    return combined_df

# Function to output combined DataFrame to a CSV file named after current month and year
def output_combined_csv(combined_df):
    # Get current month and year
    current_month_year = datetime.now().strftime('%b_%Y')
    
    # Output combined DataFrame to CSV file
    combined_df.to_csv(f'{current_month_year}.csv', index=False)

# Main function
def main():
    # Directory containing CSV files
    directory = '/Users/andrewspurr/Library/Mobile Documents/com~apple~CloudDocs/Finance/March_24'
    
    # Combine CSV files
    combined_df = combine_csv_files(directory)
    
    # Output combined DataFrame to CSV file
    output_combined_csv(combined_df)

# Run the main function
if __name__ == "__main__":
    main()
