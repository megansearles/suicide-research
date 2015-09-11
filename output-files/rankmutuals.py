from sklearn import linear_model
import numpy

train_X = numpy.loadtxt('test.csv', delimiter=',',usecols = (1,2,3,4))
train_y = numpy.loadtxt('test.csv', delimiter=',',usecols = [0], unpack=True)

lm = linear_model.LinearRegression()
lm.fit(train_X, train_y)

init_screen = raw_input("Which user do you want to look at? ")
test = numpy.loadtxt('%s.csv' % init_screen, delimiter=',')
test_X = numpy.loadtxt('%s.csv' % init_screen, delimiter=',', usecols=(1,2,3,4))
test_y = lm.predict(test_X)
#test_y_tp = numpy.transpose(test_y)
	#For some reason I couldn't get transpose to work like I wanted it to
test_yt = []
for item in test_y:
	test_yt.append([item])

test2 = numpy.append(test,test_yt,axis=1)
test2 = test2[test2[:,5].argsort()[::-1]]

numpy.savetxt('ranked-%s.csv' % init_screen,test2,delimiter=',',newline='\n')