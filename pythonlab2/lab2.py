#task1

def fill_and_sort_array():
    """Fill an array of 5 elements from the user, sort it in descending and ascending orders, then display the output."""
    array = []
    print("Enter 5 elements:")
    for _ in range(5):
        while True:
            try:
                element = int(input("Enter a number: "))
                array.append(element)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    ascending_sorted = sorted(array)
    descending_sorted = sorted(array, reverse=True)
    
    print("Original array:", array)
    print("Ascending order:", ascending_sorted)
    print("Descending order:", descending_sorted)


#task2

def generate_incremental_array(length, start):
    """
    Accepts two arguments (length, start) to generate an array of a specific length 
    filled with integer numbers increased by one from start.
    """
    array = [start + i for i in range(length)]
    return array


#task3

def calculate_numbers():
    """
    Repeatedly reads numbers until the user enters “done”. 
    Prints out the total, count, and average of the numbers.
    Detects non-number inputs and skips them.
    """
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number or 'done' to finish: ").strip().lower()
        if user_input == "done":
            break
        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

    if count > 0:
        average = total / count
    else:
        average = 0

    print("Total:", total)
    print("Count:", count)
    print("Average:", average)

#bonus

    # Discusses why dictionary keys can only be of an immutable type, 
    # why sets only accept immutable types, 
    # and how sets ensure they have no duplicates:

    # 1. Dictionary keys must be immutable:
    #    - Dictionaries in Python are implemented using hash tables. The key in a dictionary is used to compute a hash value, 
    #      which determines where the key-value pair should be stored.
    #    - If the key is mutable and its value changes, the hash value would change as well, making it impossible to retrieve 
    #      the original value using the key. This could corrupt the hash table.
    #    - Immutable types such as strings, numbers, and tuples ensure that the hash value remains constant throughout the 
    #      lifespan of the key, making the retrieval reliable.
    
    # 2. Sets only accept immutable types:
    #    - Like dictionary keys, elements in a set must be hashable to ensure that they can be checked efficiently for uniqueness. 
    #      Mutable types like lists and dictionaries cannot be reliably hashed because their contents can change, 
    #      which would change their hash value.
    #    - This property ensures that the elements of a set can be quickly compared for equality and stored/retrieved efficiently.

    # 3. Sets ensure non-duplicates:
    #    - Sets are implemented as hash tables. When a new element is added to a set, its hash value is computed. 
    #      The set checks if this hash value already exists. If it does, the element is considered a duplicate and is not added again.
    #    - This constant-time check (O(1) on average) ensures that all elements in the set are unique.
