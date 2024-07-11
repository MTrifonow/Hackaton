def aggregate_dict_to_list(tuple_list):

    result = {}

    for i, n in tuple_list:
        if i not in result:
            result[i] = []
        result[i].append(n)
    return result

'''
- Aggregates a list of tuples into a dictionary where values are preserved in lists for each key.
- A list of tuples where each tuple contains a text-number pair.
- Return: A dictionary where text is extracted from the first element of each tuple in tuple_list.
Numbers associated with each text are aggregated into lists.

'''

input_tuples = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]

output_dict = aggregate_dict_to_list(input_tuples)

print(output_dict)
