from FastApi import FASTAPI
from FastApi.middleware.cors import CORSMiddleware
from app.config import ALLOWED_ORIGINS
from app.routes.analyze import router as analyze_router

app = FASTAPI(
    title="ClearCall API",
    description="Resume vs Job Description Explanability Engine",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allowed_orgins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)

@app.get("/")
def health_check():
    return {
        "message" : "ClearCall API runnning.",
        "status" : "healthy",
    }