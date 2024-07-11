def delete_subtuple(large_tuple, subtuple):

    index = -1

    for i in range(len(large_tuple) - len(subtuple) + 1):
        if large_tuple[i:i+len(subtuple)] == subtuple:
            index = i
            break
    

    if index != -1:
        result_list = list(large_tuple)
        result_list = result_list[:index] + result_list[index+len(subtuple):]
        return tuple(result_list)
    else:
        return large_tuple

'''
- Deletes the first occurrence of a subtuple from a larger tuple, if found.
- Return a new tuple from removing the first occurrence of subtuple from large_tuple,
or returns large_tuple unchanged if subtuple is not found.

'''

large_tuple = (1, 2, 3, 4, 5)

subtuple = (3, 4)

result_tuple1 = delete_subtuple(large_tuple, subtuple)

print(result_tuple1)

subtuple2 = (6, 7)

result_tuple2 = delete_subtuple(large_tuple, subtuple2)

print(result_tuple2)

