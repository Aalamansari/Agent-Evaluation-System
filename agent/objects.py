from pydantic import BaseModel, Field

class ResponseModel(BaseModel):
    response: str = Field(description="response given by the model for the user's question")
    conversationYn:bool = Field(description="indicator to check if the conservation has to be continued or not. if the agent has made the decision about refund then this should be made False." \
                                             "if the conservation still need more discussion then this will be True", 
                                default=True)

class PurchaseItemModel(BaseModel):
    name:str = Field(description="name of the item purchased")