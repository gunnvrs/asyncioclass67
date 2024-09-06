import time
import asyncio
from asyncio import Queue

# The Product class represents products that need to be checked out.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    customer_count = 0
    cashier_start_time = time.perf_counter()  
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_count += 1 
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} "
              f"will checkout Customer_{customer.customer_id}")
        for product in customer.products:
            if cashier_number == 2:
                checkout_time = 0.1  # Use fixed checkout time for cashier 2
            else:
                checkout_time = product.checkout_time * (1 + 0.1 * cashier_number)  # Apply multiplier for other cashiers
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {checkout_time} secs")
            await asyncio.sleep(checkout_time)
        print(f"The Cashier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id} "
              f"in {round(time.perf_counter() - customer_start_time ,ndigits=2)} secs")
        
        queue.task_done()
    cashier_total_time = time.perf_counter() - cashier_start_time  # Total time cashier took
    return customer_count, cashier_total_time  # Return customer count and total time

def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, total_customers: int):
    customer_count = 0
    while customer_count < total_customers:
        new_customers = [generate_customer(customer_count + i)
                        for i in range(total_customers - customer_count)]
        for customer in new_customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            print("Customer put in line...")
        customer_count += len(new_customers)
        await asyncio.sleep(.001)

async def main():
    QUEUE = 10
    CUSTOMER = 10
    CASHIER = 5
    customer_queue = Queue(QUEUE)
    customers_start_time = time.perf_counter()
    # Generate customers
    customer_producer = asyncio.create_task(customer_generation(customer_queue, CUSTOMER))
    # Create tasks for cashiers, track customer count
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(CASHIER)]
    await asyncio.gather(customer_producer, *cashiers)

    print("------------------")

    # Sum the number of customers that checked out, time
    total_customers_checked_out = 0
    for cashier_number, cashier_task in enumerate(cashiers):
        customer_count, cashier_total_time = await cashier_task
        total_customers_checked_out += customer_count
        print(f"The Cashier_{cashier_number} took {customer_count} customers in total {round(cashier_total_time, 2)} secs.")
    print(f"The supermarket process finished checking out {total_customers_checked_out} customers "
          f"in {round(time.perf_counter() - customers_start_time ,ndigits=2)} secs")

if __name__ == "__main__":
    asyncio.run(main())
