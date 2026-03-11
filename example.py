from shekel import budget
from langchain.chat_models import ChatOpenAI

# Enforce a daily budget on LangChain
budget_ctx = budget(max_usd=5.0)

llm = ChatOpenAI(model="gpt-4o-mini")

with budget_ctx:
    response = llm.invoke("Explain general relativity")

print(response)