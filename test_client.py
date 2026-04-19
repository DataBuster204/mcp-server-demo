import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_server():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("--- Valid token: Customer 001 ---")
            result = await session.call_tool(
                "get_financial_summary",
                {"token": "tok_abc123"}
            )
            print(result.content[0].text)

            print("\n--- Valid token: Customer 002 ---")
            result = await session.call_tool(
                "get_financial_summary",
                {"token": "tok_xyz789"}
            )
            print(result.content[0].text)

            print("\n--- Invalid token: Should be rejected ---")
            result = await session.call_tool(
                "get_financial_summary",
                {"token": "tok_HACKER"}
            )
            print(result.content[0].text)

asyncio.run(test_server())