from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "test 1"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "test 2"}

    return {"model_name": model_name, "message": "test 3"}
