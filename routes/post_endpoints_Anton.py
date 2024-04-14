from fastapi import APIRouter
import database
from models import models
from queries import tartare as queries

app = APIRouter()


@app.post("/subscription")
def create_subscription(subscription: models.Subscription):
    query = queries.insert_subscription_query
    success = database.execute_sql_query(query, (
        subscription.eventName,
        subscription.participantName,
        subscription.participantFirstName,
        subscription.eventWeek
    ))
    if success:
        return subscription