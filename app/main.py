from fastapi import FastAPI
from app.users.router import router as users_router
from app.messages.router import router as messages_router
from app.conversations.router import router as conversations_router
from app.contacts.router import router as contacts_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

# Include routers
app.include_router(users_router)
app.include_router(messages_router)
app.include_router(conversations_router)
app.include_router(contacts_router)