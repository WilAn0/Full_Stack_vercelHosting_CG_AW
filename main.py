from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import get_endpoints_Cameron, post_endpoints_Cameron, get_endpoints_Anton, post_endpoints_Anton

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=get_endpoints_Cameron.app)
app.include_router(router=post_endpoints_Cameron.app)
app.include_router(router=get_endpoints_Anton.app)
app.include_router(router=post_endpoints_Anton.app)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

