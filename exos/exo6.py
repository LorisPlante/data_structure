def find_largest_tuple(tuple_list):
    if not tuple_list:
        return None

    largest_tuple = max(tuple_list, key=len)
    return largest_tuple
