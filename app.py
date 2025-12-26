from flask import Flask, send_file
from doc_generator.generator import generate_mediation_form
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "to get document add '/generate' to the url"

@app.route("/generate", methods=["GET"])
def generate():
    output_path = "output/generated.docx"
    os.makedirs("output", exist_ok=True)
    generate_mediation_form(output_path)
    return send_file(output_path, as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
