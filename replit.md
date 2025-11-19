# Email Genius

## Overview
Email Genius is a GPT-powered web application that generates professional cold emails and replies based on user-provided context. The app uses OpenAI's latest GPT-5 model to create compelling, well-structured emails tailored to different tones and purposes.

## Features
- Form interface for inputting email context (job role, purpose, tone, recipient)
- GPT-5 powered email generation
- Multiple tone options (Professional, Casual, Friendly, Formal)
- Copy to clipboard functionality
- Download generated emails as text files
- Clean, responsive Bootstrap 5 interface

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap 5, Vanilla JavaScript
- **AI**: OpenAI GPT-5 API via Replit OpenAI integration
- **Deployment**: Replit

## Project Structure
```
.
├── app.py                 # Flask application and API endpoints
├── templates/
│   └── index.html        # Main UI with form and email display
├── static/               # Static assets (if needed)
├── .gitignore           # Python ignore patterns
└── replit.md            # This file
```

## Environment Variables
- `OPENAI_API_KEY`: Required for OpenAI API access (managed via Replit integration)

## Recent Changes
- 2025-11-19: Initial project setup with Flask, OpenAI integration, and Bootstrap UI

## User Preferences
- None documented yet

## Architecture Notes
- Uses Flask for simple web server and API endpoints
- OpenAI integration handles API key management securely
- Single-page application with AJAX calls for email generation
- GPT-5 model used for email generation (latest OpenAI model as of August 2025)
