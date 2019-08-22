## Results of DecisionTreeClassifier

**Observation 1:** 

- *min_samples_split=40*  
    no. of Chris training emails: 7936  
    no. of Sara training emails: 7884 
    no. of features:  3785
    accuracy: 0.9778156996587031

**Observation 2:** 

- *min_samples_split=40*  
    no. of Chris training emails: 7936  
    no. of Sara training emails: 7884 
    no. of features: 379 
    accuracy: 0.9658703071672355


**Changing the no. of features**
    ```python
    #selector = SelectPercentile(f_classif, percentile=10)
    selector = SelectPercentile(f_classif, percentile=1)
    ```