from fpdf import FPDF
import pandas as pd

def create_pdf_document():
  #emty pdf document
  pdf = FPDF(orientation='P', unit='pt', format='A4')
  pdf.add_page()
  
  pdf.image('tiger.jpeg', w=80, h=50)
  #w=0 is take the all witdth
  
  pdf.set_font(family='Times', style='B', size=24)
  #ln=1 get the new line
  pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1)
  
  pdf.set_font(family='Times', style='B', size=14)
  pdf.cell(w=0, h=20, align='C',txt="Description", ln=1)
  
  text1="""The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous declining trend"""
  
  pdf.set_font(family='Times', size=14)
  pdf.multi_cell(w=0, h=15,txt=text1)
  
  pdf.set_font(family='Times', style='B', size=14)
  pdf.cell(w=100,h=25, txt='Kingdom: ')
  
  pdf.set_font(family='Times', size=14)
  pdf.cell(w=100,h=25, txt='Animalia', ln=1)
  
  
  pdf.set_font(family='Times', style='B', size=14)
  pdf.cell(w=100,h=25, txt='Phylum:: ')
  
  pdf.set_font(family='Times', size=14)
  pdf.cell(w=100,h=25, txt='Chordata', ln=1)
  
  pdf.output('output.pdf')
#create_pdf_document()

#Let's crete multiple pdf document from the excel data
def create_multiple_pdf_from_excel_data():
  df  = pd.read_excel('data.xlsx')
  
  for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
  
    #create title
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)
  
    #kingdom
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100,h=25, txt='Kingdom: ')
    
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100,h=25, txt=row['kingdom'], ln=1)
  
    #phylum
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100,h=25, txt='Phylum: ')
    
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100,h=25, txt=row['phylum'], ln=1)
  
    #class
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100,h=25, txt='Class: ')
    
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100,h=25, txt=row['class'], ln=1)
  
    #order
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100,h=25, txt='Order: ')
    
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100,h=25, txt=row['order'], ln=1)
  
    #suborder
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100,h=25, txt='Suborder: ')
    
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100,h=25, txt=row['suborder'], ln=1)
  
    pdf.output(f"{row['name']}.pdf")
    
#create_multiple_pdf_from_excel_data()
  





  


