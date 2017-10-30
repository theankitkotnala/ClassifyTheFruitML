# Import tree from the sklearn library so that you can use that to train your data 
from sklearn import tree


#Extract your feature from the object on which behave you are training the tree to pridect your  result , here i extracted the feature from the fruits such as - texture and wieght .

features = [[150, 0], [170, 0], 
            [140, 1],[130, 1], [150,1]]
labels = ["orange", "orange",
          "apple", "apple","apple"]

# Declare your classifier here using the DecisionTreeClassifier Method 
clf = tree.DecisionTreeClassifier()

#Train your classifier using thr extracted feature with the help of the fit Method 
clf = clf.fit(features, labels)

#asking for the data on which your classifier has to predict 
weight = input("Enter the weight : ")
texture = input("Enter the Texture of the fruit : ")

# At the end just print out the prediction using the predict Method 
print ("The fruit  you are searching for is :")
print(clf.predict([[weight, texture]]))


