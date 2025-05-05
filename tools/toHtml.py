from nbconvert import HTMLExporter
from nbformat import read
import os

# Load the notebook
with open("D:\\0-AI-ML\\ai-ml\\CaseStudy\\FoodHub\\Learner_Notebook_Full_Code.ipynb", "r", encoding="utf-8") as f:
    notebook = read(f, as_version=4)

# Convert to HTML
html_exporter = HTMLExporter()
html_data, _ = html_exporter.from_notebook_node(notebook)

# Save the HTML file
with open("D:\\0-AI-ML\\ai-ml\\CaseStudy\\FoodHub\\Learner_Notebook_Full_Code.html", "w", encoding="utf-8") as f:
    f.write(html_data)
