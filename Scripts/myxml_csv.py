from xml.dom import minidom  
import operator      
import csv        
import os

# function to conver xml to csv
def convert_tocsv(inputfile):                   
	xmldoc = minidom.parse(inputfile)
	xmldoc
	item = xmldoc.childNodes[0]
	outputfile = inputfile.replace("xml", "csv")
	csv_n = "CSV_files/" + outputfile
	inputfile = open(csv_n,"wb")
	writer = csv.writer(inputfile, delimiter=' ')
			
	writer.writerow(["Reviews","Link","Title","Rating"])
	for j in range(0,31):
		try: 
			rating = item.childNodes[j].childNodes[1].childNodes[0].childNodes[0]
			review = item.childNodes[j].childNodes[0]
			link = item.childNodes[j].childNodes[2]
			title = item.childNodes[j].childNodes[3]
			col1 = review.toxml().replace("<reviews>"," ").replace("</reviews>"," ").replace("<value>"," ").replace("</value>"," ").replace("&lt;/b&gt;  &lt;div class=&quot;reviewText&quot;&gt;",",").replace("&lt;b&gt;",",").replace("&lt;/div&gt;"," ").replace("&lt;br&gt;"," ").replace("&amp;amp;",",").replace("<value>"," ")
			col2 = link.toxml().replace("<link>","").replace("</link>","")
			col3 = title.toxml().replace("<value>","").replace("</value>","").replace("<title>","").replace("</title>","")
			col1 = col1.encode('ascii', 'ignore')
			col4 = rating.toxml().replace("out of 5 stars&lt;/span&gt;&lt;/span&gt;","").replace("out of 5 stars&quot;&gt;&lt;span&gt;","").replace("&lt;span class=&quot;swSprite","").replace("&quot;","")
			#.replace("&lt;span class=&quot;swSprite s_star_4_5 &quot; title=&quot;","").replace("&quot;&gt;&lt;span&gt;","").replace("&lt;/span&gt;&lt;/span&gt;","")
			#print len(col4)
			#print col4[0]
			final = [col4[0],col4[1],col4[2]]
			#print '\n'
			#writer.writerow([col1, col2, col3, col4[:3]])
			for word in col4:
				if "s_star" in word:
					word = ""
			writer.writerow([col1, col2, col3, col4])
		except IndexError:
			pass
	inputfile.close()	

