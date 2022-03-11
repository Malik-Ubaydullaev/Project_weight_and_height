import csv

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    result_data = []
    reader = ''
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result_data.append(row)
    
   # print(result_data)
    # WRITE YOUR CODE HERE
    return result_data

file_path = 'data/weight-height.csv'
read_csv_data(file_path)