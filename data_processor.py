import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Load the dataset
def load_data(file_path, file_delimiter='\t'):
    """Load the dataset from a CSV file."""
    try:
        return pd.read_csv(file_path, delimiter=file_delimiter, engine='python')
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None


# Step 2: Calculate summary statistics
def calculate_statistics(dataset):
    """Calculate and print summary statistics for numerical columns."""
    print("Summary Statistics:")
    print(dataset.describe())


# Step 3: Filter the data
def filter_data(dataset, column_name, threshold):
    """Filter the dataset based on a specified threshold for a given column."""
    if column_name not in dataset.columns:
        print(f"Error: Column '{column_name}' not found in dataset.")
        return dataset  # Return original data if column doesn't exist
    return dataset[dataset[column_name] > threshold]


# Step 4: Generate visualizations
def generate_visualizations(filtered_data, hist_column, scatter_x, scatter_y):
    """Generate and display visualizations."""
    plt.figure(figsize=(10, 5))

    # Histogram for the specified column
    if hist_column in filtered_data.columns:
        plt.subplot(1, 2, 1)
        plt.hist(filtered_data[hist_column], bins=10, color='blue', edgecolor="red", alpha=0.8)
        plt.title(f'Histogram of {hist_column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
    else:
        print(f"Column '{hist_column}' not found for histogram.")

    # Scatter plot for specified x and y columns
    if scatter_x in filtered_data.columns and scatter_y in filtered_data.columns:
        plt.subplot(1, 2, 2)
        plt.scatter(filtered_data[scatter_x], filtered_data[scatter_y], color='orange', edgecolor='red', alpha=0.7)
        plt.title(f'Scatter Plot of {scatter_x} vs {scatter_y}')
        plt.xlabel(scatter_x)
        plt.ylabel(scatter_y)
    else:
        print(f"Columns '{scatter_x}' and/or '{scatter_y}' not found for scatter plot.")

    plt.tight_layout()
    plt.show()


# Step 5: Save processed data
def save_processed_data(processed_data, output_file):
    """Save the processed DataFrame to a new CSV file."""
    processed_data.to_csv(output_file, index=False)
    print(f'Processed data saved to {output_file}')


# Main function to execute the script
if __name__ == "__main__":
    # Ask the user for file paths and column information
    input_file_path = input("Enter the path to the CSV file: ")
    output_file_path = input("Enter the name of the output CSV file: ")
    file_Delimiter = input("Enter the delimiter used in the file (default is tab '\\t'): ") or '\t'

    # Load the dataset
    Dataset = load_data(input_file_path, file_Delimiter)

    if Dataset is not None:
        # Calculate and display summary statistics
        calculate_statistics(Dataset)

        # Ask for the column to filter and the threshold value
        filter_column = input("Enter the column name to filter by: ")
        threshold_value = float(input(f"Enter the threshold value for {filter_column}: "))

        # Filter the dataset
        filtered_dataset = filter_data(Dataset, filter_column, threshold_value)

        # Ask for the column names for histogram and scatter plot
        hist_columN = input("Enter the column name for histogram visualization: ")
        scatter_X = input("Enter the column name for the scatter plot (X-axis): ")
        scatter_Y = input("Enter the column name for the scatter plot (Y-axis): ")

        # Generate visualizations
        generate_visualizations(filtered_dataset, hist_columN, scatter_X, scatter_Y)

        # Save the processed data to a new CSV file
        save_processed_data(filtered_dataset, output_file_path)
