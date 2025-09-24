#IntrotoML
## Selecting Data for Modeling 

To choose variables/columns, we'll need to see a list of all columns in the dataset. That is done with the **columns** property of the DataFrame (the bottom line of code below)
Input:
```python
import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
Output: 
```plaintext
Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
       'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
       'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
       'Longtitude', 'Regionname', 'Propertycount'],
      dtype='object')
```

Input
```python
# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
```

## Selecting the Prediction Target

You can select a variable with the dot-notation. This single column is stored in a Series, which is broadly like a DataFrame with only a single column of data. 

The column specified with dot-notation is called a **prediction target**

By convention, the **Prediction Target** is called **y**. 

```python
y = melbourne_data.Price
```

## Choosing "Features"

The columns that are inputted into our model are called **Features**. The columns will be used to determine the home price. Sometimes, you will use all columns except the target as features. Other times youll be better off with fewer features. 

Example
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

by convention data is called X

Example
```python
X = melbourne_data[melbourne_features]
```

Using the **describe** to see house prices and **head** method to show the top few rows. 
```python
X.describe()
```

**output:** 

|Rooms|Bathroom|Landsize|Lattitude|Longtitude|
|---|---|---|---|---|
|count|6196.000000|6196.000000|6196.000000|6196.000000|6196.000000|
|mean|2.931407|1.576340|471.006940|-37.807904|144.990201|
|std|0.971079|0.711362|897.449881|0.075850|0.099165|
|min|1.000000|1.000000|0.000000|-38.164920|144.542370|
|25%|2.000000|1.000000|152.000000|-37.855438|144.926198|
|50%|3.000000|1.000000|373.000000|-37.802250|144.995800|
|75%|4.000000|2.000000|628.000000|-37.758200|145.052700|
|max|8.000000|8.000000|37000.000000|-37.457090|145.526350|

```python 
X.head()
```

**output:** 

|Rooms|Bathroom|Landsize|Lattitude|Longtitude|
|---|---|---|---|---|
|1|2|1.0|156.0|-37.8079|144.9934|
|2|3|2.0|134.0|-37.8093|144.9944|
|4|4|1.0|120.0|-37.8072|144.9941|
|6|3|2.0|245.0|-37.8024|144.9993|
|7|2|1.0|256.0|-37.8060|144.9954|


## Building Your Model

Scikit-learn library will create our models. When coding the library is written as sklearn. This is the most popular library for modeling the types of data typically stored in DataFrames. 

The steps to build a model follows:

1. **Define**: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too. 
2. **Fit**: Capture patterns from provided data. This is the heart of modeling.
3. **Predict**: Just what it sounds like
4. **Evaluate**: Determine how accurate the models predictions are

Example: 
```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

output: 
```
DecisionTreeRegressor(random_state=1)
```

Specifying the random_state ensures you get the same result in each run. This is considered good practice. Any number will work here so long as it stays that number. 

With that fitted model we now can make predictions. 

```python
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
```

Output: 
Making predictions for the following 5 houses:
   Rooms  Bathroom  Landsize  Lattitude  Longtitude
1      2       1.0     156.0   -37.8079    144.9934
2      3       2.0     134.0   -37.8093    144.9944
4      4       1.0     120.0   -37.8072    144.9941
6      3       2.0     245.0   -37.8024    144.9993
7      2       1.0     256.0   -37.8060    144.9954
The predictions are
[1035000. 1465000. 1600000. 1876000. 1636000.]```
```