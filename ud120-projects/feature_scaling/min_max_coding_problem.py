def featureScaling(arr):
    nmax = max(arr)
    nmin = min(arr)

    if (nmax == nmin):
        return [0.5 for e in arr ]
    normalize = nmax - nmin
    return [float(e-nmin)/normalize for e in arr ]


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print (featureScaling(data))


data2 = [200, 200, 200]
print (featureScaling(data2))