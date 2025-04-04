from PayoffTuple import PayoffTuple
from merge_sort import merge_sort

def process_matrices(matrix1, matrix2, sort_function=merge_sort):
    # Constructing normal_form
    normal_form = [
        [
            PayoffTuple(matrix1[i][j], matrix2[i][j])
            for j in range(len(matrix1[0]))
        ]
        for i in range(len(matrix1))
    ]

    # Flattening the normal_form matrix
    payoff_tuples = [item for row in normal_form for item in row]

    try:
        sorted_payoff_tuples, comparisons = sort_function(payoff_tuples)
        return f"Game is strictly competitive! ({comparisons} comparisons)", sorted_payoff_tuples
    except ValueError as e:
        return f"Game is not strictly competitive! \n{e}", None

# For testing
# if __name__ == "__main__":
#     utility_matrix1 = [[0, -4], [4, 0], [4, 0]]
#     utility_matrix2 = [[2, 3], [1, 2], [1, 2]]
    
#     result, sorted_payoff_tuples = process_matrices(utility_matrix1, utility_matrix2)
#     print(result)
#     if sorted_payoff_tuples:
#         print(sorted_payoff_tuples)