import os
import PyPDF2
import sys
os.chdir('/home/kapil/Desktop')

passwords=[]

PDFReaderobj=PyPDF2.PdfFileReader(open('encrypted1.pdf','rb'))
file_obj=open('dictionary.txt','r')

passwords=file_obj.read().split('\n')

for password in passwords:
	try:
		if PDFReaderobj.decrypt(password):
			print('the hacked password is '+password)
			
			break
					
	except UnicodeEncodeError:
		pass
	
file_obj.close()
