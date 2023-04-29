from fastapi import FastAPI

api = FastAPI()


@api.get("//")
def create_board():
    return ["lista", "das", "bananas"]
