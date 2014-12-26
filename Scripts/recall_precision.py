#script to calculate recall precision for annotated data set 
from database import feature_list, feature, new_syn, new_hyp 
from senti_database import pos_list, neg_list
from nltk.stem.wordnet import WordNetLemmatizer
import similarity
#from database1 import  feature_list, feature, new_syn, new_hyp 
import csv
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
	
def remove_symbol(word):
	word = word.replace("<reviews>"," ").replace("</reviews>"," ").replace("<value>"," ").replace("</value>"," ").replace("&lt;/b&gt;  &lt;div class=&quot;reviewText&quot;&gt;",",").replace("&lt;b&gt;",",").replace("&lt;/div&gt;"," ").replace("&lt;br&gt;"," ").replace("&amp;amp;",",").replace("<value>"," ").replace("'","").replace("\"","")
	return word

def detect_sentiment(line_word):
	if positive(line_word):
		a=0;
	else:
		if negative(line_word):
			a=1;
		else:
			a=2;
	return a
def check_generic(word):
	generic_word = ["get","time","ask","work","item","product","have","do","friend","just","while","piece","even","person","buy","go","easy","set"]
	for i in range(len(generic_word)):
		 if word == generic_word[i]:
			return True
	return False

def edit_distance(s,len_s,t,len_t):
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

			
def detect_feature(line_word,word_list):
	index = 100
	feature_word = ""
	lmtzr = WordNetLemmatizer()
	for word in line_word:
		word = ''.join([i for i in word if not i.isdigit()])
		word.replace("-","")
		for i in range(len(word_list)):
			for j in range(len(word_list[i])):
				#if word == word_list[i][j]:
				if lmtzr.lemmatize(word_list[i][j]) == lmtzr.lemmatize(word):
				# or edit_distance(word_list[i][j],len(word_list[i][j]),word,len(word)) < 2 :
					return (i,word_list[i][j])
	return (-1,"NONE")

def matching(line_word,word_list):
	lmtzr = WordNetLemmatizer()
	for word in line_word:
		for i in range(len(word_list)):
			#if :
			if word_list[i] in word or word in word_list[i] or similarity.semantic_match(word,word_list[i]) > 0.6:
				return True
	return False
	
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
	
def find_RP(inputfile):
	#inputfile = input();
	#inputfile = "dataset1.txt"
	reviewfile = open(inputfile,'r');

	count = []
	final_data = []
	unmatch_data = []
	text = []
	feature_found = []
	debug_file = open("debug.txt","w")
	for i in range(len(feature_list)):
		count.append([0,0,0]);
		final_data.append([[],[],[]])
		
	for line in reviewfile:
		dummy = []
		splited = line.split();
		if len(splited) != 0:
			first = splited[0]
			if "[t]" not in first:
				index = last_index(splited)
				#print splited[:index]
				#splited[index] = remove_feature(splited[index]) 
				new_line = splited[index:]
				fea_size = index
				word = ""
				for i in range(0,fea_size+1):
					#print splited[i]
					mylist = splited[i].split(',')
					for feature_word in mylist:
						dum_index = feature_word.find('[')		
						if dum_index != -1:
							#print splited[i][:dum_index]
							word += feature_word[:dum_index]
							dummy.append(word)
							#print [word,sentiment]
							word = ""
						else :
							if "#" not in word:
								word = splited[i]
							else:
								word = ""
				if len(dummy) > 0:
					text.append(new_line)
					feature_found.append(dummy)
	#print feature_found
	retrive_count = 0
	match = 0						
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
			retrive_count = retrive_count + 1
			debug_file.write(ans + "\n")
			found_match = matching(feature_found[k],feature[aspect_list[0]])
			if  not(found_match):
				found_match = matching(feature_found[k],new_syn[aspect_list[0]])
			if not(found_match):
				found_match = matching(feature_found[k],new_hyp[aspect_list[0]])
			if found_match:
				match = match + 1	
		else:
			unmatch_data.append(repr(text[k]))
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
	debug_file.write("Unmatched" + "\n")
	for k in range(len(unmatch_data)):
		debug_file.write(repr(unmatch_data[k]) + "\n")
	debug_file.close()
	mtr_file = open("data_mtrix.txt","a")
	mtr_file.write(repr(inputfile) +"\n" + " count =" + repr(count) + "\n")
	
	csv_name = inputfile.replace(".xml","_feature.csv").replace("json","_feature.csv").replace(".txt","_feature.csv") 
	csv_n = "CSV_files/" + csv_name
	outfile = open(csv_n,"wb")
	writer = csv.writer(outfile, delimiter=' ')
	writer.writerow(["Features","Positive_count","Negative_count","Neutral_count"])
	for i in range(len(count)):
		writer.writerow([feature_list[i],count[i][0],count[i][1],count[i][2]])
	outfile.close()
	#match = len(text) - len(unmatch_data)
	print "size of total segments = " + str(len(text))
	print "size of retrived segments = " + str(retrive_count)
	print "size of correctly retrived segments = " + str(match)
	print "recall value is = " + str(float(match)/len(text))
	print "precision is = " + str(float(match)/retrive_count)
	return count

#find_RP("dataset1_phone.txt")		

