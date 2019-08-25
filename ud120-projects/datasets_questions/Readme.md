### Errors :

- **If you tried using print enron_data[0] it will print KeyError: 0 which means there is no key with 0.**

    *In Dictionary you can search or print on basis of key value only , it can’t be traversed like array.*


- Like any dict of dicts, individual people/features can be accessed like so:  

    `enron_data["LASTNAME FIRSTNAME"]["feature_name"]`  
    or, sometimes   
    `enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]`  