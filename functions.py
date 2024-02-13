def load_warehouse(warehouse_file_path):
    warehouse = {}
    with open(warehouse_file_path) as f:
        for row in f:
            product_name, quantity = row.strip().split(":")

            if product_name and quantity in warehouse:
                print(f"Warning: Duplicate value of {product_name}")

            warehouse[product_name] = {
                "product": product_name,
                "quantity": quantity,
            }
        return warehouse


def save_library(warehouse, product_name, quantity, warehouse_file_path):
    with open(warehouse_file_path, "w") as f:
        for product_name, quantity in warehouse.items():
            f.write("{}:{}\n".format(product_name["product_name"], quantity["quantity"]))
