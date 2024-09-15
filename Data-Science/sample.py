# Predict male or female by studying a dataset containgin height , weight and shoe size 

from sklearn import tree 

#[hieght , weight , shoe size]

x= [[180,50,44],[175,60,42],[185,80,46],[175,75,44], [178,74,40]]

y = ['male', "female","male","male", "female"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

prediction = clf.predict([[192,55,40]])

print(prediction)