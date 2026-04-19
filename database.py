# Simulated database — in production this would be real SQL queries

CUSTOMERS = {
    "cust_001": {
        "name": "Paws & Claws Vet Clinic",
        "gl_data": {
            "4000": {"name": "Revenue - Consultations", "balance": 125000.00},
            "4100": {"name": "Revenue - Surgery", "balance": 89000.00},
            "6000": {"name": "Salaries", "balance": 74000.00},
            "6200": {"name": "Medical Supplies", "balance": 31000.00},
        }
    },
    "cust_002": {
        "name": "Happy Pets Hospital",
        "gl_data": {
            "4000": {"name": "Revenue - Consultations", "balance": 210000.00},
            "4100": {"name": "Revenue - Surgery", "balance": 145000.00},
            "6000": {"name": "Salaries", "balance": 98000.00},
            "6200": {"name": "Medical Supplies", "balance": 52000.00},
        }
    },
}

def get_customer_gl(customer_id: str, code: str) -> dict | None:
    customer = CUSTOMERS.get(customer_id)
    if not customer:
        return None
    return customer["gl_data"].get(code)

def get_all_customer_gl(customer_id: str) -> dict | None:
    customer = CUSTOMERS.get(customer_id)
    if not customer:
        return None
    return customer["gl_data"]