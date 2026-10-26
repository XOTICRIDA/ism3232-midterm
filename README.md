# ism3232-midterm: Copper Kettle Coffee Roasters

Name: River Sookralli

Version: 1.0.0

Date: October 25, 2026

What This Program Does
This program automates the generation of coffee bean shipment reports and logistics summaries for Copper Kettle Coffee Roasters. It calculates base bean costs, applies volume and partner discount tiers, determines shipping fees, and evaluates prepayment and pallet requirements for wholesale buyers. Finally, it compiles a clean terminal report with aggregate statistics including total shipments, average cost, prepayment counts, and pallet requirements.

Business Rules
(Rule 1): Bean Cost: The base cost is calculated by multiplying the price per bag by the number of bags ordered.

(Rule 2): Volume Discounts: Discounts depend on quantity: no discount for fewer than 20 bags, 9% for 20 through 79 bags, and 14% for 80 bags or more.

(Rule 3): Partner Bonus: Partner cafes receive an extra 4 percentage points of discount (raising 9% to 13% and 14% to 18%) on shipments of 20 bags or more.

(Rule 4): Shipping Fees: A flat $35.00 shipping fee is added when the discounted bean cost falls below $250.00.

(Rule 5): Prepayment: A shipment total of $1,500.00 or more requires advance prepayment.

(Rule 6): Freight Pallets: A shipment requires a freight pallet only when it has more than 60 bags and its shipment total exceeds $700.00.

How to Run:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

How to Test:
ruff check .
pytest -v

AI Use Statement:
No AI was used to complete this project. Only to answer problems that helped make the code work, no copy and paste AI. 