import json

import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from os import getenv

async def main():
    bot = await Chatbot.create(cookies=getenv("EDGE_COOKIES"))
    print(await bot.ask(
        prompt="大阪府の人口について教えてください。",
        conversation_style=ConversationStyle.creative,
        simplify_response=True,))
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())