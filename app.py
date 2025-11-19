import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# the newest OpenAI model is "gpt-5" which was released August 7, 2025.
# do not change this unless explicitly requested by the user
openai_client = OpenAI(api_key=OPENAI_API_KEY)


@app.route('/')
def index():
    return render_template('index.html')


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
        
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        response = openai_client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are an expert email writer who crafts compelling, effective cold emails and professional correspondence."},
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=1000
        )
        
        generated_email = response.choices[0].message.content
        
        return jsonify({'email': generated_email})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
