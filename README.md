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

So far the accuracy is not perfect 0.934 Most common mistake is Surname/GivenName. 
All mistakes from the evaluation dataset:
```
True: 
[('Surname', 'HOOPER'), ('SuffixGenerational', 'SR,'), ('GivenName', 'BARRON')]
Predicted: 
[('GivenName', 'HOOPER'), ('SuffixGenerational', 'SR,'), ('GivenName', 'BARRON')]
True: 
[('Surname', 'RAMIREZ,'), ('GivenName', 'PATRICIA'), ('MiddleInitial', 'M')]
Predicted: 
[('Surname', 'RAMIREZ,'), ('GivenName', 'PATRICIA'), ('LastInitial', 'M')]
True: 
[('Surname', 'RODRIGUEZ'), ('SuffixGenerational', 'JR,'), ('GivenName', 'FRANCISCO')]
Predicted: 
[('GivenName', 'RODRIGUEZ'), ('SuffixGenerational', 'JR,'), ('GivenName', 'FRANCISCO')]
```
Another examples:
```
Initial string: Mikhail Saakashvili
[('GivenName', 'Mikhail'), ('Surname', 'Saakashvili')]

Initial string: Saakashvili Mikhail
[('GivenName', 'Saakashvili'), ('Surname', 'Mikhail')]

Initial string: Saakashvili, Mikhail
[('Surname', 'Saakashvili,'), ('GivenName', 'Mikhail')]

Initial string: Mikhail, Saakashvili
[('Surname', 'Mikhail,'), ('GivenName', 'Saakashvili')]

Initial string: John Bonzo Bonham
[('GivenName', 'John'), ('MiddleName', 'Bonzo'), ('Surname', 'Bonham')]

Initial string: John "Bonzo" Bonham
[('GivenName', 'John'), ('Nickname', '"Bonzo"'), ('Surname', 'Bonham')]

Initial string: Anne-Caroline Chausson
[('GivenName', 'Anne-Caroline'), ('Surname', 'Chausson')]

Initial string: Chausson Anne-Caroline
[('GivenName', 'Chausson'), ('GivenName', 'Anne-Caroline')]

Initial string: Slash
[('GivenName', 'Slash')]

Initial string: "Slash"
[('GivenName', '"Slash"')]

Initial string: Jack White III
[('GivenName', 'Jack'), ('MiddleName', 'White'), ('SuffixGenerational', 'III')]

Initial string: Cheng Long
[('GivenName', 'Cheng'), ('Surname', 'Long')]

Initial string: Li Lianjie
[('GivenName', 'Li'), ('Surname', 'Lianjie')]

Initial string: Ma Yun
[('GivenName', 'Ma'), ('Surname', 'Yun')]

Initial string: Rajesh Khanna
[('GivenName', 'Rajesh'), ('Surname', 'Khanna')]

Initial string: Khanna Rajesh
[('GivenName', 'Khanna'), ('Surname', 'Rajesh')]
```


This is possibly caused by:
 - Small dataset in which pattern GivenName/Surname is more frequent than other combinations
 - Class disbalance with higher number of GivenName examples

* Optimization

A feature vector for the input contains 804 features, but ~50% of these are not used for prediction. 
This issue could be resolved with a feature selection algorithm.

* Hyperparameter tuning

An XGB model hyperparameter tuning can be a very time-consuming task, which in the other hand can give an improvement to 
algorithm performance. This step is skipped so far and to be implemented in th future.