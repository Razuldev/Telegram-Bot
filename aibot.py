from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessage

client = OpenAI(
    api_key="add your token here",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = (
    """
    write about yourself
    """
)

async def replyToUser(message: str) -> ChatCompletionMessage:
    response = client.chat.completions.create(
        model="gemini-2.0-flash-exp",
        n=1,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message





