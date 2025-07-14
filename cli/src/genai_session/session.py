from fastapi import FastAPI
import inspect
from pydantic import BaseModel
import asyncio

class GenAISession:
    def __init__(self, jwt_token=None):
        self.app = FastAPI()
        self.jwt_token = jwt_token
        self.bindings = {}

    def bind(self, name: str, description: str = ""):
        def decorator(fn):
            sig = inspect.signature(fn)
            self.bindings[name] = {
                "function": fn,
                "signature": sig,
                "description": description,
            }
            return fn
        return decorator

    async def process_events(self):
        print(" Agent is running... Waiting for input...")
        while True:
            await asyncio.sleep(1)
