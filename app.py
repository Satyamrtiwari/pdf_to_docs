from flask import Flask, send_file
from doc_generator.generator import generate_mediation_form
import os

app = Flask(__name__)

@app.route("/")
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>PDF to DOCX</title>
        </head>
        <body style="display:flex; justify-content:center; align-items:center; height:100vh; font-family:Arial;">
            <form action="/generate" method="get">
                <button 
                    type="submit"
                    style="
                        padding:12px 20px;
                        font-size:16px;
                        cursor:pointer;
                        border-radius:6px;
                        border:1px solid #333;
                        background-color:#f5f5f5;
                    "
                >
                    Click to get document
                </button>
            </form>
        </body>
    </html>
    """


@app.route("/generate", methods=["GET"])
def generate():
    output_path = "output/generated.docx"
    os.makedirs("output", exist_ok=True)
    generate_mediation_form(output_path)
    return send_file(output_path, as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
