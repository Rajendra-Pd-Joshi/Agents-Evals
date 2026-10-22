from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model(model = "gpt-6-luna")

# response = model.invoke(input = "write a short notes on importance of reranker in rag chatbots")
# print(response.content)