

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os

API_KEY = os.getenv("API_KEY")

def blog_generator_app(topic: str):
    llm = ChatGroq(
        api_key = API_KEY,
        model = "openai/gpt-oss-120b",
        temperature= 0.7
    )

    response = llm.invoke([
        SystemMessage(content = "Write a blog with: Title, Introduction, 3 sections, Conclusion"),
        HumanMessage(content=f"Write a blog on {topic}")
    ])

    return response.content


if __name__ == "__main__":

    while True:
        topic = input("Enter blog topic: :")
        if topic.lower() in ["exit", "quit"]:
            break

        reply = blog_generator_app(topic)
        print("AI:", reply)



