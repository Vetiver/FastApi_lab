from fastapi import FastAPI
import pyjokes
import wikipedia
from pydantic import BaseModel

app = FastAPI()

class Joke(BaseModel):
    friend: str
    joke: str

class JokeInput(BaseModel):
    friend: str


@app.get("/")
def joke():
    return pyjokes.get_joke() 


@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " " 
    return result

@app.post("/model", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke()) 




@app.get("/wiki")
def get_summary():
    return wikipedia.search("Bill", results=2)

