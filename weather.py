from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather", stateless_http=True)

@mcp.tool()
def get_weather(city: str) -> str:
    return f"Weather in {city} is sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")