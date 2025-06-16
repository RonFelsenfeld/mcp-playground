# MCP Playground

## Description

This project is a playground for MCP (Model Context Provider) implementations, featuring multiple microservices including a News MCP and Weather MCP. The services are implemented using MCP with stdio transport, providing a simple and efficient way to expose functionality through standard input/output streams.

## Requirements

- Python 3.12
- `uv` package manager
- Virtual environment support

## Technologies and Tools

- **MCP**: Model Context Provider for service communication
- **uv**: Fast Python package installer and resolver
- **Python-dotenv**: Environment variable management

## Local Installation Instructions

1. Clone the repository:

```bash
git clone <repository-url>
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

5. Run the services:
   - To run a specific MCP service:
   ```bash
   make run-file file=src/news_mcp/main.py
   ```
   - To run the server:
   ```bash
   make run-server
   ```

## Available Make Commands

- `make setup`: Creates a new virtual environment
- `make activate`: Shows activation command for the virtual environment
- `make sync`: Syncs project dependencies
- `make run-file`: Runs a specific Python file
- `make run-server`: Starts the server
- `make clean`: Removes virtual environment and lock files

## Project Structure

```
mcp-playground/
├── src/
│   ├── news_mcp/
│   └── weather_mcp/
├── Makefile
├── requirements.txt
└── README.md
```
