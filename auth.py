# auth.py — Token management and verification

# In production this would be a real database
# Each token maps to a specific customer
TOKEN_DATABASE = {
    "tok_abc123": "cust_001",
    "tok_xyz789": "cust_002",
}

def resolve_customer(token: str) -> str | None:
    """
    Takes a token, returns the customer ID it belongs to.
    Returns None if the token is invalid.
    """
    return TOKEN_DATABASE.get(token)