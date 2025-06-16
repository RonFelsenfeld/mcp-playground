from mcp.server.fastmcp import FastMCP

from src.weather_mcp.tools import get_weather_alerts, get_forecast

mcp = FastMCP("weather")

# Weather tools
mcp.add_tool(get_weather_alerts)
mcp.add_tool(get_forecast)

if __name__ == "__main__":
    mcp.run(transport="stdio")
