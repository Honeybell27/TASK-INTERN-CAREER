# Data Processing Script

## Overview
  This Python script is designed to load a dataset from a CSV file, calculate summary statistics, filter the data based on
  user-defined criteria, generate visualizations, and save the processed data to a new CSV file. It utilizes the _'pandas'_
  library for data manipulation and _'matplotlib'_ for visualizations.
  

## Features
- Load datasets with customizable delimiters.
- Calculate and display summary statistics for numerical columns.
- Filter data based on specified thresholds.
- Generate histograms and scatter plots for data visualizaton.
- Save Proceesed data to a new CSV file.

## Requirements
 To run this script, you need to have Python installed along with the following libraries:
 - _'pandas'_
 - _'matplotlib'_

 You can install the required libraries using pip:
  `pip install pandas matplotlib`

## Usage
1. **Run the Script:**Execute the script in your terminal or command prompt.
   `python [name_of_your_script].py`

2. **Input Prompts:**The script will prompt you to enter:
  - The path to the CSV file you want to process.
  - The name of the output CSV file where processed data will be saved.
  - The delimiter used in the input file(default is tab '\t').
  - The column name you want to filter by and the threshold value.
  - Column names for histogram and scatter plot visualizations.

3. **Output:**The processed data will be saved to the specified output file, and visualizations will be diplayed.

# Code Structure

 ## Functions
- 'load_data(file_path', file_delimiter='\t')': Loads the dataset from a CSV file.
- 'calculate_statistics(dataset)': Calculates and prints summary statistics for numerical columns.
- 'filter_data(dataset, column_name, threshold)': Filters the dataset based on a specified threshold for a given column.
- 'generate_visualizations(filtered_data, hist_column, scatter_x, scatter_y)': Generates and displays visualizations(histogram and scatter plot).
- 'save_processed_data(processed_data, output_file)': Saves the processed DataFrame to a new CSV file.

## Example Dataset
 The script is designed to work with numerical datasets. Ensure that your dataset has the appropraite numerical columns for analysis.

## Conclusion
 The script provides an efficient way to process and visualize data from CSV files. It is suitable for various apllications in data analysis and can be adapted for different datasets.
 
## Author
 Aduge Honeybell Akpesiri