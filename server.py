from mcp.server.fastmcp import FastMCP
from pydantic import Field
from typing import Annotated
from database import get_customer_gl, get_all_customer_gl
from auth import resolve_customer

mcp = FastMCP("Veterinary GL Server")

@mcp.tool()
def lookup_gl_code(
    token: Annotated[str, Field(description="Your API token e.g. tok_abc123")],
    code: Annotated[str, Field(description="The GL account code e.g. 4000")]
) -> str:
    """Look up a specific GL account code and balance. Requires a valid API token."""
    customer_id = resolve_customer(token)
    if not customer_id:
        return "Unauthorised — invalid or expired token."
    result = get_customer_gl(customer_id, code)
    if result:
        return f"GL {code} — {result['name']}: ${result['balance']:,.2f}"
    return f"GL code {code} not found."

@mcp.tool()
def get_financial_summary(
    token: Annotated[str, Field(description="Your API token e.g. tok_abc123")]
) -> str:
    """Get a full financial summary for the authenticated customer."""
    customer_id = resolve_customer(token)
    if not customer_id:
        return "Unauthorised — invalid or expired token."
    data = get_all_customer_gl(customer_id)
    if not data:
        return "No financial data found."
    lines = [f"Financial Summary — {customer_id}:"]
    for code, info in data.items():
        lines.append(f"  GL {code} — {info['name']}: ${info['balance']:,.2f}")
    return "\n".join(lines)

if __name__ == "__main__":
    mcp.run()