from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("ajtprint_2.pdf")
merger.append("ajtprint_3.pdf")
merger.append("ajtprint_4.pdf")

merger.Write("Mergedfile.pdf")
merger.close()

print("Pdf merged successfully")

