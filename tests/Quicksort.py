import pandas as pd

import matplotlib.pyplot as plt

 

def quicksort(arr):

    if len(arr) <= 1:

        return arr

 

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

 

    return quicksort(left) + middle + quicksort(right)

 

def read_excel_file(file_path):

    try:

        # Read the Excel file using pandas

        df = pd.read_excel(file_path)

 

        # Extract data from column 'Price' and drop any rows with non-numeric values

        column_e = df['Price']

        column_e = column_e.apply(pd.to_numeric, errors='coerce').dropna()

 

        # Sort the data using quicksort

        data_column_e = column_e.tolist()

        data_column_e = quicksort(data_column_e)

 

        # Plot the sorted data

        plt.plot(data_column_e)

        plt.xlabel('Index')

        plt.ylabel('Price')

        plt.title('Sorted Diamond Prices')

        plt.show()

 

    except FileNotFoundError:

        print(f"File not found at path: {file_path}")

    except pd.errors.ParserError:

        print(f"Error parsing the file at path: {file_path}")

 
	
if __name__ == "__main__":

    file_path = r"C:\\Users\\sskis\\OneDrive\\Desktop\\Python stuff T3\\Python-T3\\DiamondValues(1000).xlsx"

    read_excel_file(file_path)

