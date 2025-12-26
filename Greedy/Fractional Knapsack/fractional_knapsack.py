def fractional_knapsack(weights, values, capacity):
    """
    Solve the fractional knapsack problem using a greedy approach.

    Parameters:
    weights (list of float): The weights of the items.
    values (list of float): The values of the items.
    capacity (float): The maximum weight capacity of the knapsack.

    Returns:
    float: The maximum value that can be carried in the knapsack.
    """

    # Calculate value to weight ratio for each item
    # using a comprehension as we are transforming. [Learn here: https://realpython.com/python-for-loop/#using-for-loops-vs-comprehensions]
    # zip function is normal zip function which merges two lists into list of tuples.
    ratio = [(v / w, w, v) for w, v in zip(weights, values)]
    # Now sort. You maybe asked to not use inbuilt sort.
    # No matter what you use the time complexity would be O(n log n) always; I find merge sort easy to remember.
    # Here lambda is idenity of first element of tuple to the sort function as a comparator, lambda is nothing but a closure in swift.
    # refer about lambda here: https://realpython.com/python-lambda/
    # here reverse is true to sort in descending order.
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0  # Total value accumulated in the knapsack
    currentCapacity = capacity
    
    for r, w, v in ratio:
        if w <= currentCapacity:
            # If the item can be fully added
            total_value += v
            currentCapacity -= w
        else:
            # If only part of the item can be added
            total_value += r * currentCapacity
            break
    return total_value


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # Output: 240