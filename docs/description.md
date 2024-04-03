# Description 

<img src="https://www.maritimecyprus.com/wp-content/uploads/2015/10/titanic-infographic-696x431.jpg" width="650" >


## The Challenge

The sinking of the [Titanic](https://en.wikipedia.org/wiki/Titanic) is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

In this challenge, we ask you to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).


## Dataset Description

### Overview

The data has been split into two groups:

*   training set (`train.csv`)
*   test set (`test.csv`)

**The training set** should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use [feature engineering](https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/) to create new features.

**The test set** should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

We also include **gender\_submission.csv**, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.

### Data Dictionary

| Variable Name | Definition                          | Possible Values                                |
|---------------|-------------------------------------|------------------------------------------------|
| `survival`    | Survival status                     | 0 (No), 1 (Yes)                                |
| `pclass`      | Passenger class                     | 1 (1st), 2 (2nd), 3 (3rd)                      |
| `sex`         | Gender                              | Male, Female                                   |
| `age`         | Age in years                        | Numerical                                      |
| `sibsp`       | Number of siblings/spouses on board | Numerical                                      |
| `parch`       | Number of parents/children on board | Numerical                                      |
| `ticket`      | Ticket number                       | String                                         |
| `fare`        | Passenger fare                      | Numerical                                      |
| `cabin`       | Cabin number                        | String (may contain missing values)            |
| `embarked`    | Port of embarkation                 | C (Cherbourg), Q (Queenstown), S (Southampton) |



### Variable Notes

**pclass**: A proxy for socio-economic status (SES)  

* 1st = Upper  
* 2nd = Middle  
* 3rd = Lower  
  
**age**: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5  
  
**sibsp**: The dataset defines family relations in this way... 

* Sibling = brother, sister, stepbrother, stepsister  
* Spouse = husband, wife (mistresses and fiancés were ignored)  
  
**parch**: The dataset defines family relations in this way...  
* Parent = mother, father  
* Child = daughter, son, stepdaughter, stepson  
* Some children travelled only with a nanny, therefore parch=0 for them.

> 🔑 **Note**: For more details about the project, please see the [Kaggle documentation](https://www.kaggle.com/c/titanic/overview) on the Titanic challenge.