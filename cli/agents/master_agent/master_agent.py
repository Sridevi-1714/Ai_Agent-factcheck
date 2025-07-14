import sys
import os

sys.path.append("C:\\Users\\kosur\\genai-agentos\\cli\\src")

import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from genai_session.utils.agent_call import call_agent


import os
from dotenv import load_dotenv

load_dotenv()
AGENT_JWT = os.getenv("AGENT_JWT")
git commit -m "Initial commit of AIGent Fact-Checker project"

session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(
    name="master_agent",
    description="Routes statement through statement_checker and fact_source agents"
)
async def master_agent(
    agent_context: GenAIContext,
    statement: Annotated[
        str,
        "A statement that needs to be checked and potentially verified."
    ],
):
    # Step 1: Check the statement
    verdict = await call_agent(
        name="statement_checker_agent",
        input={"statement": statement}
    )

    # Step 2: If it's suspicious, get sources
    is_suspicious = "suspicious" in verdict.lower() or "X" in verdict

    if is_suspicious:
        sources = await call_agent(
            name="fact_source_agent",
            input={"statement": statement}
        )
        return {
            "verdict": verdict,
            "sources": sources
        }
    else:
        return {
            "verdict": verdict,
            "sources": "No fact-check sources needed"
        }
        

async def main():
    print("🔁 master_agent running...")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
