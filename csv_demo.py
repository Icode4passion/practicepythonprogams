import csv

fields= ['Movie','Hero','Director','Gener']

data =[['Krishna','Raviteja','VV Vinayak','Comedy'],
		['Jalsa','Pavan Kalyan','Trivikram','Action'],
		['Dasavatharam','Kamalahasan','KS Ravikumar','Sci Fic'],
		['Nenu Meeku Telusa...?','Manchu','Ajay Sastry','Thriller'],
		['Kotha Bangaru Lokam','Gottam','Srikath Addala','Romance'],
		['Cell','Prabhakar','Venkata Narayana','Political'],
		['Palasa','Ualasa','Narayana','Singam']]

filename = 'shit.csv'

with open(filename,'w+') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(data)

print('CSV Data Completed .....')