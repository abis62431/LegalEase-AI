from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        legal_text = request.form.get('legal_text')
        # Simple AI logic - summarization mockup
        if legal_text:
            result = f"Simplified Version: This document basically says about {legal_text[:100]}... [LegalEase AI Analyzed]"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
