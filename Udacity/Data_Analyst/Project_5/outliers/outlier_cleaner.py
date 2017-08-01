
#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth). This would be in ther variable
        "errors "
        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).

        note predictions is created by predicting the age train (in another py file)
    """

    cleaned_data = []
    # identify and remove the most outlier-y points

    # creates the residual errors
    error = (net_worths - predictions) ** 2

    #for each element
    for idx in range(0,90):
        #arrange the values in this order (this creates an array)
        row = (ages[idx], net_worths[idx], error[idx])

        #append it to cleaned_data
        cleaned_data.append(row)

    #sorts the array
    #lambda is creating a function where the value is sorted by the first item
    #of the 3rd array.
    #reverse the order (hhigh to low)
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2][0], reverse = True)

    #creates a limit, 10% of networths,
    limit = int(len(net_worths)*0.1)

    #reterns cleaned_data with the limit
    return cleaned_data[limit:]
