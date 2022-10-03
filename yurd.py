
import xlsxwriter
import array
from xlsxwriter.worksheet import Worksheet
import numpy as np





workbook = xlsxwriter.Workbook('NewstudentList.xlsx')
worksheet = workbook.add_worksheet('Colleges')
worksheet2 = workbook.add_worksheet('US-Prompts')

worksheet.write('A1', 'University Name')
worksheet.write('B1', 'Category')
worksheet.write('C1', 'Application') 
worksheet.write('D1', 'Supplemental/writing')
worksheet.write('E1', 'Early Decision')
worksheet.write('F1', 'Early Decision II')
worksheet.write('G1', 'Early Action')
worksheet.write('H1', 'Regular Decision')
worksheet.write('I1', 'Notes')
worksheet.write('J1', 'Document')

    
rowIndex = 2
NumCollege = int(input('How many colleges?'))
for i in range (NumCollege):
    
    college = input('Enter College Name: '  )
 
    category = input('Enter Category: ')
   
    worksheet.write('A' + str(rowIndex), college)
    worksheet.write('B' + str(rowIndex), category)
    worksheet2.write('A'+ str(rowIndex), college)
    rowIndex +=1

worksheet2.write('A1', 'University Name')
worksheet2.write('B1', 'Prompts')
workbook.close()


