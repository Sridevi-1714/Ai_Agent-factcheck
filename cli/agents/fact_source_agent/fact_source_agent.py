import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

import os
AGENT_JWT = os.getenv("AGENT_JWT")

session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(
    name="fact_source_agent",
    description="Returns trusted sources for verifying a statement"
)
async def fact_source_agent(
    agent_context: GenAIContext,
    statement: Annotated[str, "A statement to find fact sources for."]
):
    text = statement.lower()
    if "moon" in text:
        return [
            "https://www.nasa.gov/mission_pages/apollo/missions/index.html",
            "https://en.wikipedia.org/wiki/Moon_landing"
        ]
    elif "flat earth" in text:
        return [
            "https://en.wikipedia.org/wiki/Flat_Earth",
            "https://www.britannica.com/science/Earth/Shape-of-the-Earth"
        ]
    else:
        return ["https://en.wikipedia.org/wiki/Factual_accuracy"]

async def main():
    print("fact_source_agent running...")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
