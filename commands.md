# Terminal Record: [Copper Kettle Coffee Roasters]

## 1. Building the projectpwd
mkdir ism3232-midterm
cd ~/ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install pytest ruff
pip freeze > requirements.txt
git init
git remote add origin [https://github.com/XOTICRIDA/ism3232-midterm.git](https://github.com/XOTICRIDA/ism3232-midterm.git)
touch business_rules.py main.py commands.md README.md .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
ruff format
ruff check

## 2. The virtual environment
/usr/bin/python3

## 3. The project structure
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_business_rules.py
## 4. Every function and test
business_rules.py
18:def calculate_bean_cost(bag_price: float, bags: int) -> float:
23:def get_bulk_discount(bags: int, partner: bool = False) -> float:
34:def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
44:def requires_prepayment(total: float) -> bool:
49:def needs_pallet(bags: int, total: float) -> bool:
54:def total_shipped(shipments: list) -> float:
63:def largest_shipment(shipments: list) -> str:
77:def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:

tests/test_business_rules.py
15:def test_calculate_bean_cost():
20:def test_get_bulk_discount_tier1_below_limit():
25:def test_get_bulk_discount_tier1_at_limit():
30:def test_get_bulk_discount_tier2_below_limit():
35:def test_get_bulk_discount_tier2_at_limit():
40:def test_get_bulk_discount_with_partner_changes_answer():
46:def test_calculate_shipment_total_fee_limit_below():
53:def test_calculate_shipment_total_fee_limit_at():
60:def test_requires_prepayment_at_limit():
65:def test_requires_prepayment_above_limit():
70:def test_needs_pallet_bag_limit_below():
76:def test_needs_pallet_bag_limit_at():
82:def test_needs_pallet_total_limit_below():
88:def test_needs_pallet_total_limit_above():
94:def test_total_shipped_with_short_list():
104:def test_largest_shipment_with_short_list():
112:def test_largest_shipment_tie_returns_first():
121:def test_largest_shipment_empty_list():
126:def test_format_shipment_line():
132:def test_calculate_shipment_total_partner_impact():
## 5. Which files print
main.py
## 6. The commit history
4dcc5df (HEAD -> main, origin/main, origin/HEAD) ism3232-midterm