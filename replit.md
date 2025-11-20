# Email Genius

## Overview
Email Genius is a Gemini-powered web application that generates professional cold emails and automatically finds hiring managers at tech companies. The app uses Google's latest Gemini 2.5 model to create compelling, well-structured emails tailored to different tones and purposes, plus an AI-powered contact finder to discover potential recipients.

## Features
- **Contact Finder**: Automatically find hiring managers (Staff Engineers, HR Leaders, VPs) at big tech companies or SF-based startups
- **Smart Email Generation**: Gemini 2.5-powered email creation with customizable tone
- **One-Click Workflow**: Click a found contact to auto-populate email form with personalized context
- Multiple tone options (Professional, Casual, Friendly, Formal)
- Copy to clipboard functionality
- Download generated emails as text files
- Clean, responsive Bootstrap 5 interface with tabbed navigation

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap 5, Vanilla JavaScript
- **AI**: Google Gemini 2.5 Flash/Pro via Replit Gemini integration
- **Deployment**: Replit

## Project Structure
```
.
├── app.py                 # Flask application and API endpoints
├── templates/
│   └── index.html        # Main UI with contact finder and email form
├── static/               # Static assets (if needed)
├── .gitignore           # Python ignore patterns
└── replit.md            # This file
```

## API Endpoints
- `GET /`: Main application interface
- `POST /find-contacts`: Find hiring managers based on company type, location, and role
- `POST /generate-email`: Generate personalized cold email using Gemini AI

## Environment Variables
- `GEMINI_API_KEY`: Required for Google Gemini API access (managed via Replit integration)

## Recent Changes
- 2025-11-20: Switched from OpenAI to Google Gemini
- 2025-11-20: Added contact finder feature for discovering hiring managers
- 2025-11-20: Enhanced UI with tabbed navigation and contact selection
- 2025-11-19: Initial project setup with Flask and Bootstrap UI

## User Preferences
- Prefers Google Gemini over OpenAI
- Wants automatic contact discovery for hiring managers at tech companies
- Target contacts: Staff Engineers, HR Leaders at big tech or SF startups

## Architecture Notes
- Uses Flask for simple web server and API endpoints
- Gemini integration handles API key management securely
- Single-page application with AJAX calls for contact finding and email generation
- Gemini 2.5 Flash model used for email generation and contact suggestions
- Contact finder generates realistic example contacts (note: for production use, integrate with a professional contact database API like Apollo.io or Hunter.io)
