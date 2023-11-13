import os
import asyncio
from EdgeGPT.EdgeGPT import Chatbot,ConversationStyle

async def main():
    bot = await Chatbot.create()
    print(await bot.ask(
        prompt="大阪府の人口について教えてください。",conversation_style=ConversationStyle.creative,)
    )
    await bot.close()

if __name__ =="__main__":
    asyncio.run(main())