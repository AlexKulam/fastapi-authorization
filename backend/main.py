from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.log_in import router as log_in_router
from backend.sign_up import router as sign_up_router
from backend.data_base import Base, engine
from backend.admin_panel import router as admin_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(log_in_router)
app.include_router(sign_up_router)
app.include_router(admin_router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
