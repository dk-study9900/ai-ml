from nbconvert import HTMLExporter
from nbformat import read
import os

# Load the notebook
with open("D:\\Downloads\\Lesson5_CaseStudy.ipynb", "r", encoding="utf-8") as f:
    notebook = read(f, as_version=4)

# Convert to HTML
html_exporter = HTMLExporter()
html_data, _ = html_exporter.from_notebook_node(notebook)

# Save the HTML file
with open("D:\\Downloads\\Lesson5_CaseStudy.html", "w", encoding="utf-8") as f:
    f.write(html_data)
