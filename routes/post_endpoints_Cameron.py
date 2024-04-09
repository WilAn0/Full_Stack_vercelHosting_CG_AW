from fastapi import APIRouter
import database
from models import models
from queries import tartare as queries

app = APIRouter()


@app.post("/messageus")
def create_message(messageus: models.Messageus):
    query = queries.insert_message_query
    success = database.execute_sql_query(query,
                                        (
                                            messageus.fullname,
                                            messageus.emailaddress,
                                            messageus.subject,
                                            messageus.message
                                        ))
    if success:
        return messageus