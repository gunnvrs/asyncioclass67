import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
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
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
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

async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                    for the_id in range (customer_count, customer_count+customers)]
        for customer in customers:
            print("Waiting to put customer in line....")
            await queue.put (customer)
            print("Customer put in line...")
        customer_count = customer_count + len (customers)
        await asyncio.sleep(.001)

        return customer_count


async def main():
    customer_queue = Queue(3)
    customers_start_time = time.perf_counter()
    # Generate customers
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 10))
    # Create tasks for cashiers , track customer count
    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(5)]
    await asyncio.gather(customer_producer, *cashiers)

    print("------------------")

    # Sum the number of customers that checked out , time
    total_customers_checked_out = 0
    for cashier_number, cashier_task in enumerate(cashiers):
        customer_count, cashier_total_time = cashier_task.result()
        total_customers_checked_out += customer_count
        print(f"The Cashier_{cashier_number} take {customer_count} customers total {round(cashier_total_time, 2)} secs.")
    print(f"The supermarket process finished checking out {total_customers_checked_out} customers "
          f"in {round(time.perf_counter() - customers_start_time ,ndigits=2)} secs")

if __name__ == "__main__":
    asyncio.run(main())