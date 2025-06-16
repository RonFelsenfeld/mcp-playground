from mcp.server.fastmcp import FastMCP

from src.news_mcp.tools import get_latest_news

news_mcp = FastMCP("news")

news_mcp.add_tool(get_latest_news)

if __name__ == "__main__":
    news_mcp.run(transport="stdio")
