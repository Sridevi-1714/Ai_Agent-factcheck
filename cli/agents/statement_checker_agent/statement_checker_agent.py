import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
import os
from dotenv import load_dotenv

load_dotenv()
AGENT_JWT = os.getenv("AGENT_JWT")
session = GenAISession(jwt_token=AGENT_JWT)

# ✅ Agent binding: sets up this function as your agent
@session.bind(
    name="statement_checker_agent",
    description="Checks if a statement is likely false or suspicious"
)
async def statement_checker_agent(
    agent_context: GenAIContext,
    statement: Annotated[
        str,
        "A statement that may or may not be factual.",
    ],
):
    """Main agent function: detects if the input statement sounds suspicious."""

    suspicious_keywords = [
        "always", "never", "everyone says", "nobody", "flat earth", "moon landing was fake",
        "vaccines cause", "aliens built", "fake news", "hoax", "earth is flat", "5g causes", 
        "climate change is a lie", "covid is a hoax", "chemtrails"
    ]

    text = statement.lower()
    for keyword in suspicious_keywords:
        if keyword in text:
            return "❌ This statement might be suspicious or needs verification."

    return "✅ This statement appears okay, but still verify with trusted sources."

# ✅ Agent entry point
async def main():
    print(f"statement_checker_agent running...")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
