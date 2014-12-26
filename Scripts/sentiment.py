##this creates a csv with feature count for single brand
from nltk.stem.wordnet import WordNetLemmatizer
import operator
from feature_database import feature_list, feature, new_syn, new_hyp 
from sentiment_database import pos_list, neg_list
import csv 
#from pos import 

def edit_distance(s, len_s, t, len_t):
##base case: empty strings 
  if len_s == 0 :
	   return len_t;
  if len_t == 0 :
	  return len_s;
 
  #test if last characters of the strings match 
  if s[len_s-1] == t[len_t-1]:
      cost = 0;
  else:
      cost = 1;
 
  #return minimum of delete char from s, delete char from t, and delete char from both 
  return min(edit_distance(s, len_s - 1, t, len_t    ) + 1,edit_distance(s, len_s    , t, len_t - 1) + 1,edit_distance(s, len_s - 1, t, len_t - 1) + cost);

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
	word = word.replace("<reviews>"," ").replace("</reviews>"," ").replace("<value>"," ").replace("</value>"," ").replace("&lt;/b&gt;  &lt;div class=&quot;reviewText&quot;&gt;",",").replace("&lt;b&gt;",",").replace("&lt;/div&gt;"," ").replace("&lt;br&gt;"," ").replace("&amp;amp;",",").replace("<value>"," ")
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
			
def found(word,split_list):
	for split in split_list:
		if split in word:
			return True
	else:
		return False	

## function to find feature count for a xml file 
def find_count(inputfile):
	reviewfile = open(inputfile,'r') 
	count = []
	dum = []
	final_data = []
	unmatch_data = []
	text = []
	line_list = []
	split_word = [".","and","but",",","with"]
	debug_file = open("debug.txt","w")
	for line in reviewfile:
		splited = line.split();
		for i in range(len(splited)):
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
	reviewfile.close()
	for i in range(len(feature_list)):
		count.append([0,0,0]);
		final_data.append([[],[],[]])
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
			#debug_file.write(ans + "\n")
			#print ([feature_list[aspect]] + [str(ans)] + text[k])
		else:
			unmatch_data.append(repr(text[k]))
			#debug_file.write(repr(text[k]) + "\n")
			#print (text[k])
			

	for i in range(len(count)) :
		#print ("Count for positive the feature " + feature_list[i] + " is :" + str(count[i][0]) + "\n")
		#print ("Count for negative the feature " + feature_list[i] + " is :" + str(count[i][1]) + "\n")
		#print ("Count for neutral the feature " + feature_list[i] + " is :" + str(count[i][2]) + "\n")
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
	debug_file.write("Unmatched" + "\n")
	for k in range(len(unmatch_data)):
		debug_file.write(repr(unmatch_data[k]) + "\n")
	debug_file.close()
	inputfile = inputfile.replace("../input_files","")
	csv_name = inputfile.replace(".xml","_feature.csv").replace("json","_feature.csv").replace(".txt","_feature.csv") 
	csv_n = "../CSV_files/" + csv_name
	outfile = open(csv_n,"wb")
	writer = csv.writer(outfile, delimiter=' ')
	writer.writerow(["Features","Positive_count","Negative_count","Neutral_count"])
	for i in range(len(count)):
		writer.writerow([feature_list[i],count[i][0],count[i][1],count[i][2]])
	outfile.close()
	return count

#find_count("dataset1.txt")

