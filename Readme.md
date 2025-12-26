## Mediation Form PDF to Word Generator

### Overview
This project recreates a predefined legal PDF form into a Microsoft Word document
using Python. The layout, table structure, spacing, and placeholders are manually
reconstructed to closely match the original PDF.

Due to fundamental differences between PDF and Word rendering engines, a fully
automated conversion is not feasible. Instead, this solution focuses on high-accuracy,
programmatic document generation for the given format.

### Tech Stack
- Python 3.x
- Flask
- python-docx

### Approach
- Analyzed the PDF layout manually
- Recreated headings, tables, and merged cells using `python-docx`
- Disabled Word auto-fit and enforced column widths to preserve table geometry
- Preserved all placeholders and conditional templating logic
- Exposed document generation via a Flask endpoint

### Limitations
- This solution is designed for the provided PDF format only
- Minor font and rendering differences may exist between PDF and Word

### How to Run
```bash
pip install -r requirements.txt
python app.py
