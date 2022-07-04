import sys
import pikepdf


pdf_filename = sys.argv[1]

pdf = pikepdf.Pdf.open(pdf_filename)

docinfo = pdf.docinfo
for key, value in docinfo.items():
    print(key, ":", value)
