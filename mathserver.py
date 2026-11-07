from mcp.server.fastmcp import FastMCP
import sys

# IMPORTANT: never print() to stdout — it corrupts the JSON-RPC stream.
# Use sys.stderr for any debug output.
print("MATH SERVER: starting", file=sys.stderr)

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


if __name__ == "__main__":
    # MUST be stdio — this is what the client speaks
    mcp.run(transport="stdio")