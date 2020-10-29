# ----------------------------------
# Given a list of Integers, find the
# product of the three largest
# ----------------------------------


def highest_product_sum(integer_list):
    temp = list(integer_list)
    result = 1
    for i in range(3):
        result *= max(temp)
        temp.remove(max(temp))

    return result


print(highest_product_sum([1, 10, 2, 6, 5, 3]))
