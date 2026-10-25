import pytest
from business_rules import (calculate_bean_cost,get_bulk_discount,calculate_shipment_total,requires_prepayment,needs_pallet,total_shipped,largest_shipment,format_shipment_line,)

def test_calculate_bean_cost():
    """Test basic bean cost calculation."""
    assert calculate_bean_cost(10.00, 5) == 50.00


def test_get_bulk_discount_tier1_below_limit():
    """Test bulk discount just below the first tier limit (49 bags vs 50 limit)."""
    assert get_bulk_discount(49, partner=False) == 0.10


def test_get_bulk_discount_tier1_at_limit():
    """Test bulk discount exactly at the first tier limit (50 bags)."""
    assert get_bulk_discount(50, partner=False) == 0.15


def test_get_bulk_discount_tier2_below_limit():
    """Test bulk discount just below the second tier limit (99 bags vs 100 limit)."""
    assert get_bulk_discount(99, partner=False) == 0.15


def test_get_bulk_discount_tier2_at_limit():
    """Test bulk discount exactly at the second tier limit (100 bags)."""
    assert get_bulk_discount(100, partner=False) == 0.20


def test_get_bulk_discount_with_partner_changes_answer():
    """Test that passing partner=True increases the discount rate."""
    base_discount = get_bulk_discount(20, partner=False)
    partner_discount = get_bulk_discount(20, partner=True)
    assert partner_discount == base_discount + 0.05


def test_calculate_shipment_total_fee_limit_below():
    """Test shipment total calculation just below the shipping fee limit (29 bags vs 30 limit)."""
    # 29 bags < 30 triggers flat fee $35.00, discount tier 1 (10%)
    expected = round((10.00 * 29) * 0.90 + 35.00, 2)
    assert calculate_shipment_total(10.00, 29, partner=False) == expected


def test_calculate_shipment_total_fee_limit_at():
    """Test shipment total calculation exactly at the shipping fee limit (30 bags)."""
    # 30 bags >= 30 triggers 1% shipping fee instead of flat fee, discount tier 1 (10%)
    expected = round((10.00 * 30) * 0.90 + (10.00 * 30) * 0.01, 2)
    assert calculate_shipment_total(10.00, 30, partner=False) == expected


def test_requires_prepayment_at_limit():
    """Test prepayment requirement exactly at the limit ($1500.00 -> False)."""
    assert requires_prepayment(1500.00) is False


def test_requires_prepayment_above_limit():
    """Test prepayment requirement just above the limit ($1500.01 -> True)."""
    assert requires_prepayment(1500.01) is True


def test_needs_pallet_bag_limit_below():
    """Test pallet requirement just below the bag limit (149 bags with low total -> False)."""
    # Other condition (total) is set low so bags decide the outcome
    assert needs_pallet(bags=149, total=500.00) is False


def test_needs_pallet_bag_limit_at():
    """Test pallet requirement exactly at the bag limit (150 bags with low total -> True)."""
    # Other condition (total) is set low so bags decide the outcome
    assert needs_pallet(bags=150, total=500.00) is True


def test_needs_pallet_total_limit_below():
    """Test pallet requirement at/below the total limit ($1500.00 with low bags -> False)."""
    # Other condition (bags) is set low so total decides the outcome
    assert needs_pallet(bags=10, total=1500.00) is False


def test_needs_pallet_total_limit_above():
    """Test pallet requirement just above the total limit ($1500.01 with low bags -> True)."""
    # Other condition (bags) is set low so total decides the outcome
    assert needs_pallet(bags=10, total=1500.01) is True


def test_total_shipped_with_short_list():
    """Test total_shipped with a custom short list of shipments."""
    sample_shipments = [
        {"buyer": "Shop A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "Shop B", "bag_price": 20.00, "bags": 5, "partner": False},
    ]
    total_a = calculate_shipment_total(10.00, 10, False)
    total_b = calculate_shipment_total(20.00, 5, False)
    expected = round(total_a + total_b, 2)
    assert total_shipped(sample_shipments) == expected


def test_largest_shipment_with_short_list():
    """Test largest_shipment returns the correct buyer from a short list."""
    sample_shipments = [
        {"buyer": "Small Shop", "bag_price": 10.00, "bags": 5, "partner": False},
        {"buyer": "Big Shop", "bag_price": 15.00, "bags": 100, "partner": False},
    ]
    assert largest_shipment(sample_shipments) == "Big Shop"


def test_largest_shipment_tie_returns_first():
    """Test largest_shipment tie-breaker returns the buyer that appears first in the list."""
    sample_shipments = [
        {"buyer": "First Shop", "bag_price": 10.00, "bags": 100, "partner": False},
        {"buyer": "Second Shop", "bag_price": 10.00, "bags": 100, "partner": False},
    ]
    assert largest_shipment(sample_shipments) == "First Shop"


def test_largest_shipment_empty_list():
    """Test largest_shipment returns an empty string when given an empty list."""
    assert largest_shipment([]) == ""


def test_format_shipment_line():
    """Test format_shipment_line returns the properly formatted string."""
    line = format_shipment_line("Uptown Bakery", 175.00, prepayment=False, pallet=False)
    assert line == "Uptown Bakery: $175.00 | prepayment: no | pallet: no"


def test_calculate_shipment_total_partner_impact():
    """Test that setting partner=True alters the calculated shipment total."""
    total_regular = calculate_shipment_total(12.00, 50, partner=False)
    total_partner = calculate_shipment_total(12.00, 50, partner=True)
    assert total_partner < total_regular
