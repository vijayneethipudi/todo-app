import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from packages.routes.api import router as api_router

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,
    # allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app", host="127.0.0.1", port=8000, log_level="info", reload=True
    )
    print("running")
