## script to generate database
import nltk
import similarity
from nltk.corpus import wordnet as wn
from database import feature, feature_list
from nltk.stem.wordnet import WordNetLemmatizer
#########################
#function for checking if 2 words are synonyms or not
def check_synonym(word, word2):
    """checks to see if word and word2 are synonyms"""
    l_syns = list()
    lmtzr = WordNetLemmatizer()
    word = lmtzr.lemmatize(word)
    synsets = wn.synsets(word2)
    for synset in synsets:
        for i in range(0,len(synset.lemma_names)):
			if word == synset.lemma_names[i] and similarity.semantic_match(word,word2) == 1:
				l_syns.append( (word, word2))
				#print l_syns
				return l_syns
    return l_syns
##########################    
#function for checking if 2 words are hypernyms or not
def check_hypernym(word, word2):
    """checks to see if word and word2 are hypernyms"""
    l_syns = list()
    synsets = wn.synsets(word2)
    
    for synset in synsets:
		for hypernym in synset.hypernyms():
			for ss in hypernym.lemmas: 
				if word == ss.name:
					 l_syns.append( (word, word2) )
					 #print l_syns
					 return l_syns	
    return l_syns
					 
#######################
def remove_duplicates(l):
    return list(set(l))
#######################
new_syn = [[] for x in xrange(len(feature))]
new_hyp = [[] for x in xrange(len(feature))]
############## 

#function takes a list of file to create database
def increase_database(filename_list):
	for filename in filename_list:
		file_content = open(filename).read()
		tokens = nltk.word_tokenize(file_content)
		ans = nltk.pos_tag(tokens)

		class_NNP = [];
		for x in range(0,len(ans)):
			if ans[x][1] == 'NN' or ans[x][1] == 'NNP':
				str = ans[x][0].lower()
				for i in range(0,len(feature)):
					for j in range(0,len(feature[i])):
						if str != feature[i][j]:
							syn = check_synonym(str, feature[i][j])
							syn1 = check_hypernym(str, feature[i][j])
							if len(syn)> 0 : 
								if str != feature[i][j]:
									new_syn[i].append(str)
							if len(syn1)> 0 : 
								if str != feature[i][j]:
									new_hyp[i].append(str)	
	for i in range(0,len(feature)):
		new_syn[i] = remove_duplicates(new_syn[i])
		new_hyp[i] = remove_duplicates(new_hyp[i])

	f = open('database.py', 'a')	
	f.write( 'new_syn = ' + repr(new_syn) + '\n' )
	f.write( 'new_hyp = ' + repr(new_hyp) + '\n' )
	f.close()

#increase_database(["../XML_files/apple1.xml","../XML_files/samsung1.xml","../XML_files/nokia1.xml"])



	
	

		
		
		
		
		
