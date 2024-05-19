from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def compare_documents(doc1, doc2):
    prompt = f"Compare the following two documents and highlight the similarities and differences:\n\nDocument 1:\n{doc1}\n\nDocument 2:\n{doc2}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    doc1 = request.form['doc1']
    doc2 = request.form['doc2']

    if not doc1 or not doc2:
        return jsonify({"error": "Both documents must be provided"}), 400

    comparison_result = compare_documents(doc1, doc2)
    return jsonify({"comparison": comparison_result})

if __name__ == '__main__':
    app.run(debug=True)
