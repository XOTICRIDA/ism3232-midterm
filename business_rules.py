# business_rules.py
# Author: [River Sookralli]


FLAT_SHIPPING_FEE = 35.00
SHIPPING_COST_THRESHOLD = 250.00

DISCOUNT_TIER_LOW = 0.09
DISCOUNT_TIER_HIGH = 0.14
PARTNER_BONUS = 0.04
MIN_PARTNER_BAGS = 20

PREPAYMENT_THRESHOLD = 1500.00
PALLET_BAG_THRESHOLD = 60
PALLET_TOTAL_THRESHOLD = 700.00


def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Return the bean cost before any discount (rule 1)."""
    return bag_price * bags


def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate as a decimal (rules 2 and 3)."""
    discount = 0.0
    if bags >= 80:
        discount = DISCOUNT_TIER_HIGH
    elif bags >= 20:
        discount = DISCOUNT_TIER_LOW

    if partner and bags >= MIN_PARTNER_BAGS:
        discount += PARTNER_BONUS

    return round(discount, 2)


def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """Return the shipment total including discounted cost and shipping fee when applicable (rule 4)."""
    base_cost = calculate_bean_cost(bag_price, bags)
    discount_rate = get_bulk_discount(bags, partner)
    discounted_cost = base_cost * (1.0 - discount_rate)

    shipping_fee = FLAT_SHIPPING_FEE if discounted_cost < SHIPPING_COST_THRESHOLD else 0.0

    return round(discounted_cost + shipping_fee, 2)


def requires_prepayment(total: float) -> bool:
    """Return True when the shipment total requires prepayment (rule 5), otherwise False."""
    return total >= PREPAYMENT_THRESHOLD


def needs_pallet(bags: int, total: float) -> bool:
    """Return True when the shipment needs a freight pallet (rule 6), otherwise False."""
    return bags > PALLET_BAG_THRESHOLD and total > PALLET_TOTAL_THRESHOLD


def total_shipped(shipments: list) -> float:
    """Return the sum of the shipment totals for every shipment in the list using a for loop."""
    total = 0.0
    for shipment in shipments:
        total += calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
    return round(total, 2)


def largest_shipment(shipments: list) -> str:
    """Return the buyer of the shipment with the largest shipment total using a for loop."""
    if not shipments:
        return ""

    largest_buyer = ""
    max_total = -1.0
    for shipment in shipments:
        current_total = calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
        if current_total > max_total:
            max_total = current_total
            largest_buyer = shipment["buyer"]
    return largest_buyer


def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    """Return one formatted line of the report."""
    pre_str = "yes" if prepayment else "no"
    pal_str = "yes" if pallet else "no"
    return f"{buyer}: ${total:.2f} | prepayment: {pre_str} | pallet: {pal_str}"