def queue_time(customers, n):
    if len(customers) == 1:
        return customers[0]
    elif not customers:
        return 0
    elif n == 1:
        return sum(customers)
    empty_check = [0 for x in range(n)]

    for customer in customers:
        min_val = min(empty_check)
        empty_check[empty_check.index(min_val)] += customer

    return max(empty_check)



