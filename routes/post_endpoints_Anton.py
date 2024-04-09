from fastapi import APIRouter
import database
from models import models
from queries import tartare as queries

app = APIRouter()

@app.post("/subscription")
def create_subscription(subscription: models.Subscription):
     return subscription