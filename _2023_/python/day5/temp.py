import multiprocessing


def calculate_number(value):
    result = value * value
    return result


def worker_process(value, result_list):
    result = calculate_number(value)
    result_list.append(result)


if __name__ == "__main__":
    # Number of processes to create
    num_processes = 4

    # Values to be processed
    values_to_process = [1, 2, 3, 4, 5]

    # Shared list to store results
    manager = multiprocessing.Manager()
    result_list = manager.list()

    # Create a pool of worker processes
    with multiprocessing.Pool(num_processes) as pool:
        # Use starmap to pass multiple arguments to the worker function
        pool.starmap(worker_process, [(value, result_list)
                     for value in values_to_process])

    # Print the results
    print("Results:", result_list)
