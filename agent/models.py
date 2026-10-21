from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# initializing the model connection
model = init_chat_model(
    model = "gpt-6-luna"
)

# testing the model connection
# response = model.invoke("What is the capital of india")
# print(response.content)

