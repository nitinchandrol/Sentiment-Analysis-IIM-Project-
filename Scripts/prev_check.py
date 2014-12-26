from feature_database import feature_list, feature, new_syn, new_hyp 
from sentiment_database import pos_list, neg_list
import csv
## script to find a matching between annotated dataset features and our model features
def positive(word_list):
	for pos in pos_list:
		for word in word_list:
			if word == pos:
				return True
	return False
	
def negative(word_list):
	for neg in neg_list:
		for word in word_list:	
			if word == neg:
				return True
	return False

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

def last_index(word_list):
	ans = -1
	for i in range(0,len(word_list)):
		if "#" in word_list[i]:
			ans = i
	return ans
		
def find_match(inputfile):
	reviewfile = open(inputfile,'r');
	feature_found = []
	word = []
	sentiment = 0
	for line in reviewfile:
		splited = line.split();
		if len(splited) > 0 :
				if "[t]" not in splited[0]:
					fea_size =last_index(splited)
					word = ""
					for i in range(0,fea_size+1):
						dum_index = splited[i].find('[')
						
						if dum_index != -1:
							word += splited[i][:dum_index]
							if "+" in splited[i]:
								sentiment = 0
								
							else :
								if "-" in splited[i]:
									sentiment = 1
									feature_found.append([word,1])
								else :
									sentiment = 2
									feature_found.append([word,2])
							feature_found.append([word,sentiment])
							word = ""
						else :
							word = splited[i]
	#print feature_found
	len(feature_found)
	feature_count = []
	for i in range(len(feature_list)):
		feature_count.append([0,0,0]);
	match = 0;	
	for i in range(0,len(feature_found)):
		aspect_list = detect_feature(feature_found[i][0],feature)
		if  aspect_list[0] == -1:
			aspect_list = detect_feature(feature_found[i][0],new_syn)
		if aspect_list[0] == -1:
			aspect_list = detect_feature(feature_found[i][0],new_hyp)
		if aspect_list[0] != -1:
			match = match + 1
			feature_found[i].append(feature_list[aspect_list[0]])
			if feature_found[i][1] == 0 :
				feature_count[aspect_list[0]][0] = feature_count[aspect_list[0]][0] + 1
			else :
				feature_count[aspect_list[0]][1] = feature_count[aspect_list[0]][1] + 1
		else:
			feature_found[i].append("NONE")
	print (str(match) + " features being matched out of " + str(len(feature_found)))
	var = inputfile
	csv_name = var.replace(".xml","_featurecheck.csv").replace("json","_featurecheck.csv").replace(".txt","__featurecheck.csv") 
	csv_n = "CSV_files/" + csv_name
	outfile = open(csv_n,"wb")
	writer = csv.writer(outfile, delimiter=' ')
	writer.writerow(["Features","Positive_count","Negative_count","Neutral_count"])
	for i in range(len(feature_count)):
		writer.writerow([feature_list[i],feature_count[i][0],feature_count[i][1],feature_count[i][2]])
	outfile.close()
	
	var = inputfile
	csv_name = inputfile.replace(".xml","_matching.csv").replace(".json","_matching.csv").replace(".txt","_matching.csv") 
	csv_n = "CSV_files/" + csv_name
	outfile = open(csv_n,"wb")
	writer = csv.writer(outfile, delimiter=' ')
	writer.writerow(["Feature","Inherited_feature"])
	for i in range(len(feature_found)):
		writer.writerow([feature_found[i][0],feature_found[i][2]])
	outfile.close()
	return feature_count
	
#find_count("dataset1.txt")

