from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware

# from app.configs.Environment import get_environment_variables
from app.infra.controllers import leagues

# # Application Environment Configuration
# env = get_environment_variables()

# Core Application Instance
app = FastAPI()

# origins = [
#     "http://localhost:8000",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Add Routers
app.include_router(leagues.router, prefix="/api/v1", tags=["leagues"])


# Health
@app.get("/api/v1/health", tags=["health"])
async def root():
    return {"version": "v1"}
