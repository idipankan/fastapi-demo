from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/hello-world")
async def root():
    return {"message": "Hello World"}
