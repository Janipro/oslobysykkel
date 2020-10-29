# -----------------------------------------------
# Given a list of integers, returns the highest
# product between three of those numbers.
# For example, given the list [1, 10, 2, 6, 5, 3]
# the highest product would be 10 * 6 * 5 = 300
# -----------------------------------------------


def highest_product_sum(integer_list):
    temp = list(integer_list)
    result = 1
    for i in range(3):
        result *= max(temp)
        temp.remove(max(temp))

    return result

