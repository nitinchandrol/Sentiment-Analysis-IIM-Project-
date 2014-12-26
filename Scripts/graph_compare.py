import matplotlib.pyplot as pyplot
import sentiment
from feature_database import feature_list

## function for creating comparative graph between 2 products
def make_compare_graph(inputfile1,inputfile2):
	l1 = sentiment.find_count(inputfile1)
	l2 = sentiment.find_count(inputfile2)
	y1=[]
	y2=[]
	x1=[]
	for i in range(0,len(l1)):
		y1.append(l1[i][0] + l1[i][1])
		y2.append(l2[i][0] + l2[i][1])
		x1.append(i)
	x2 = [ x + 0.25 for x in x1 ]
	pyplot.xticks(x1,feature_list,rotation='vertical')
	pyplot.yticks([5*k for k in range(0,100)])
	pyplot.title('Feature_Count')
	pyplot.xlabel("Features")
	pyplot.ylabel("Count")
	inputfile1 = inputfile1.replace("../input_files/","")
	inputfile2 = inputfile2.replace("../input_files/","")
	name1 = inputfile1.replace(".xml","").replace(".json","")
	name2 = inputfile2.replace(".xml","").replace(".json","")
	pyplot.bar(x1,y1, width=0.1, color='red', label= name1) 
	pyplot.bar(x2,y2, width=0.1,color='green', label= name2)
	pyplot.legend()
	#autolabel(count)
	#inputfile = inputfile.replace("../XML_files/","")
	png_name = name1 + " vs " + name2 + ".png" 
	#png_name = inputfile.replace(".xml",".png").replace(".json",".png").replace(".txt",".png") 
	png_n = "../Graph/" + png_name
	pyplot.savefig(png_n) 
	pyplot.show()			
	print "Comparasion Graph is generated"
#make_compare_graph("../input_files/apple1.xml","../input_files/nokia1.xml")
