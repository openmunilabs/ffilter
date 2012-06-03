import sys
import re
from openpyxl.reader.excel import load_workbook

def main():
	filename=sys.argv[1]
	workbook=load_workbook(filename=filename)
	
	for worksheet in workbook.worksheets:
		title=worksheet.title
		for row in worksheet.rows:
			values=[]
			for cell in row:
				coords=cell.get_coordinate()

				value=cell.value
				if value is None:
					value=''
				if not isinstance(value, unicode):
					value=unicode(value)
				value=value.encode('utf8')
				
				if sensitive(value):
					print "Sensitive information at ","Worksheet: ", title," Cell: ", coords

def sensitive(content):
	ssn=re.compile('\d\d\d-\d\d-\d\d\d\d')
	return ssn.match(content) is not None
	
if __name__=='__main__':
	main()