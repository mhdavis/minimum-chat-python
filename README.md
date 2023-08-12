# minimum-chat-python
## Introduction
Minimum Chat (Python) is a chat application project I'm developing to learn the basics of:
- Python, specifically creating REST APIs in a Python ecosystem
- Learning Flask
- Learning the basics of implementing a socket

## Setup

To install project package dependencies run:
```
pip install -r requirements.txt
```

## Database Migration

In order to update the database (postgres) tables for the app, we use Flask-Migrate to capture changes to the database schemas.

To capture updates for schemas based on changes made to models in the application we can run the following commands:

Creates the migration script
```
flask db migrate -m "Description of the changes made"
```

Applies migration script changes to the actual database
```
flask db upgrade
```

Optionally, if we need to downgrade the migration script to an earlier version, we can do so with the following command:
```
flask db downgrade
```