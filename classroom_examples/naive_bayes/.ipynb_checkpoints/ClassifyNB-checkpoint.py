from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    clf = GaussianNB()
    #print('---------')
    #clf = SVC(kernel="rbf", C=1)
    #print(clf)
    clf.fit(features_train, labels_train)
    return clf
    ### your code goes here!
    
    