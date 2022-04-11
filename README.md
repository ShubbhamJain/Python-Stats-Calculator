# Python Stats Calculator

### This project is build to calculate probability in python.

Using Numpy we output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix. 

The function we use to calculate  takes a list containing 9 digits. The function converts the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix. 

The returned dictionary follow this format:
```py
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

If the list contains less than 9 elements when passed into the function, it raises a `ValueError` exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.