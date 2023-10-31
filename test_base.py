import json
import os
import pytest
from EdgeGPT.EdgeGPT import Chatbot
from EdgeGPT.EdgeGPT import ConversationStyle

os.chdir("C:\Users\misak\OneDrive\ドキュメント\大場")
pytest_plugins = ("pytest_asyncio",)

from os import getenv

print(os.getcwd())
@pytest.mark.asyncio()
async def test_ask() -> None:
    bot = await Chatbot.create(cookies=getenv("EDGE_COOKIES"))
    response = await bot.ask(
        prompt="東京都の人口を教えてください",
        conversation_style=ConversationStyle.creative,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response, indent=2))
    assert response
