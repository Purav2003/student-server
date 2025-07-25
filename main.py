from fastapi import FastAPI
from config.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from controller import user_controller, student_controller, course_controller, result_controller, stats_controller
from middleware.auth_middleware import CustomMiddleware
# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.add(
    "logs/app.log",
    rotation="30 MB",           # Rotate logs when they reach 30 MB
    retention="30 days",        # Keep logs for 30 days
    compression="zip",          # Compress old log files
    level="INFO",               # Minimum log level
    format="{time} -  {level} - {message}"  # Log format    
)


@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Server is running"}

app.add_middleware(CustomMiddleware)


# Register routers
app.include_router(user_controller.user_router, prefix="/api/auth", tags=["user"])
app.include_router(student_controller.student_router, prefix="/api/students", tags=["students"])
app.include_router(course_controller.course_router, prefix="/api/courses", tags=["courses"])
app.include_router(result_controller.result_router, prefix="/api/results", tags=["results"])
app.include_router(stats_controller.stats_router, prefix="/api/stats", tags=["stats"])


@app.on_event("startup")
async def startup_event():
    print("App is starting.")

@app.on_event("shutdown")
async def shutdown_event():
    print("App is shutting down.")
