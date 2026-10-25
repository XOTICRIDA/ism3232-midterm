shipments = [
    {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
    {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
    {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    {"buyer": "Zenith Grocers", "bag_price": 11.00, "bags": 200, "partner": False},
    {"buyer": "Alder Hotel", "bag_price": 12.00, "bags": 60, "partner": False},
    {"buyer": "Birch Diner", "bag_price": 11.00, "bags": 61, "partner": False},
    {"buyer": "Cove Market", "bag_price": 13.00, "bags": 150, "partner": True},
]

from business_rules import (calculate_shipment_total,requires_prepayment,needs_pallet,total_shipped,largest_shipment,format_shipment_line)

    # Print exact title line
print("Copper Kettle Coffee Roasters - Shipment Report")

    # Loop over the list and print one line for each shipment
for shipment in shipments:
        buyer = shipment["buyer"]
        bags = shipment["bags"]
        price = shipment["bag_price"]
        partner = shipment.get("partner", False)
        
        total = calculate_shipment_total(price, bags, partner)
        prepayment = requires_prepayment(total)
        pallet = needs_pallet(bags, total)
        
        print(format_shipment_line(buyer, total, prepayment, pallet))

    # Summary calculations using loops in main.py
num_shipments = 0
for _ in shipments:
        num_shipments += 1

revenue_total = total_shipped(shipments)
average_total = revenue_total / num_shipments if num_shipments > 0 else 0.0
top_buyer = largest_shipment(shipments)

prepayment_count = 0
for shipment in shipments:
        total = calculate_shipment_total(
            shipment["bag_price"], 
            shipment["bags"], 
            shipment.get("partner", False)
        )
        if requires_prepayment(total):
            prepayment_count += 1

pallet_count = 0
for shipment in shipments:
        total = calculate_shipment_total(
            shipment["bag_price"], 
            shipment["bags"], 
            shipment.get("partner", False)
        )
        if needs_pallet(shipment["bags"], total):
            pallet_count += 1

    # Print summary lines matching exact target output
print(f"Shipments: {num_shipments}")
print(f"Total shipped: ${revenue_total:.2f}")
print(f"Average shipment total: ${average_total:.2f}")
print(f"Largest shipment total: {top_buyer}")
print(f"Prepayments required: {prepayment_count}")
print(f"Pallets needed: {pallet_count}")

