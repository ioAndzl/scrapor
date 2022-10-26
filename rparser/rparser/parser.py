import io
import os
import re
import nltk
#nltk.download('stopwords')
import spacy
import pandas as pd
import docx2txt
import constants as cs
from spacy.matcher import Matcher
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords 

import fitz
from PIL import Image

def extract_text_from_pdf(pdf_path):
    
    """
        Read and extract pdf content
        param:
            pdf_path(str): path to PDF file to be extracted
        return:
            to_complete 
            
    """
    # https://www.blog.pythonlibrary.org/2018/05/03/exporting-data-from-pdfs-with-python/
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle,laparams=LAParams())
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            print(text)
            
 
            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_image_from_pdf(pdf_path):
    
    """
        extract images from pdf content
        param:
            pdf_path(str): path to PDF file to be extracted
        return:
            to_complete 
            
    """
    # PyMuPDF
    
    pdf_file = fitz.open(pdf_path)
    # STEP 3
    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.getImageList()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            print(base_image)
            break
        break


if __name__=='__main__':

    print('there')
    #print(extract_text_from_pdf("Basico.pdf"))
    print(extract_image_from_pdf("Basico.pdf"))
