#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt,style.use('ggplot')
%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12, 8)


##reeding the data
df = pd.read_csv('movies.csv')