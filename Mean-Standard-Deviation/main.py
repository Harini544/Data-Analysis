import numpy as np

def convert_to_2d_array(flat_list, rows, cols):
    """Convert a flat list into a 2D array with the specified number of rows and columns."""
    if len(flat_list) != rows * cols:
        raise ValueError("List must contain nine numbers.")
    
    # Use list comprehension to create the 2D array
    return [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]

def calculate_statistics(flat_list, rows, cols):
    matrix = np.array(flat_list).reshape(rows, cols)
    
    # Compute row-wise statistics
    row_mean = np.mean(matrix, axis=1).tolist()
    row_variance = np.var(matrix, axis=1, ddof=0).tolist()
    row_std_dev = np.sqrt(row_variance).tolist()
    row_max = np.max(matrix, axis=1).tolist()
    row_min = np.min(matrix, axis=1).tolist()
    row_sum = np.sum(matrix, axis=1).tolist()

    # Compute column-wise statistics
    col_mean = np.mean(matrix, axis=0).tolist()
    col_variance = np.var(matrix, axis=0, ddof=0).tolist()
    col_std_dev = np.sqrt(col_variance).tolist()
    col_max = np.max(matrix, axis=0).tolist()
    col_min = np.min(matrix, axis=0).tolist()
    col_sum = np.sum(matrix, axis=0).tolist()

    # Compute overall statistics
    overall_mean = np.mean(matrix)
    overall_variance = np.var(matrix, ddof=0)
    overall_std_dev = np.sqrt(overall_variance)
    overall_max = np.max(matrix)
    overall_min = np.min(matrix)
    overall_sum = np.sum(matrix)

    # Format the result
    result = {
        'mean': [col_mean, row_mean, overall_mean],
        'variance': [col_variance, row_variance, overall_variance],
        'standard deviation': [col_std_dev, row_std_dev, overall_std_dev],
        'max': [col_max, row_max, overall_max],
        'min': [col_min, row_min, overall_min],
        'sum': [col_sum, row_sum, overall_sum]
    }
    
    return result

def main():
    l = []
    for i in range(9):
        l.append(int(input("enter a num:")))
    
    print("Flat list:", l)

    rows = 3
    cols = 3
    try:
        # Convert to 2D array
        matrix = convert_to_2d_array(l, rows, cols)
        print("2D matrix:")
        for row in matrix:
            print(row)
        
        # Calculate and print statistics
        stats = calculate_statistics(l, rows, cols)
        print("Statistics:")
        print(stats)

    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
