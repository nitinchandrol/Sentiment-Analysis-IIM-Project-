import matplotlib.pyplot as pyplot
from feature_database import feature_list
#count =[[7, 4, 0], [12, 0, 4], [32, 2, 14], [21, 4, 7], [33, 8, 22], [12, 5, 8], [12, 1, 6], [3, 0, 1],[0, 0, 0], [22, 5, 10]]

## function for creating graph for single product
def make_graph(count,inputfile,index):
	if index == 1:
		y1=[]
		y2=[]
		y3=[]
		x1=[]
		for i in range(0,len(count)):
			y1.append(count[i][0])
			y2.append(count[i][1])
			y3.append(count[i][2])
			x1.append(i)
		x2 = [ x + 0.25 for x in x1 ] 
		x3 = [ x + 0.50 for x in x1 ]
		pyplot.xticks(x1,feature_list,rotation='vertical')
		pyplot.yticks([3*k for k in range(0,100)])
		pyplot.title('Feature_Count')
		pyplot.xlabel("Features")
		pyplot.ylabel("Count")
		pyplot.bar(x1,y1, width=0.1, color='blue', label='Positive') 
		pyplot.bar(x2,y2, width=0.1,color='green', label='Negative') 
		pyplot.bar(x3,y3, width=0.1, color='red', label='Neutral') 
		pyplot.legend()
		#autolabel(count)
		inputfile = inputfile.replace("../XML_files","")
		png_name = inputfile.replace(".xml",".png").replace(".json",".png").replace(".txt",".png") 
		
		png_n = "../Graph/" + png_name
		pyplot.savefig(png_n) 
		print "Graph is generated"
		pyplot.show()
		
	else:
		for i in range(0,len(count)):
			y1=[]
			y2=[]
			y3=[]
			x1=[]
			print count
			for j in range(0,len(count[0])-1):
				y1.append(count[i][j][0])
				y2.append(count[i][j][1])
				y3.append(count[i][j][2])
				x1.append(j)
			x2 = [ x + 0.25 for x in x1 ] 
			x3 = [ x + 0.50 for x in x1 ]
			pyplot.xticks(x1,feature_list)
			pyplot.yticks([10*k for k in range(0,100)])
			pyplot.title('Feature_Count')
			pyplot.xlabel("Features")
			pyplot.ylabel("Count")
			pyplot.xticks(x1,feature_list,rotation='vertical')
			pyplot.bar(x1,y1, width=0.1, color='blue', label='Positive') 
			pyplot.bar(x2,y2, width=0.1,color='green', label='Negative') 
			pyplot.bar(x3,y3, width=0.1, color='red', label='Neutral') 
			pyplot.legend()
			#autolabel(count)
			inputfile = inputfile.replace("../XML_files","")
			png_name = inputfile.replace("CSV_files","Graph").replace(".csv","")
			png_name += str(i)
			png_name += ".png" 
			pyplot.savefig(png_name) 
			pyplot.show()
			pyplot.clf()
			print "Graph is generated"
	
