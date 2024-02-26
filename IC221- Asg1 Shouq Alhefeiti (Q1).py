class Chocolate:
    def __init__(self, weight, price, type):
        # Initialize a Chocolate object with weight, price, and type attributes
        self.weight = weight
        self.price = price
        self.type = type

    def __str__(self):
        # String representation of Chocolate object
        return f"Chocolate(type='{self.type}', weight={self.weight}, price={self.price})"

def compare_chocolates(chocolate):
    # Comparison function for sorting chocolates by price
    return chocolate.price

def merge_sort(arr):
    """Merge sort algorithm to sort chocolates based on price."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if compare_chocolates(left[left_index]) < compare_chocolates(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def distribute_chocolates_iterative(chocolates, students):
    """Distribute chocolates to students iteratively."""
    # Sort chocolates based on price using merge sort
    chocolates_sorted = merge_sort(chocolates)

    # Create an empty dictionary to store distribution of chocolates to students
    distribution = {}

    # Iterate over each student and assign them a chocolate
    for i in range(len(students)):
        if i < len(chocolates_sorted):
            distribution[students[i]] = chocolates_sorted[i]
        else:
            break

    return distribution

def distribute_chocolates_recursive(chocolates, students):
    """Distribute chocolates to students recursively."""
    # if no chocolates or no students, return empty distribution
    if not chocolates or not students:
        return {}

    # Sort chocolates based on price using merge sort
    chocolates_sorted = merge_sort(chocolates)

    # Create an empty dictionary to store distribution of chocolates to students
    distribution = {}

    # Assign chocolates to students
    for student, chocolate in zip(students, chocolates_sorted):
        distribution[student] = chocolate

    return distribution

# Additional test cases

# 1. Empty Input
chocolates_empty = []
students_empty = []

# 2. Single Chocolate and Single Student
chocolates_single = [Chocolate(10, 5, 'dark')]
students_single = ['Shouq']

# 3. Equal Number of Chocolates and Students
chocolates_equal = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white')]
students_equal = ['Shouq', 'Alya', 'Abdullah']

# 4. Unequal Number of Chocolates and Students
chocolates_unequal = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk')]
students_unequal = ['Shouq', 'Alya', 'Abdullah']

# 5. Identical Chocolates
chocolates_identical = [Chocolate(10, 5, 'dark'), Chocolate(15, 5, 'milk'), Chocolate(8, 5, 'white')]
students_identical = ['Shouq', 'Alya', 'Abdullah']

# 6. Identical Students
chocolates_identical_students = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white')]
students_identical_students = ['Shouq', 'Shouq', 'Shouq']

# Test each case
test_cases = [
    ("Single Chocolate and Single Student", chocolates_single, students_single),
    ("Equal Number of Chocolates and Students", chocolates_equal, students_equal),
    ("Unequal Number of Chocolates and Students", chocolates_unequal, students_unequal),
    ("Identical Chocolates", chocolates_identical, students_identical),
    ("Identical Students", chocolates_identical_students, students_identical_students)
]

for test_name, chocolates, students in test_cases:
    print(f"\nTest Case: {test_name}")
    # Iterative distribution
    distribution_iterative = distribute_chocolates_iterative(chocolates, students)
    print("Iterative distribution:")
    for student, chocolate in distribution_iterative.items():
        print(f"{student}: {chocolate}")

    # Recursive distribution
    distribution_recursive = distribute_chocolates_recursive(chocolates, students)
    print("\nRecursive distribution:")
    for student, chocolate in distribution_recursive.items():
        print(f"{student}: {chocolate}")
