import pdfkit

path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
path_to_file = 'Daily.mhtml'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
pdfkit.from_file(path_to_file, output_path='sample.pdf', configuration=config)