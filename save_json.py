"""
Loads the json template, and saves it to the outer 'stuff' directory, replacing paths with envars.

Usage: uv run --env-file "../.env" "./save_json.py"
"""

import json
import os

## load envars and raise error if not found -------------------------
DB_PATH = os.environ['DB_PATH']
OLLAMA_MCP_FILESYSTEM_PATH = os.environ['OLLAMA_MCP_FILESYSTEM_PATH']

## load json template -----------------------------------------------
with open('json_template.json', 'r') as f:
    template = json.load(f)

## replace paths with envars -----------------------------------------
template['mcpServers']['sqlite']['args'][2] = os.getenv('DB_PATH')
template['mcpServers']['filesystem']['args'][2] = os.getenv('OLLAMA_MCP_FILESYSTEM_PATH')

## save actual json-file --------------------------------------------
with open('../mcp_servers.json', 'w') as f:
    json.dump(template, f, indent=2)
