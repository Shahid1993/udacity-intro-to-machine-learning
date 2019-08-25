#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

print(enron_data)
print('No. of data points:', len(enron_data))
#print(len(enron_data[0].columns))  
"""
Above statement gives KeyError: 0, on execution
Reason :: In Dictionary you can search or print on basis of key value only , it can’t be traversed like array.
"""
print('No. of features:',len(enron_data['GLISAN JR BEN F'].keys()))

print('No. of POIs:', sum(v.get('poi', 0) == 1 for v in enron_data.values()))

"""
Like any dict of dicts, individual people/features can be accessed like so:

enron_data["LASTNAME FIRSTNAME"]["feature_name"]
or, sometimes 
enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]
"""

print(enron_data['PRENTICE JAMES']['total_stock_value'])

print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

#print(max( int(v.get('total_payments')) for v in enron_data.values()))

print('Kenneth Lay Payments:',enron_data['LAY KENNETH L']['total_payments'])

print('No. of people with quantified salary:', sum( v.get('salary') != 'NaN' for v in enron_data.values()))


print('No. of people with known email address:', sum( v.get('email_address') != 'NaN' for v in enron_data.values()))

print('No. of people with NaN in their total_payments:', (sum( v.get('total_payments') == 'NaN' for v in enron_data.values())/len(enron_data))*100)


print('No. of POIs with NaN in their total_payments:', (sum( v.get('total_payments') == 'NaN' and v.get('poi', 0) == 1 for v in enron_data.values())/sum( v.get('poi', 0) == 1 for v in enron_data.values()))*100)
