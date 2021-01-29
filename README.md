# Instacart-Market-Basket-Anlaysis
### 1. Business problem :
Instacart is an American company that operates a grocery delivery and pick-up service in the United States and Canada. The company offers its services via a website and mobile app.
The service allows customers to order groceries from participating retailers with the shopping being done by a personal shopper. 4 years ago instacart hosted a kaggle competition,  In
that they provided the customer prior and last order data(The data is totally anonimized) In this competition   "we have to find which products the user may reorder agian."   The 
problem is a different from recomendation system In this problem we will find based on prior order which product the user will purchase agian

### 2. Data source :
Kaggle : https://www.kaggle.com/c/instacart-market-basket-analysis/data

### 3. Data overview:
Source :  https://www.kaggle.com/c/instacart-market-basket-analysis/data. 
<br/> They have given seven files 
<br/> 1. Aisles.csv : It contains aisle_id and aisle_name of product
<br/> 2. Department.csv : It contains Department Name and department_id of a product
<br/> 3. Products.csv : It contains product_name product_id,Department_id and aisle_id in which product belongs
<br/> 4. order_products__prior.csv : It contains all the prior orders (means all the previous orders) product_d,order_id and reorderd or not of user
<br/> 5. order_products__train.csv : It contains all the train_orers (last orders of train user)  product_d,order_id and reorderd or not of user
<br/> 6. orders.csv  : It contains all the prior, train and test users order_id, days_since_prior_order, order_hour_of_day and order_day_of_week
<br/> 7. sample_submission.csv : It contains all the test order_id and shows the sample of orders of how to submit

### 4. Metric:

Mean F1_score : Here mean f1_score means caluculating f1_score for each order and taking the mean of f1_score of all the orders
<br/> F1(i) = 2*((precision*recall)/(precesion+recall))
<br/> MeanF1_score : 1/N(sigma(for each order in F1(i))

### 5.Train_test_split:
Train_data : Frist take orders_products_train and merge with orders files on left with orders_products_train on Left, then add the prior products of each user from the order_products__prior and keep the reordered equal to zero
<br/>Test_data : From the orders file take all  the test_orderid after geting the order_id with respect to user_id take all of the prior products and merge with orders_id fil
<br/> Cross_validation : From the train_data take all the unique users and split the data for cross_val by taking 20 percent of users in train_data

### 6. Feature_enginering:

<br/> 1.Add none product as reordered ==1 with respect to order_id wherever if the sum of the reordered products of that particular order_id ==0. So that we can also predict None if the user doesn't want to order
<br/> 2.User_product_ratio
<br/> 3.Day of Week reordered_ratio
<br/> 4.Hour_of_day Reordered Ratio
<br/> 5.Days_since_prior_order Reordered ratio
<br/> 6.Product hour of day reordered ratio
<br/> 7.Product_dayofweek Ratio
<br/> 8.User_dow reordered ratio
<br/> 9.User hour reordered_ratio
<br/> 10.Days since prior order for a product
<br/> 11.How many times product reordered by user
<br/> 12. Word2Vectors of products_aisles_departemet of each_product and performed Pca

<br/> After performing this feature engineering stored all these in pkl files and merged with Trian and test_data in 5th step

### 7.Modelling:
<br/> After trying with logistic regression,svm,random_forest,decison_tree i found out Lightgbm performs fast and better so i have done random search hyperparameter to get optimal score
This is shown in modelling ipynb. Done in colab with gpu of 25 gb ram

### References:
https://medium.com/kaggle-blog/instacart-market-basket-analysis-feda2700cded
<br/> https://vishalmendekarhere.medium.com/instacart-market-basket-analysis-challenged-e39d3c550bbd
<br/> https://github.com/alexanderrich/instacart-analysis

### Files:
Flask_demp.mp4 : This project i have implemented with flask have 2 html pages this vedio is demo of flask
<br/>Kaggle_score.png : The kaggle score i got

##### File_order to perform
1 EDA
<br/>2 prior_features
<br/>3 Train_features
<br/>4 Test_features
<br/>5 Modelling
<br/>6 Final_pipeline
<br/>7 app.py(Flask)
