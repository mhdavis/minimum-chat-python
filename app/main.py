from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users.router import router as users_router
from app.contacts.router import router as contacts_router
from app.conversations.router import router as conversations_router
from app.messages.router import router as messages_router
from app.usergroups.router import router as usergroups_router

app = FastAPI(
    title="Minimum Chat App API",
    description="API for a minimum chat application that supports user managemnt and messaging.",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users_router, prefix="/api", tags=["Users"])
app.include_router(contacts_router, prefix="/api", tags=["Contacts"])
app.include_router(conversations_router, prefix="/api", tags=["Conversations"])
app.include_router(messages_router, prefix="/api", tags=["Messages"])
app.include_router(usergroups_router, prefix="/api", tags=["User Groups"])

@app.get("/")
def root():
    return {"message": "Endpoint hit Successfully"}