## Errors in Udacity Code :

- In  `email_preprocess.py` file

    `from sklearn import cross_validation` changed to `from sklearn.model_selection import train_test_split`

- **TypeError: a bytes-like object is required, not ‘str’**  
    or:  
    **ValueError: could not convert string to float**  
    or:  
    **UnpicklingError: the STRING opcode argument must be quoted**  

    The problem is caused when files written in Unix are used in Windows, or vice versa.
    Use below function for each such file (replacing by appropriate file names):

    ```python
    #!/usr/bin/env python
    """\
    convert dos linefeeds (crlf) to unix (lf)
    usage: dos2unix.py <input> <output>
    """
    original = "word_data.pkl"
    destination = "word_data_unix.pkl"

    content = ''
    outsize = 0
    with open(original, 'rb') as infile:
    content = infile.read()
    with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

    print("Done. Saved %s bytes." % (len(content)-outsize))
    ```