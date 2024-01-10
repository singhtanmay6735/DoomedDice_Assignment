def total_combinations(die_a, die_b):
    """
    Calculate the total number of combinations when two dice are thrown together.
    """
    return len(die_a) * len(die_b)

def display_combinations(die_a, die_b):
    """
    Generate and return all possible combinations when two dice are thrown together.
    """
    number_faces_die_a = len(die_a)
    number_faces_die_b = len(die_b)

    combinations = [[(i, j) for j in range(1, number_faces_die_b + 1)] for i in range(1, number_faces_die_a + 1)]
    return combinations

def calculate_probabilities(die_a, die_b):
    """
    Calculate and print the probabilities of all possible sums when two dice are thrown together.
    """
    total_outcomes = len(die_a) * len(die_b)
    probabilities = {}

    for outcome in range(2, 13):
        count = sum(1 for face_a in die_a for face_b in die_b if face_a + face_b == outcome)
        probability = count / total_outcomes
        probabilities[outcome] = probability

    for key, val in probabilities.items():
        print(f'P(Sum = {key}) = {round(val, 4)}')

# Initial dice
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

# Function calls
total_combinations_number = total_combinations(die_a, die_b)
print(f'The total possible combinations are: {total_combinations_number}\n')

total_combinations_matrix = display_combinations(die_a, die_b)
print('The combination matrix is given by:')
print(total_combinations_matrix, '\n')

print('The probabilities of all possible sums occurring among the number of combinations are:')
calculate_probabilities(die_a, die_b)
