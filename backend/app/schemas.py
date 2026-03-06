# schemas.py
# this file defines the structure of data that our api expects and returns
# fastapi uses these models to validate requests and format responses

from pydantic import BaseModel


# this model defines what the frontend must send when asking a question
# it expects a json body with a single field called "question"
class AskRequest(BaseModel):
    question: str


# this model defines the shape of the response our backend will return
# the frontend will receive an "answer" string from the api
class AskResponse(BaseModel):
    answer: str
