from openai import OpenAI

api_key = "weeewewdedwedwedwd10ythg"
base_url = "http://192.168.2.167:10005/v1"

model = "/hy-tmp/hz/models-hub/Qwen3-30B-A3B-FP8"

client = OpenAI(api_key=api_key, base_url=base_url)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁"},
]
async def main():

    kwargs = {}


    response = client.chat.completions.create(
                    model=model, messages=messages, **kwargs
                )
    print(f"response: {response}")

import asyncio

asyncio.get_event_loop().run_until_complete(main())