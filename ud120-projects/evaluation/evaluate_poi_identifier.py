#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, classification_report, confusion_matrix

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys_unix.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here 
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

print(clf.score(features_test, labels_test))

# How many POIs are in the test set for your POI identifier?
pred = clf.predict(features_test)

print (len([e for e in labels_test if e == 1.0]))
#or
print(sum(pred))

# How many people total are in your test set?

print(len(features_test))
#or
print(len(pred))


# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print(1.0 - 4.0/29)
#or
print(pred.tolist().count(0) / float(len(pred)))


# Do you get any true positives? (In this case, we define a true positive as a case where both the actual label and the predicted label are 1)
true_positives = 0
for i in range(len(pred)):
	if (pred[i] == labels_test[i]) and labels_test[i] == 1:
		true_positives += 1

print(true_positives)

print ("Precision score:", precision_score(labels_test, pred))
print ("Recall score:", recall_score(labels_test, pred))

print(classification_report(pred, labels_test))



predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

cm = confusion_matrix(true_labels, predictions)

print(cm)

print (cm, '\n')
print ('{0} True positives'.format(cm[1][1]))
print ('{0} True negatives'.format(cm[0][0]))
print ('{0} False positives'.format(cm[0][1]))
print ('{0} False negatives'.format(cm[1][0]))

print(precision_score(true_labels, predictions))
print(recall_score(true_labels, predictions))