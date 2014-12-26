import pylab as pl
import numpy as np
from sklearn import linear_model
import sentiment2
## function to apply regression model between feature count and customer rating

def apply_regress(inputfile):
	count1 = sentiment2.find_count(inputfile)
	#count1 = sentiment2.find_count("CSV_files/regress_data.csv")
	regr = linear_model.LinearRegression()
	y_train = []
	x_train = []
	y_test = []
	x_test = []
	sz = len(count1)
	sz1 = len(count1[0])
	for i in range(0,sz):
		if i < 6*sz/7 :
			y_train.append(10*count1[i][sz1-1])
			x_dum = []
			for j in range(0,sz1-1):
				x_dum.append(count1[i][j][0] + count1[i][j][1] + count1[i][j][2])
			x_train.append(x_dum)
		else :
			y_test.append(10*count1[i][sz1-1])
			x_dum = []
			for j in range(0,sz1-1):
				x_dum.append(count1[i][j][0] + count1[i][j][1] + count1[i][j][2])
			x_test.append(x_dum)
				
		
	regr.fit (x_train,y_train)
	print('Coefficients: \n', regr.coef_)
	#LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
	#print clf.coef_array
	# The mean square error
	print("Residual sum of squares: %.2f"
		  % np.mean((regr.predict(x_test) - y_test) ** 2))
	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.2f' % regr.score(x_test, y_test))

#apply_regress("CSV_files/regress_data.csv")
