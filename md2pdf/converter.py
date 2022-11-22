import os

os.add_dll_directory(r"C:/Program Files/GTK3-Runtime Win64/bin")
from md2pdf.core import md2pdf

directory = 'geromesmuziek\md2pdf\input'

filelist = []

# iterate over files in
# that directory
for filename in os.listdir(directory):
    mdfile = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(mdfile):
        print(mdfile)
        filelist.append(mdfile)
        pdfname = mdfile.replace("input","output",1)
        pdfname = pdfname[0:-2] + "pdf"
        print(pdfname)

        md2pdf(pdfname,
              md_content=None,
              md_file_path=mdfile,
              css_file_path=None,
              base_url=None)
    

print(filelist)

with open("geromesmuziek/md2pdf/template.html","r",encoding='utf-8') as htmlfile:
    htmldata = (htmlfile.read())
    htmllist = ""
    for file in filelist:
         htmllist += f"<a href={file}> test </a>" + "<br>"
    
    htmldata = htmldata.replace("data",htmllist)

    with open("geromesmuziek/md2pdf/index.html","w") as htmloutput:
        htmloutput.write(htmldata)

#installeer GTK3-runtime
#werkt niet zonder