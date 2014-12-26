from feature_database import feature_list, feature, new_syn, new_hyp 
from sentiment_database import pos_list, neg_list
from nltk.stem.wordnet import WordNetLemmatizer
from xml.dom import minidom  
import operator      
import csv        
import os

## function to check positive sentiment
def positive(word_list):
	for pos in pos_list:
		for word in word_list:
			if word == pos:
				return True
	return False

# function to check negative sentiment	
def negative(word_list):
	for neg in neg_list:
		for word in word_list:	
			if word == neg:
				return True
	return False
	
# function to properly extract review sentances		
def remove_symbol(word):
	word = word.replace("<value>","").replace("</value>","").replace("<title>","").replace("</title>","").replace("<item>"," ").replace("</item>"," ").replace("<items>","").replace("<reviews>"," ").replace("</reviews>"," ").replace("&lt;/b&gt;  &lt;div class=&quot;reviewText&quot;&gt;",",").replace("&lt;b&gt;",",").replace("&lt;/div&gt;"," ").replace("&lt;br&gt;"," ").replace("&amp;amp;",",").replace("<value>"," ").replace("class=\"reviewtext\"&gt;","").replace("&lt;/b&gt;  &lt;div","").replace("&lt;/b&gt;&lt;div","")
	return word

# function to detect sentiment
def detect_sentiment(line_word):
	if positive(line_word):
		a=0;
	else:
		if negative(line_word):
			a=1;
		else:
			a=2;
	return a
			
# function to detect feature			
def detect_feature(line_word,word_list):
	feature_word = ""
	lmtzr = WordNetLemmatizer()
	for word in line_word:
		word = ''.join([i for i in word if not i.isdigit()])
		word.replace("-","")
		for i in range(0,len(word_list)):
			for j in range(0,len(word_list[i])):
				if lmtzr.lemmatize(word_list[i][j]) == lmtzr.lemmatize(word) :
					#or edit_distance(word_list[i][j],len(word_list[i][j]),word,len(word)) < 2 :
					return (i,word_list[i][j])
				
	return (-1,"NONE")

def remove_feature(word):
	a = word.find('#')
	if a != -1 :
		word = word[a+2:]
	return word
	
def last_index(word_list):
	ans = -1
	for i in range(0,len(word_list)):
		if "#" in word_list[i]:
			ans = i
	return ans

def found(word,split_list):
	for split in split_list:
		if split in word:
			return True
	else:
		return False	

## function to find feature count for a csv file 
def find_count(inputfile):

	reviewfile = open(inputfile ,'rb');
	split_word = [".","and","but",",","with"]
	file_num = 1
	count1 = []
	next(reviewfile)
	for line in reviewfile:
		debug_file = open("debug.txt","w")
		count = []
		final_data = []
		text = []
		line_list = []
		for i in range(len(feature_list)):
			count.append([0,0,0]);
			final_data.append([[],[],[]])
		check = False
		rating = ""
		splited = line.split();
		for i in range(len(splited)):
			if "title=" in splited[i] and not(check):
				rating += splited[i][6:]
				check = True
			if found(splited[i],split_word):
				if "."  in splited[i]:
					new_word = splited[i].split(".")
					line_list.append(new_word[0])
					text.append(line_list)
					line_list = []
					line_list.append(new_word[1])
				else :
					if ","  in splited[i]:
						new_word = splited[i].split(",")
						line_list.append(new_word[0])
						text.append(line_list)
						line_list = []
						line_list.append(new_word[1])
					else :
						line_list.append(splited[i])
						text.append(line_list)
						line_list = []
			else:
				line_list.append(splited[i])

		for k in range(0,len(text)):
			for j in range(0,len(text[k])):
				text[k][j] = text[k][j].lower()
				text[k][j] = remove_symbol(text[k][j])
				
			#print (text[k])
			ans = detect_sentiment(text[k])
			aspect_list = detect_feature(text[k],feature) 
			if  aspect_list[0] == -1:
				aspect_list = detect_feature(text[k],new_syn)
				if aspect_list[0] == -1:
					aspect_list = detect_feature(text[k],new_hyp)
			if aspect_list[0] != -1:
				count[aspect_list[0]][ans] = count[aspect_list[0]][ans] + 1
				data_line = repr(aspect_list[1]) + repr(feature_list[aspect_list[0]]) + repr(str(ans)) + repr(text[k])
				final_data[aspect_list[0]][ans].append(data_line)
				debug_file.write(ans + "\n")
			else:
				debug_file.write(repr(text[k]) + "\n")
				

		for i in range(len(count)) :
			debug_file.write(feature_list[i].upper() + "\n")
			for j in range(0,len(final_data[i][0])):
				debug_file.write(repr(final_data[i][0][j]) + "\n")
			
			debug_file.write("\n")
			
			for j in range(0,len(final_data[i][1])):
				debug_file.write(repr(final_data[i][1][j]) + "\n")
			
			debug_file.write("\n")
			
			for j in range(0,len(final_data[i][2])):
				debug_file.write(repr(final_data[i][2][j]) + "\n")
			
			debug_file.write("\n" + "\n")
		count.append(float(rating))
		count1.append(count)
		debug_file.close()

	csv_name = inputfile.replace(".xml","_regress.csv").replace(".json","_regress.csv").replace(".txt","_regress.csv").replace(".csv","_regress.csv") 
	#csv_n = "CSV_files/" + csv_name
	outfile = open(csv_name,"wb")
	writer = csv.writer(outfile, delimiter=' ')
	writer.writerow(["price", "picture","battery","storage", "upgrade","hardware","feature","size","design","media","sound","service","help-care","overall"])
	for i in range(0,len(count1)):
		dum = []
		for j in range(0,len(count1[0])):
			if j != len(count1[0])-1:
				data = count1[i][j][0]+ count1[i][j][1]+ count1[i][j][2]
			else:
				data = count1[i][j]
			dum.append(data)
		writer.writerow([dum[0],dum[1],dum[2],dum[3],dum[4],dum[5],dum[6],dum[7],dum[8],dum[9],dum[10],dum[11],dum[12],dum[13],dum[14]])
	outfile.close()
	print "CSV file is generated"
	return count1
	
#find_count("../CSV_files/regress_data.csv")
		
