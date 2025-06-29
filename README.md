# MCP Playground

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Technologies and Tools](#technologies-and-tools)
- [Local Installation Instructions](#local-installation-instructions)
- [Available Make Commands](#available-make-commands)
- [Connecting with Claude Desktop](#connecting-with-claude-desktop)

## Description

This project is a playground for MCP (Model Context Provider) implementations, featuring multiple microservices including a News MCP and Weather MCP. The services are implemented using MCP with stdio transport, providing a simple and efficient way to expose functionality through standard input/output streams.

## Requirements

- Python 3.12
- `uv` package manager
- Virtual environment support

## Technologies and Tools

- `mcp[cli]`: Model Context Provider for service communication
- `httpx`: Modern HTTP client for Python
- `python-dotenv`: Environment variable management

## Local Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/RonFelsenfeld/mcp-playground.git
cd mcp-playground
```

2. Set up the virtual environment and install dependencies:

```bash
make setup
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Sync dependencies:

```bash
make sync
```

5. Run the MCP services:

   - To run the News MCP service:

   ```bash
   python -m src.news_mcp.main
   ```

   - To run the Weather MCP service:

   ```bash
   python -m src.weather_mcp.main
   ```

## Available Make Commands

- `make setup`: Creates a new virtual environment
- `make activate`: Shows activation command for the virtual environment
- `make sync`: Syncs project dependencies
- `make freeze-dependencies`: Freezes current dependencies to requirements.txt
- `make clean`: Removes virtual environment and lock files

## Connecting with Claude Desktop

This project can be connected to Claude Desktop to test and interact with the MCP services using Anthropic's Model Context Protocol (MCP).

1. Install Claude Desktop, available [here](https://claude.ai/download)

2. Open Claude, go to Settings -> Developer
3. Click "Edit Config"
4. Open "claude_desktop_config.json" file
5. Copy-paste the following JSON inside the file:

```json
{
  "mcpServers": {
    "weather": {
      "command": "<ABSOLUTE_PATH_TO_UV>",
      "args": [
        "--directory",
        "<YOUR_PROJECT_PATH>",
        "run",
        "-m",
        "src.weather_mcp.main"
      ]
    },
    "news": {
      "command": "<ABSOLUTE_PATH_TO_UV>",
      "args": [
        "--directory",
        "<YOUR_PROJECT_PATH>",
        "run",
        "-m",
        "src.news_mcp.main"
      ],
      "env": {
        "NEWS_API_KEY": "<YOUR_NEWS_API_KEY>"
      }
    }
  }
}
```

Replace:

- `<ABSOLUTE_PATH_TO_UV>` with the absolute path to your `uv` executable (from the `which uv` command)
- `<YOUR_PROJECT_PATH>` with the absolute path to your project directory

For the News MCP service, you'll need a News API key from [newsdata.io](https://newsdata.io/). You can get a free API key by:

1. Creating an account at newsdata.io
2. Going to your dashboard
3. Generating a new API key

After generating you API key, replace `<YOUR_NEWS_API_KEY>` with it.
