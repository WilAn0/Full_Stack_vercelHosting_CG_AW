from pydantic import BaseModel


#Cameron
class Messageus(BaseModel):
    fullname: str
    emailaddress: str
    subject: str
    message: str


#Anton
class Subscription(BaseModel):
    eventName: str
    participantName: str
    participantFirstName: str
    eventWeek: int