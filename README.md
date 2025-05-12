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
