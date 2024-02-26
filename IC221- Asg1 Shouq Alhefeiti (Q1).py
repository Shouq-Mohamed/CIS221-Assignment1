class Chocolate:
    def __init__(self, weight, price, type):
        # Define a class to represent Chocolate objects with weight, price, and type attributes
        self.weight = weight  # Initialize weight attribute
        self.price = price    # Initialize price attribute
        self.type = type      # Initialize type attribute

    def __str__(self):
        # Define string representation of Chocolate object
        return f"Chocolate(type='{self.type}', weight={self.weight}, price={self.price})"

def compare_chocolates(chocolate):
    # Define a comparison function for sorting chocolates by price
    return chocolate.price  # Return price attribute of the chocolate

def merge_sort(arr):
    """Merge sort algorithm to sort chocolates based on price."""
    # Define a function to sort chocolates based on price using merge sort
    if len(arr) <= 1:
        return arr  # if the array has 0 or 1 element, it is already sorted

    mid = len(arr) // 2  # Calculate the middle index of the array
    left_half = merge_sort(arr[:mid])  # Recursively sort left half of the array
    right_half = merge_sort(arr[mid:])  # Recursively sort right half of the array

    return merge(left_half, right_half)  # Merge sorted halves

def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    # Define a function to merge two sorted lists into one sorted list
    merged = []  # Initialize an empty list to store merged elements
    left_index = right_index = 0  # Initialize index variables for left and right lists

    while left_index < len(left) and right_index < len(right):
        # Merge elements from left and right lists in sorted order
        if compare_chocolates(left[left_index]) < compare_chocolates(right[right_index]):
            merged.append(left[left_index])  # Append element from left list to merged list
            left_index += 1  # Move to the next element in the left list
        else:
            merged.append(right[right_index])  # Append element from right list to merged list
            right_index += 1  # Move to the next element in the right list

    merged.extend(left[left_index:])  # Add remaining elements from left list to merged list
    merged.extend(right[right_index:])  # Add remaining elements from right list to merged list

    return merged  # Return the merged list

def distribute_chocolates_iterative(chocolates, students):
    """Distribute chocolates to students iteratively."""
    chocolates_sorted = merge_sort(chocolates)  # Sort chocolates based on price using merge sort
    distribution = {}  # Initialize an empty dictionary to store distribution of chocolates to students

    for i in range(len(students)):
        # Iterate over each student and assign them a chocolate
        if i < len(chocolates_sorted):
            distribution[students[i]] = chocolates_sorted[i]  # Assign chocolate to the student
        else:
            break  # Stop assigning chocolates if there are no more chocolates to distribute

    return distribution  # Return the distribution dictionary

def distribute_chocolates_recursive(chocolates, students):
    """Distribute chocolates to students recursively."""
    if not chocolates or not students:
        #if there are no chocolates or no students, return an empty distribution
        return {}

    chocolates_sorted = merge_sort(chocolates)  # Sort chocolates based on price using merge sort
    distribution = {}  # Initialize an empty dictionary to store distribution of chocolates to students

    for student, chocolate in zip(students, chocolates_sorted):
        # Assign chocolates to students
        distribution[student] = chocolate  # Assign chocolate to the student

    return distribution  # Return the distribution dictionary


# Define test cases with different scenarios
chocolates_empty = []  # Define empty list of chocolates
students_empty = []  # Define empty list of students

chocolates_single = [Chocolate(10, 5, 'dark')]  # Define list with a single Chocolate object
students_single = ['Shouq']  # Define list with a single student name

chocolates_equal = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white')]  # Define list with multiple Chocolate objects
students_equal = ['Shouq', 'Alya', 'Abdullah']  # Define list with multiple student names

chocolates_unequal = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk')]  # Define list with unequal number of Chocolate objects
students_unequal = ['Shouq', 'Alya', 'Abdullah']  # Define list with multiple student names

chocolates_identical = [Chocolate(10, 5, 'dark'), Chocolate(15, 5, 'milk'), Chocolate(8, 5, 'white')]  # Define list with identical priced Chocolate objects
students_identical = ['Shouq', 'Alya', 'Abdullah']  # Define list with multiple student names

chocolates_identical_students = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white')]  # Define list with multiple Chocolate objects
students_identical_students = ['Shouq', 'Shouq', 'Shouq']  # Define list with identical student names

test_cases = [
    ("Single Chocolate and Single Student", chocolates_single, students_single),
    ("Equal Number of Chocolates and Students", chocolates_equal, students_equal),
    ("Unequal Number of Chocolates and Students", chocolates_unequal, students_unequal),
    ("Identical Chocolates", chocolates_identical, students_identical),
    ("Identical Students", chocolates_identical_students, students_identical_students)
]


# Test cases
for test_name, chocolates, students in test_cases:
    print(f"\nTest Case: {test_name}")
    distribution_iterative = distribute_chocolates_iterative(chocolates, students)  # Iterative distribution
    print("Iterative distribution:")
    for student, chocolate in distribution_iterative.items():
        print(f"{student}: {chocolate}")

    distribution_recursive = distribute_chocolates_recursive(chocolates, students)  # Recursive distribution
    print("\nRecursive distribution:")
    for student, chocolate in distribution_recursive.items():
        print(f"{student}: {chocolate}")
