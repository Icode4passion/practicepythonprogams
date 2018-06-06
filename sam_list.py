# import csv

# []

# with open('data.csv','w+') as fp:
	
# 	fieldnames = ["Company","date","share","profit"]
# 	out = csv.DictWriter(fp , fieldnames = fieldnames)
# 	out.writerows([
# {"Company" : "Amazon" , "date":"12/01/2017","share":"133","profit":"87.1"},
# {"Company" : "Apple" , "date":"12/12/2017","share":"134","profit":"67.11"},
# {"Company" : "Wipro" , "date":"11/01/2017","share":"135","profit":"77.90"},
# {"Company" : "IBM" , "date":"10/01/2017","share":"136","profit":"57.56"},
# {"Company" : "Infosys" , "date":"02/01/2017","share":"137","profit":"87.76"}
# ])
# 	print("Write Completed !!!!!")
	


import pickle

data  = {"int_list":[1, 2, 3],"text":'string',"number":3.44,"boolean":True,"none":None}


with open('data.pickle','wb') as f:
	pickle.dump(data,f)