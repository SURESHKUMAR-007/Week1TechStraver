# List operations
def list_operations():
    # Create a list
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)
    
    # Append to the list
    my_list.append(6)
    print("After Append:", my_list)
    
    # Reverse the list
    my_list.reverse()
    print("Reversed List:", my_list)
    
    # Delete the list
    del my_list
    print("List Deleted")

# Dictionary operations
def dictionary_operations():
    # Create a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original Dictionary:", my_dict)
    
    # Append to the dictionary
    my_dict['d'] = 4
    print("After Append:", my_dict)
    
    # Reverse the dictionary (this operation is not directly applicable, so we'll reverse the values)
    reversed_dict = {k: v for k, v in reversed(my_dict.items())}
    print("Reversed Dictionary:", reversed_dict)
    
    # Delete the dictionary
    del my_dict
    print("Dictionary Deleted")

# Set operations
def set_operations():
    # Create a set
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)
    
    # Append to the set
    my_set.add(6)
    print("After Append:", my_set)
    
    # Reverse the set (not directly applicable, converting to list and then reversing)
    reversed_set = set(list(my_set)[::-1])
    print("Reversed Set:", reversed_set)
    
    # Delete the set
    del my_set
    print("Set Deleted")

# Tuple operations
def tuple_operations():
    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Original Tuple:", my_tuple)
    
    # Append to the tuple (tuples are immutable, so create a new tuple)
    my_tuple = my_tuple + (6,)
    print("After Append:", my_tuple)
    
    # Reverse the tuple
    reversed_tuple = my_tuple[::-1]
    print("Reversed Tuple:", reversed_tuple)
    
    # Delete the tuple
    del my_tuple
    print("Tuple Deleted")

# Execute all operations
if __name__ == "__main__":
    list_operations()
    dictionary_operations()
    set_operations()
    tuple_operations()
