import asyncio
import os
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

os.chdir(os.path.dirname(os.path.abspath(__file__)))
async def main():
    bot = await Chatbot.create()
    print(await bot.ask(prompt="大阪府の人口について教えてください。", conversation_style=ConversationStyle.creative))
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())