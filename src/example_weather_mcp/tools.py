from configs.logger_config import app_logger

from src.example_weather_mcp.constants import NWS_API_BASE, FORMAT_SEPARATOR
from src.example_weather_mcp.helpers import (
    make_nws_request,
    format_alert,
    format_forecast,
)


async def get_weather_alerts(state: str) -> str:
    """
    Get weather alerts for a given US state.

    Args:
      state: Two-letter US state code (e.g. CA, NY)

    Returns:
      str: A string containing the weather alerts for the given state.
    """

    app_logger.info(f"MCP SERVER: Getting weather alerts for {state}")

    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch weather alerts for the given state or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    app_logger.info(f"MCP SERVER: Found {len(alerts)} alerts")

    return FORMAT_SEPARATOR.join(alerts)


async def get_forecast(latitude: float, longitude: float) -> str:
    """
    Get the forecast for a given latitude and longitude.

    Args:
      latitude: The latitude of the location.
      longitude: The longitude of the location.

    Returns:
      str: A string containing the forecast for the given latitude and longitude.
    """

    app_logger.info(f"MCP SERVER: Getting forecast for {latitude}, {longitude}")

    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    periods = forecast_data["properties"]["periods"]
    forecasts = [format_forecast(period) for period in periods[:5]]

    app_logger.info(f"MCP SERVER: Found {len(forecasts)} forecasts")

    return FORMAT_SEPARATOR.join(forecasts)
