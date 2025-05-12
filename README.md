# mcp_agent_tutorial_project

A professional-development-day investigation.

_(2025-May-12-Monday)_


## preparatory research

Used chatgpt's deep-research for an overview of mcp/agent tutorials.

- [link](https://chatgpt.com/share/6821f6dd-bfcc-8006-98e2-8704797b796a) (took about 8-minutes)


## chosen tutorial

- "Model Context Protocol (MCP) using Ollama" (MCP Servers using Local LLMs tutorial) -- by Mehul Gupta _(Mar 29, 2025)_
- [link](https://medium.com/data-science-in-your-pocket/model-context-protocol-mcp-using-ollama-e719b2d9fd7a)


## setting up Ollama

I already have Ollama installed on my system.

```bash
% ollama --version
Warning: could not connect to a running Ollama instance
Warning: client version is 0.6.5
```

(I don't have the Ollama server running; not sure why the version also has a warning.)

### upgrading Ollama

I want to ensure I'm using a recent version of Ollama -- but how to upgrade depends on how I installed it (I don't remember).

```bash
% ls -l $(which ollama)
lrwxr-xr-x  1 root  wheel    50B May 21  2024 /usr/local/bin/ollama@ -> /Applications/Ollama.app/Contents/Resources/ollama
```

...shows that I installed it as an app. Downloading the newest version from the website...

Download link: <https://ollama.com/download>

```bash
% ollama --version
ollama version is 0.6.8
```

The deep-research document notes "...A 32 GB M1 can comfortably run 7B to 13B parameter models...", so I'll figure out how to specify the `7b` version of the `qwen2.5` model the tutorial recommends ([link](https://ollama.com/library/qwen2.5)). But I'll note that as of about a week ago, qwen3 came out, so I'll try that, eventually, too (note to self: the version I should be able to run is the `8b` version).

Ok, the command-pattern to load a model, specifying the size: `ollama pull qwen2.5:7b`.

Ok, it's installed:

```bash
% ollama list           
NAME                                                    ID              SIZE      MODIFIED      
qwen2.5:7b                                              845dbda0ea48    4.7 GB    5 seconds ago    
[snip] (other models listed)
```

### running the Ollama server

To see if it's running:

```bash
% curl 127.0.0.1:11434
curl: (7) Failed to connect to 127.0.0.1 port 11434 after 0 ms: Couldn't connect to server
```

To start it:

```bash
% ollama serve
```

...then:

```bash
% curl 127.0.0.1:11434
birkin@Brown-50021K9L ~ % curl 127.0.0.1:11434
Ollama is running
```

This will keep the ollama server running as long as the terminal session is open. 

To keep the server running in the background, use `ollama serve &` (lifetime of terminal session) or `nohup ollama serve &` (needs to be killed manually).

Note: running the ollama server doesn't automatically load a model. You can load a model persistently for an interactive chat session via:

```bash
% ollama run qwen2.5:7b
>>> Send a message (/? for help)
```

But that doesn't confirm that the model is running in the server. The only way to do that via the api is like:

```bash
% curl -X POST localhost:11434/api/generate -d '{"model":"qwen2.5:7b","prompt":"","stream":false}' | jq
{
  "model": "qwen2.5:7b",
  "created_at": "2025-05-12T16:15:37.730822Z",
  "response": "",
  "done": true,
  "done_reason": "load"
}
```

## Preparing the json-config file

The json-config file is a configuration file for the MCP server. It contains the following information:

- `globalShortcut`: the global shortcut to use to access the MCP server
- `mcpServers`: a list of MCP servers to use


---

