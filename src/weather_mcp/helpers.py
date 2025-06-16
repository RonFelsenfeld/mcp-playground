import httpx
from typing import Any

from configs.logger_config import app_logger

from src.weather_mcp.constants import USER_AGENT


async def make_nws_request(url: str) -> dict[str, Any] | None:
    """
    Make a request to the NWS API with proper error handling.

    Args:
        url (str): The URL to make the request to.

    Returns:
        dict[str, Any]: The response from the NWS API.
    """

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            app_logger.error(f"Error making request to {url}: {str(e)}")
            return None


def format_alert(feature: dict) -> str:
    """
    Format an alert feature into a readable string.

    Args:
        feature (dict): The alert feature to format.

    Returns:
        str: The formatted alert string.
    """

    props = feature["properties"]
    return f"""
    Event: {props.get('event', 'Unknown')}
    Area: {props.get('areaDesc', 'Unknown')}
    Severity: {props.get('severity', 'Unknown')}
    Description: {props.get('description', 'No description available')}
    Instructions: {props.get('instruction', 'No specific instructions provided')}
    """


def format_forecast(period: dict) -> str:
    """
    Format a forecast period into a readable string.

    Args:
        period (dict): The forecast period to format.

    Returns:
        str: The formatted forecast string.
    """

    forecast = f"""
        {period['name']}:
        Temperature: {period['temperature']}°{period['temperatureUnit']}
        Wind: {period['windSpeed']} {period['windDirection']}
        Forecast: {period['detailedForecast']}
        """

    return forecast
