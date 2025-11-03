# Chapter03 Assignment

```bash
uv init --bare --python=3.13 .
uv add mcp[cli] fastmcp
```

Testing
```bash
npx @modelcontextprotocol/inspector --cli --method tools/list -- uv run mcp run server.py

npx @modelcontextprotocol/inspector --cli --method resources/templates/list -- uv run mcp run server.py
```
