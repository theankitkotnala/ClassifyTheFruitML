from sklearn import tree

features = [[150, 0], [170, 0], 
            [140, 1],[130, 1], [150,1]]
labels = ["orange", "orange",
          "apple", "apple","apple"]

weight = input("Enter the weight : ")
texture = input("Enter the Texture of the fruit : ")

print ("The fruit  you are searching for is :")
print(clf.predict([[weight, texture]]))


