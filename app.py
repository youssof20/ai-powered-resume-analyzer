from flask import Flask, request, jsonify
from resume_analyzer import analyze_resume

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    resume_text = data.get("resume_text")
    
    if not resume_text:
        return jsonify({"error": "No resume text provided!"}), 400
    
    analysis_result = analyze_resume(resume_text)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
