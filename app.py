import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# IMPORTANT: KEEP THIS COMMENT
# Follow these instructions when using this blueprint:
# - Note that the newest Gemini model series is "gemini-2.5-flash" or gemini-2.5-pro"
#   - do not change this unless explicitly requested by the user
# This API key is from Gemini Developer API Key, not vertex AI API Key
gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find-contacts', methods=['POST'])
def find_contacts():
    try:
        data = request.get_json()
        company_type = data.get('company_type', 'big tech')
        role_types = data.get('role_types', ['Staff Engineer', 'HR Leader'])
        location = data.get('location', 'San Francisco')
        
        # Use Gemini to generate realistic contact suggestions based on the criteria
        prompt = f"""Generate a list of 5 potential hiring manager contacts at {company_type} companies in {location}.

For each contact, provide:
- Name (realistic but fictional to demonstrate the concept)
- Title (should be one of: {', '.join(role_types)})
- Company (real {company_type} company names)
- Location

Format as a JSON array with objects containing: name, title, company, location

Example format:
[
  {{"name": "John Doe", "title": "Staff Engineer", "company": "Google", "location": "San Francisco, CA"}},
  ...
]

IMPORTANT: Return ONLY the JSON array, no other text."""

        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        
        contacts_text = response.text if response.text else "[]"
        import json
        contacts = json.loads(contacts_text)
        
        return jsonify({'contacts': contacts})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/generate-email', methods=['POST'])
def generate_email():
    try:
        data = request.get_json()
        job_role = data.get('job_role', '')
        purpose = data.get('purpose', '')
        tone = data.get('tone', 'professional')
        recipient_name = data.get('recipient_name', '')
        additional_context = data.get('additional_context', '')
        
        if not purpose:
            return jsonify({'error': 'Email purpose is required'}), 400
        
        system_instruction = "You are an expert email writer who crafts compelling, effective cold emails and professional correspondence."
        
        prompt = f"""Generate a {tone} cold email based on the following details:

Job Role: {job_role if job_role else 'Not specified'}
Purpose: {purpose}
Recipient Name: {recipient_name if recipient_name else 'Not specified'}
Additional Context: {additional_context if additional_context else 'None'}

Write a compelling, well-structured email that:
- Has an engaging subject line
- Opens with a strong hook
- Clearly communicates the purpose
- Is appropriate for the {tone} tone
- Ends with a clear call-to-action
- Is concise and professional

Format the response as:
Subject: [subject line]

[email body]
"""
        
        # Using gemini-2.5-flash as specified in the blueprint
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )
        
        generated_email = response.text if response.text else "Failed to generate email"
        
        return jsonify({'email': generated_email})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
