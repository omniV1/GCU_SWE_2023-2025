#IntrotoML
## Using Pandas to Get Familiar With Your Data

```python 
import pandas as pd
```

The First step is importing pandas library. This is the primary tool in data scientists use for exploring and manipulating data. 

The most important part of the Pandas library is **DataFrame**. 
**DataFrame: holds the type of data you might think of as a table. (Excel / SQL)**

To import training data call the file path as a variable
remember to import pandas as well

<iframe src="https://www.kaggle.com/embed/dansbecker/basic-data-exploration?cellIds=4&kernelSessionId=126670606" height="300" style="margin: 0 auto; width: 100%; max-width: 950px;" frameborder="0" scrolling="auto" title="Basic Data Exploration"></iframe>

## Interpreting Data Description

The results show 8 numbers for each column in your original dataset. The first number, the **count**, shows how many rows have non-missing values.

Missing values arise for many reasons. For example, the size of the 2nd bedroom wouldn't be collected when surveying a 1 bedroom house. We'll come back to the topic of missing data.

The second value is the **mean**, which is the average. Under that, **std** is the standard deviation, which measures how numerically spread out the values are.

To interpret the **min**, **25%**, **50%**, **75%** and **max** values, imagine sorting each column from lowest to highest value. The first (smallest) value is the min. If you go a quarter way through the list, you'll find a number that is bigger than 25% of the values and smaller than 75% of the values. That is the **25%** value (pronounced "25th percentile"). The 50th and 75th percentiles are defined analogously, and the **max** is the largest number.