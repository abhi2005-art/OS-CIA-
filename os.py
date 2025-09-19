import time
import random
import threading

# Number of counters in the system
NUM_COUNTERS = 3  

# Lock for thread-safe operations
lock = threading.Lock()

# Counter status (True if free, False if busy)
counters = [True] * NUM_COUNTERS  

def serve_customer(customer_id):
    """
    Function to simulate serving a customer at a counter.
    """
    global counters
    assigned = False

    # Try to assign the customer to a free counter
    while not assigned:
        with lock:
            for i in range(NUM_COUNTERS):
                if counters[i]:  # Counter is free
                    counters[i] = False
                    print(f"Customer {customer_id} is being served at counter {i+1}")
                    assigned = True
                    # Simulate serving time
                    service_time = random.randint(2, 4)
                    time.sleep(service_time)
                    print(f"Customer {customer_id} finished checking out at counter {i+1}")
                    counters[i] = True  # Mark counter as free again
                    return

        # If no counter free, wait and retry
        print(f"Customer {customer_id} is waiting for a counter")
        time.sleep(1)


def main():
    """
    Main simulation of multiple customers arriving at counters.
    """
    num_customers = 5  # Example number of customers
    threads = []

    # Create a thread for each customer
    for customer_id in range(1, num_customers + 1):
        t = threading.Thread(target=serve_customer, args=(customer_id,))
        threads.append(t)
        t.start()
        time.sleep(random.randint(1, 2))  # Simulate random arrival times

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Simulation ended")


if __name__ == "__main__":
    main()
