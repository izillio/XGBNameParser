# XGBoost Name Parser

XGBoost Name Parser is a research version of name parsing algorithm based on 
the discriminative classifier approach. It works only with names written in latin alphabet.

Example of usage:
```
INPUT: Dr. Jack Ali Reisenfeld-Rozumovsky II Jr.
OUTPUT: [('PrefixOther', 'Dr.'), ('GivenName', 'Jack'), ('MiddleName', 'Ali'), ('Surname', 'Reisenfeld-Rozumovsky'), ('SuffixGenerational', 'II'), ('SuffixGenerational', 'Jr.')]
```

#### How to run the code:
1. Clone the repo.
2. Build the docker image using docker-compose file
```
docker-compose build name_extractor
```
3.1 Running in the notebook:
Use the following command to run JupyterNotebook server:
```
docker-compose up name_extractor
```
The script for evaluation is in: *./notebooks/evaluation.ipynb* 

3.2 Use the cmd command:
```
docker-compose run extractor python ./parse.py --name 'Alexander II "The Great"'
```

# Things TODO:
* Accuracy improving 

So far the accuracy is not perfect 0.91 Most common mistake is Surname/GivenName. 
This is possibly caused by class disbalance and lack of valuable features for robust segregation of those two classes.

* Optimization

A feature vector for the input contains 639 features, but ~60% of these are not using for prediction. 
This issue could be resolved with a feature selection algorithm.

* Hyperparameter tuning

An XGB model hyperparameter tuning can be a very time-consuming task, which in the other hand can give an improvement to 
algorithm performance. This step is skipped so far and to be implemented in th future.