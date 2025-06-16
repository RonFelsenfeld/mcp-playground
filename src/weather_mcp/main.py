from mcp.server.fastmcp import FastMCP

from src.weather_mcp.tools import get_weather_alerts, get_forecast

weather_mcp = FastMCP("weather")

weather_mcp.add_tool(get_weather_alerts)
weather_mcp.add_tool(get_forecast)

if __name__ == "__main__":
    weather_mcp.run(transport="stdio")
