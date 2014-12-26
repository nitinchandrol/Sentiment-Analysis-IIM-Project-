## this scripts generates graphic interface

from Tkinter import *
from tkFileDialog   import askopenfilename      
from tkMessageBox import *
import sentiment
import sentiment2
import graph
import graph_compare
import os

## file_name and file_name_prev are the previous 2 imported file, currently 2 defalut files are choosen
file_name = "../input_files/apple1.xml"
file_name_prev = "../input_files/samsung1.xml"
l = []
i = 1
## function for making descriptive graph of a single product 
def make_graph():
	global l
	global file_name
	global i
	print "Wait, process going on"
	graph.make_graph(l,file_name,i)
	
## function for making a comparative graph of 2 product	
def make_graph2():
	global file_name
	global file_name_prev
	print "Wait, process going on"
	graph_compare.make_compare_graph(file_name,file_name_prev)
	
## function for generating feature count for a single product	
def callscript():
	global l
	global i
	i = 1
	print "Wait, process going on"
	l=sentiment.find_count(file_name)
	print "CSV file is generated"

## function for generating feature count for multiple products	
def callscript2():
	global l
	global i
	i = 2
	print "Wait, process going on"
	l=sentiment2.find_count(file_name)

## function to import a xml file	
def callback():
    name= askopenfilename()
    global file_name_prev
    global file_name
    file_name_prev = file_name
    global i
    #name = os.path.abspath()
    #print name
    #print os.getcwd()
    parent_path = os.getcwd().replace("/Scripts","")
    file_name = name.replace(parent_path,"")[1:]
    file_name = "../" + file_name  
    print "File is imported"

## functio to import database file
def callback2():
    name= askopenfilename()
    parent_path = os.getcwd().replace("/Scripts","")
    name = name.replace(parent_path,"")[1:]
	#file_name = "Database/camera_database.txt"
    input_file = open("../" + name,"r")
    output_file = open("feature_database.py","w")
    for line in input_file:
		output_file.write(line)
    input_file.close()
    output_file.close()
    print "Database file is selected"
    
    
errmsg = 'Error!'
Button(text='Import File', command=callback).pack(fill=X) 
##it needs to be a database file camera_database, phone_database stored in database folder
Button(text='Import Database File', command=callback2).pack(fill=X)
Button(text='Find Count', command=callscript).pack(fill=X)
Button(text='Find Count for a csv file', command=callscript2).pack(fill=X)
Button(text='Make Graph/s', command=make_graph).pack(fill=X)
Button(text='Make Comparison Graph (Before clicking here make sure to import 2 files and database)', command=make_graph2).pack(fill=X)
mainloop()
