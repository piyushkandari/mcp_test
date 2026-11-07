from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
import sys

# Absolute paths remove all ambiguity about cwd and interpreter
MATH_SERVER = os.path.abspath("mathserver.py")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": sys.executable,   # same venv python as this client
                "args": [MATH_SERVER],       # absolute path
                "transport": "stdio",
            },
            # weather disabled until math works:
            # "weather": {
            #     "url": "http://127.0.0.1:8000/mcp",
            #     "transport": "streamable_http",
            #     "sse_read_timeout": 10,
            # },
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")

    print("Connecting to MCP servers...", flush=True)
    try:
        # Timeout so a broken server gives an error instead of a silent hang
        tools = await asyncio.wait_for(client.get_tools(), timeout=20)
    except asyncio.TimeoutError:
        print("❌ get_tools() timed out — the math subprocess is not responding.")
        print("   Check: does `python mathserver.py` hang silently (good) or crash (bad)?")
        return

    print(f"✅ Loaded {len(tools)} tool(s): {[t.name for t in tools]}", flush=True)

    model = ChatGroq(model="openai/gpt-oss-120b")

    # langgraph's create_react_agent binds tools itself; passing the raw model is correct.
    agent = create_react_agent(model, tools)

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    print("Math response:", response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())