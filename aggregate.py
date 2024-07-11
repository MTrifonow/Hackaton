def tuples_aggregate(tuple_list):

    result = {}

    for i, n in tuple_list:
        if i in result:
            result[i].append(n)
        else:
            result[i] = [n]
    return result

''' 
- Aggregates a list of 2 tuples into a dictionary where values with duplicate keys are grouped into a list.

- Dict: A dictionary where keys are extracted from the first element of each tuple in tuple_list.
Values associated with each key are aggregated into lists if duplicate keys are found.

'''

print(tuples_aggregate.__doc__)

tuples = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]

dict_aggregated = tuples_aggregate(tuples)

print(dict_aggregated)
