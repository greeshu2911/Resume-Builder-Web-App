from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        skills = request.form["skills"]
        experience = request.form["experience"]
        education = request.form["education"]

        # Generate PDF
        pdf_buffer = generate_pdf(name, email, phone, skills, experience, education)
        return send_file(pdf_buffer, as_attachment=True, download_name="resume.pdf", mimetype="application/pdf")

    return render_template("index.html")

def generate_pdf(name, email, phone, skills, experience, education):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Resume")

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, name)

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 720, f"Email: {email}")
    pdf.drawString(50, 700, f"Phone: {phone}")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 670, "Skills")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 650, skills)

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 620, "Experience")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 600, experience)

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 570, "Education")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 550, education)

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer

if __name__ == "__main__":
    app.run(debug=True)
