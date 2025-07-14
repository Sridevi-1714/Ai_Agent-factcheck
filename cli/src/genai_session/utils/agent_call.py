async def call_agent(name: str, input: dict):
    print(f"[Mock] Calling agent '{name}' with input: {input}")

    if name == "statement_checker_agent":
        statement = input.get("statement", "")
        if "flat" in statement.lower() or "moon landing" in statement.lower():
            return " This statement is suspicious"
        else:
            return " Statement looks fine"

    elif name == "fact_source_agent":
        return [
            "https://en.wikipedia.org/wiki/Earth",
            "https://www.nasa.gov/moon",
            "https://www.britannica.com/topic/moon-landing"
        ]

    return " Unknown agent"
