def sum_tuples(tuple1, tuple2):

    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be the same length")
    
    result = tuple(tuple1[i] + tuple2[i] for i in range(len(tuple1)))
    return result

'''
- A new tuple that is the result of addition of two input tuples.
- Raises ValueError: If tuples tuple1 and tuple2 are not of the same length.
- A new tuple where each element is the sum of corresponding numbers from tuple1 and tuple2.

'''

tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

result_tuple = sum_tuples(tuple1, tuple2)

print(result_tuple)
