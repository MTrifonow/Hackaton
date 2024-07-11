def min_tuples_aggregate(tuple_list):

    result = {}

    for i, value in tuple_list:
        if i in result:
            result[i] = min(result[i], value)
        else:
            result[i] = value
    return result

'''
- Aggregates a list of tuples into a dictionary where values with duplicate keys
are aggregated by taking the minimum value for each key.

- A list of 2 tuples where each tuple contains a key-value pair.

- Return: A dictionary where keys are extracted from the first element of each tuple in tuple_list.
Values associated with each key are aggregated by taking the minimum value if duplicate keys are found.

'''

tuples = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 1)]

dict_aggregated = min_tuples_aggregate(tuples)

print(dict_aggregated)
