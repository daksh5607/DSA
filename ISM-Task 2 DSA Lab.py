#This provides a basic inventory management system. It defines two core functions: process_sale to handle sales and update stock quantities, and identify_zero_stock to find items that are out of stock. The code also includes a series of test cases to demonstrate and verify the functionality of these functions under different scenarios, such as normal sales, insufficient stock, and SKU not found errors
# Inventory Stock Manager with Test Cases

def process_sale(inventory, sku, qty_sold):
    """
    Process a sale by decreasing stock of a specific SKU.
    """
    updated_inventory = []
    sku_found = False

    for item in inventory:
        current_sku, current_qty = item

        if current_sku == sku:
            sku_found = True
            if current_qty >= qty_sold:
                updated_inventory.append((current_sku, current_qty - qty_sold))
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                updated_inventory.append((current_sku, current_qty))
                print(f"Insufficient stock for SKU {sku}. Available: {current_qty}")
        else:
            updated_inventory.append(item)

    if not sku_found:
        print(f"SKU {sku} not found in inventory.")

    return updated_inventory


def identify_zero_stock(inventory):
    """
    Identify all SKUs with zero stock.
    """
    zero_stock_list = [sku for sku, qty in inventory if qty == 0]

    if zero_stock_list:
        print(f"Zero stock SKUs: {zero_stock_list}")
    else:
        print("No zero stock items found.")

    return zero_stock_list


# --- Test Cases ---
if __name__ == "__main__":   # ✅ fixed here
    print("TC1 – Normal Sale")
    inventory = [(101, 50)]
    inventory = process_sale(inventory, 101, 30)
    print("Updated Inventory:", inventory, "\n")

    print("TC2 – Insufficient Stock")
    inventory = [(102, 20)]
    inventory = process_sale(inventory, 102, 25)
    print("Updated Inventory:", inventory, "\n")

    print("TC3 – SKU Not Found")
    inventory = [(101, 50)]
    inventory = process_sale(inventory, 104, 10)
    print("Updated Inventory:", inventory, "\n")

    print("TC4 – Zero Stock Detection")
    inventory = [(101, 0), (102, 5), (103, 0)]
    zero_stock_items = identify_zero_stock(inventory)
    print("Updated Inventory:", inventory, "\n")

    print("TC5 – No Zero Stock")
    inventory = [(101, 10), (102, 5)]
    zero_stock_items = identify_zero_stock(inventory)
    print("Updated Inventory:", inventory, "\n")

    print("TC6 – Sale Reducing to Zero")
    inventory = [(101, 10)]
    inventory = process_sale(inventory, 101, 10)
    print("Updated Inventory:", inventory, "\n")
