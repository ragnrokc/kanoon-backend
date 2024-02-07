from fastapi import APIRouter


root = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    },
)


@root.get("/")
async def hello():
    return {"message": "Welcome to Kanoon LLM!"}
