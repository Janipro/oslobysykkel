# -----------------------------------------------
# Given a list of integers, returns the highest
# product between three of those numbers.
# For example, given the list [1, 10, 2, 6, 5, 3]
# the highest product would be 10 * 6 * 5 = 300
# -----------------------------------------------


def highest_product_sum(integer_list):
    temp = list(integer_list)
    result = 1
    negatives = 0
    choices = []

    if len(temp) < 3:
        return

    for i in range(3):
        max_element = max(temp)
        min_element = min(temp)
        if abs(max_element) < abs(min_element):
            result *= min(temp)
            choices.append(min(temp))
            temp.remove(min(temp))
        else:
            result *= max(temp)
            choices.append(max(temp))
            temp.remove(max(temp))

    for number in choices:
        if number < 0:
            negatives += 1

    if negatives % 2 != 0:
        return

    return result
