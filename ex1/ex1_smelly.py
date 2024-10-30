class OrderProcessor:
    # sample order: order = {"items": [{"id": 1, "name": "Widget", "price": 20.0, "quantity": 2}]}

    def process_order(self, order):
        # Step 1: Validate order details
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")
    
    def calculate_total_price(self, order):
        # Step 2: Calculate total price
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]

    def apply_discount(self,order):
        # Step 3: Apply discounts if applicable
        discount_code = {
            "SUMMER20": 0.8,
            "WELCOME10": 0.9
        }
        if order.get('discount_code') in discount_code:
            discount_code['discount_code']

        # Step 4: Update inventory
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

        # Step 5: Generate receipt
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"

        # Step 6: Send confirmation email
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

        return receipt

