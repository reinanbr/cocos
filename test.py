from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

# Create a PDF document
pdf_path = "output.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)

# Create a list to hold the content elements
content = []

# Define styles
styles = getSampleStyleSheet()
normal_style = styles["Normal"]
title_style = styles["Title"]

# Add a title to the PDF
title = Paragraph("Sample PDF with Text and Images", title_style)
content.append(title)

# Add some text
text = "This is an example of creating a PDF document with text and images using ReportLab in Python."
paragraph = Paragraph(text, normal_style)
content.append(paragraph)

# Add an image to the PDF
image_path = "oi.png"
image = Image(image_path, width=400, height=300)
content.append(image)

# Add space
content.append(Spacer(1, 12))

# Build the PDF document
doc.build(content)
