from docx2pdf import convert
from PyPDF2 import PdfWriter, PdfReader

#Enter the name of the document
file = "example"

#Converts the docx document into a pdf
convert(file+".docx")

#Reads the pdf created and counts the number of pages
inputpdf = PdfReader(open(file+".pdf", "rb"))
pages = len(inputpdf.pages)
page = ''
other_pages = []
extract = []

choice = input("Enter 'R' for extracting a page range or 'S' for specific pages: ")
while(choice.upper() == 'R'):
#Input page range
    start_page = int(input("Enter starting page: "))
    end_page = int(input("Enter ending page: "))
    extract += list(range(start_page,end_page+1))
    choice = input("Enter 'R' to process another range \nEnter 'S' for Single Pages \nEnter 'N' to stop processing: ")
#Input any page number you want added separately
if choice.upper() == 'S':
    page = input("Enter page numbers separated by a comma: ")
    if ',' in page:
        page = page.split(",")
        page = [int(p) for p in page]
    else:
        page = int(page)

if(choice.upper() != 'N' and type(page)==list):
    extract += page
elif(choice.upper != 'N'):
    extract.append(page)

for i in range(pages):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    if((i+1) in extract):
        with open(f"page {i+1}.pdf", "wb") as outputStream:
            output.write(outputStream)











