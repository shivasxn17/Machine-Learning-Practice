from sklearn import tree

clf = tree.DecisionTreeClassifier()

# height and weight of person
X = [[170,65],[160,54],[180,70],[166,57],[190,80],[170,60],[160,51]]
y = ['male','female','male','female','male','female','female']

clf = clf.fit(X, y)

prediction = clf.predict([[182,70]])

print(prediction)
