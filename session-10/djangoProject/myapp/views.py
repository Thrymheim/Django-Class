from django.shortcuts import render
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def home(request):
    return render(request, 'home.html')

def produce_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Age', 'City'])  # Header row
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'London'])
    writer.writerow(['Charlie', 35, 'Paris'])

    return response

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(10, 770, "Hello, I am Maziyar")
    p.showPage()
    p.save()

    return response
