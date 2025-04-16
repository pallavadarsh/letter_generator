from fastapi import FastAPI
from routers.letter_generator import router as letter_router
from routers.trace_router import router as trace_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trace_router)
app.include_router(letter_router)


