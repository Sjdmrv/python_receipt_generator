import time
"""
below dictionaries are this apps local database
"""
product_names = {0: "Laptop", 1: "Tablet", 2: "cellPhone"}
product_price = {0: 50000000, 1: 20000000, 2: 35000000}
product_counts = {0: 10, 1: 8, 2: 5}


class Receipt:
    def __str__(self):
        return self.receipt_generator()

    def __init__(self, p_id, p_count):
        self.p_id = p_id
        self.chosen_count = p_count
        self.chosen_product = product_names[p_id]
        self.chosen_price = product_price[p_id]
        self.full_price = self.chosen_price * self.chosen_count
        self.tax_per_each = int(self.chosen_price * 0.09)
        self.total_tax = int(((self.chosen_price * self.chosen_count) * 0.09))
        self.final_price = self.full_price + self.total_tax

    def counter(self):
        product_counts[self.p_id] = product_counts[self.p_id] - self.chosen_count

    def sd(self, n):
        if n == 0:
            return format(self.chosen_price, ",")
        if n == 1:
            return format(self.full_price, ",")
        if n == 2:
            return format(self.tax_per_each, ",")
        if n == 3:
            return format(self.total_tax, ",")
        if n == 4:
            return format(self.final_price, ",")

    def receipt_generator(self) -> object:
        self.counter()
        print("")
        print(f"Your Receipt Date:{time.ctime()}")
        print("****************************        Purchased Item:         ************************************")
        print(f"Product Name: ({self.chosen_product})    **************** Count: ({self.chosen_count}) ")
        print(f"Price per each: ({self.sd(0)}) **************** Total price(NO TAX)): ({self.sd(1)}) ")
        print(f"TAX per each: ({self.sd(2)})    **************** Total Tax: ({self.sd(3)})")
        print("=")
        print(f"Final Price = ({self.sd(4)}) ")
        print("*************************                END             ***************************************")

# Test:


# first_receipt = Receipt(0, 2)
# first_receipt.receipt_generator()
