# <a name="top"></a>TELCO CHURN 
![]()

by: Alfred W. Pirovits

<p>
  <a href="https://github.com/Alfred-W-S-Pirovits-Jr/telco_churn_project#top" target="_blank">
    <img alt="" src="" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

<img src="https://docs.google.com/drawings/d/e/2PACX-1vR19fsVfxHvzjrp0kSMlzHlmyU0oeTTAcnTUT9dNe4wAEXv_2WJNViUa9qzjkvcpvkFeUCyatccINde/pub?w=1389&amp;h=410">

## <a name="project_description"></a>Project Description:
[[Back to top](#top)]
The purpose of this project is to determaine the main drivers of churn for the Telco Company and try and build a model that can predict, based on chosen factors, which customers will turn over and leave the company.  The analysis included looking at some 43 variables and determining which are most predictive of whether or not Telco will retain a customer.  Many of these were redundant columns.  Of those left, twentytwo of showed a significant dependance relationship between that variable and whether or not a customer churns.  The goals were to determine which of these factors had the most significant impact on customer retention.
***
## <a name="planning"></a>Project Planning:    
[[Back to top](#top)]
The main goal of the project was to explore the data presented and see what I could discover.  Since there was a lot of data to go through, the main plan of the project was one of discovery.

### Project Outline:
- Explore the enormous dataset to find patterns
- Organize features creating dummies where appropriate and eliminating redundant features
- Run analysis to see what features are correlated/dependent to the target churn_Yes
- Try and determine which factors are driving churn and which factors are more Confounding

        
### Hypothesis
There were many hypotheses, however the general meta hypothesis was whether or not a churn was dependent on each of  the features chosen one by one.  The general Null hypothesis was that the given feature and the target (churn_Yes) were independant while the Alternate Hypothesis was that they were dependent.  An alpha of 0.01 was chosen given the number of observations there were and the fact that there were so many features to choose from to analyze.  A secondary hypothesis was that there would be quite a few confounders in the dataset, but it proved difficult to extract the main drivers as it seemed difficult almost untenable to find the main driving factors amongst the sea of contributing factors.  In the end I found a combination of two factors which seemed to really be the driving force behind it all.   


### Target variable
The target variable is churn_Yes, coded in boolean 0 or 1.  Zero for False and 1 for True.  


### Need to haves (Deliverables):
Github repo with the following:

1. Readme (.md)
- project description with goals
- initial hypotheses and/or questions you have of the data, ideas
- data dictionary
- project planning (lay out your process through the data science pipeline)
- instructions or an explanation of how someone else can reproduce your project and findings (What would someone need to be able to recreate your project on     their own?)
- key findings, recommendations, and takeaways from your project

2. Final Report (.ipynb)
- A Report that has filtered out all the extraneous elements not necessary to include in the report.
- Use markdown throughout the notebook to guide the audience. Assume the reader will not read your code blocks as you think about how much markdown guidance do you need.
- Then, assume another reader will read ALL of your code, so make sure it is very very clearly commented. All cells with code need comments.
- Your notebook should begin with a project overview and goals
- Preparation should specifically call out any ways you changed the data (like handling nulls)
- Provide the context of the target variable through a visualization (distribution of the values, e.g.)
- Exploration should be refined in the report because now you know which visualizations and tests led to valuable outcomes.
- Include at least 4 visualizations in the form of:
- Question in markdown that you want to answer
- Visualization
- Statistical test (in at least 2 of your 4)
- Provide your clear answer or takeaway in markdown and natural language to the question based on your exploration
- Include your 3 best models in the final notebook to review. Show the steps and code you went through to fit the models, evaluate, and select.
- On your best model, a chart visualizing how it performed on test would be valuable.
- End with a conclusion that talks about your original goals and how you reached those (or didn't), the key findings, recommendations and next steps ("If I had more time, I would...")

3. Acquire & Prepare Modules (.py)
- contains functions to acquire, prepare and split your data. You can have other .py files if you desire to abstract other code away from your final report.
- Your work must be reproducible by someone with their own env.py file.
- Each of your functions are complimented with docstrings. If they are functions you borrowed from instructors, put those docstrings in your own words.
- Functions to acquire and prepare your data should be imported and used in your final report.

4. Predictions (.csv).
3 columns: customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn).
These predictions should be from your best performing model ran on X_test.
Note that the order of the y_pred and y_proba are numpy arrays coming from running the model on X_test. The order of those values will match the order of the rows in X_test, so you can obtain the customer_id from X_test and concatenate these values together into a dataframe to write to CSV.

5. non-final Notebook(s) (.ipynb)
there should be at least 1 non-final notebook
these were created while working on the project, containing exploration & modeling work (and other work), not shown in the final report



### Nice to haves (With more time):
With more time, I would have liked to explore how I could combine multiple models to create a better result.  I thought of adding weights to the final predicted probability matricies and combining them in such a way to create a weighted average of the four tests.  I also thought of finding a way of running a for loop through the pred_proba matrix for one test, say the tree that extracts all rows that have a probability greater than .9, into a train set and then running the rest of the rows through a second test like knn and running through all the remaining tests, until i have three or four train sets, each with as much certaintanty about its predictions as possible.  Once I do this I would try the same with the validate and if the results are similar, I would run a test hopefully coming up with a better result than any individual test.  



***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]
The key basic finding is that the most important driver of churn seems to be the relationship between how much customers pay and how long they have been customers.  Newer customers who pay more per month clearly leave at a significant rate while old customers who pay the least tend to stay.  Thus I created a new column representing the tenure to monthly charge ratio and saw this as even stronger than the next driver being the Month-to-month contracts.

One thing to look at in the future is the viability of the Month-to-month contract since this is highly correlated with the high paying new customer.  This feature had the lowest p-value when compared to the churn column of any of the original features with a p-value on the order of ten to the minus 256 power.  

Now some may say that p-value does not indicate "more significance" however we should revisit what a p-value is.  It is the probability that this result would happen by chance if the Null Hypothesis were true.  This combined with the result about new customers churning at a higher rate seems to point to the fact that Telco needs to do something about the new customers if they wish to retain more of them.  One would be to lower their costs and another would seem to be to lock the customers into a longer term contract or entice them to purchase additional services.  Presumably the month-to-month contract exists to entice customers to try out the service and that a higher turnover is to be expected.  However, a more in depth cost to benefit analysis is required to try and figure out if this is a good strategy or not.



***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| senior_citizen | Whether the Customer is a Senior Citizen | int64 |
| partner_Yes | Whether the Customer has a Partner| uint8 |
| dependents_Yes | Whether the Customer has dependents | uint8 |
| multiple_lines_Yes | Whether the Customer has multiple lines | uint8 |
| online_security_Yes | Whether the Customer has subscribed to Online Security | uint8 |
| online_backup_Yes | Whether the Customer has subscribed to Online Backup | uint8 |
| device_protection_Yes | Whether the Customer has Opted into Device Protection | uint8 |
| tech_support_Yes | Whether the Customer has Utilized Tech Support | uint8 |
| streaming_tv_Yes | Whether the Customer has purchased Streaming TV | uint8 |
| streaming_movies_Yes | Whether the Customer has purchased Streaming Movies| uint8 |
| paperless_billing_Yes | Whether the Customer has Enrolled in Paperless Billing | uint8 |
| churn_Yes | TARGET - Whether the Customer has Churned or Not | uint8 |
| internet_service_type_Fiber optic | Whether the Customer has Purchased Fiber Optic Internet | uint8 |
| internet_service_type_None | Indicates Whether the Customer has Opted out of Having Internet Service| uint8 |
| payment_type_Credit card (automatic) | Whether the Customer Pays by Credit Card | uint8 |
| payment_type_Electronic check | Whether the Customer Pays by Electronic Check | uint8 |
| payment_type_Mailed check | Whether the Customer Pays by Mailed in Check | uint8 |
| contract_type_Month-to-month | Whether the Customer has a Month-to-Month Contract Type | uint8 |
| contract_type_One year | Whether the Customer has a One Year Contract Type  | uint8 |
| contract_type_Two year | Whether the Customer has a Two Year Contract Type | uint8 |
| tenure_charge_ratio | The Ratio of Customer Tenure over Monthly Charge Amount | float64 |
| tenure_normalized | Normalized Length the Customer is with Telco | float64 |
| monthly_charges_normalized | Normalized Monthly Charges | float64 |

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: Chi Squared Test

The main statistical test used was the Chi Squared Test to determine dependence between the target variable churn_Yes and the features.  A for loop was used to run the Chi Squared test for each column that was a feature as compared to the target.  

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is that the target column (Churn_Yes) is independent of the column in question
- The alternate hypothesis (H<sub>1</sub>) is that the target column (Churn_Yes) is dependent on the column in question

#### Confidence level and alpha value:
- For the purposes of these tests, I used an alpha < 0.01 since the number of customers was high and there were so many features to choose from.

#### Results:
After removing the redundant columns in the original dataframe; "Unnamed: 0", "gender_male", "phone_service_Yes", "multiple_lines_No phone service" all did not meet the p-value we set and thus we didn't have sufficient evidence to reject the null hypothesis. I therefore dropped them all from the analysis. 

"Unnamed: 0" is just an id number so it makes sense that they are independant events...kinda goes without saying but a good sanity check.

#### Summary:
This left us with 22 features and one target to work with which are as follows:
'senior_citizen', 
'partner_Yes', 
'dependents_Yes', 
'multiple_lines_Yes',
'online_security_Yes', 
'online_backup_Yes', 
'device_protection_Yes',
'tech_support_Yes', 
'streaming_tv_Yes', 
'streaming_movies_Yes',
'paperless_billing_Yes',
'internet_service_type_Fiber optic', 
'internet_service_type_None',
'payment_type_Credit card (automatic)', 
'payment_type_Electronic check',
'payment_type_Mailed check', 
'contract_type_Month-to-month',
'contract_type_One year', 
'contract_type_Two year', 
'tenure_normalized',
'monthly_charges_normalized', 
'churn_Yes'

### Stats Test 2: Pearson Correlation
- Looking at the scatterplot of the monthly charges vs tenure hued on churn, I decided that the tenure to charge ratio was an interesting new column I could make since it seemed new customers who pay a lot of money churn.  
- I ran the Pearsonr Correlation test on the monthly charges and tenure in order to see how strong the correlation was
#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is  that there was no correlation
- The alternate hypothesis (H<sub>1</sub>) is  that there is some correlation
- An alpha < 0.05 was chosen
    - An r value of 0.401285600132126 indicated a moderate correlation while
    - The p-value of 3.0121978116585465e-73 showed a significant result
    
Thus I felt confident making the new column 'tenure_charge_ratio' as an added feature.  I also thought that this correlation might be stronger under a non-linear correlation test so I moved on to Spearman's Correlation


### Stats Test 3: Spearman Correlation
- It was quite obvious that the regression line would be better fit if it were not linear.  So I ran a Spearman's Correlation test to make sure.  A stronger correlation with a curve bent toward the newest customers paying the most would present more evidence that using the newly made column would prove fruitful.


- I ran the Spearman's Correlation test on the monthly charges and tenure in order to see how strong the correlation was
#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is  that there was no correlation
- The alternate hypothesis (H<sub>1</sub>) is  that there is some (monotonically incresasing or decreasing) correlation
- Again an alpha < 0.05 was chosen
    - An r value of 0.4843751919531249 indicated a moderate but stronger correlation while
    - The p-value of 1.5136016239109236e-110 showed a significant result
-  These two tests combined convinced me that I was on the right track so I continued all models with this new column as an added feature
    


#### Results:
All of the columns seemed highly correlated to the target variable.  However so many of the columns seemed to be confounding features to the main two drivers of the entire thing.  It is clear that the more that the customers pay per month and the shorter timeframe that they have been customers is a main driving force behind churn.  Secondary to this and also slightly confounding is whether or not the customers were on a Month-to-Month contract, which in terms of the original features had the most significant result upon the chi squared test.   


#### Summary:
That said it is difficult to rigorously rule out the confounding variables with the tools we have used up to this point in the course.  As such I am forced to rely on intuition to guess what the main drivers are.  The fact that the two that I have chosen are of high priority in the decision trees that I looked at as well as the fact that many of the columns seem to naturally clump together like having dependents and having multiple services and lines and thus being on a long term conract seem a natural consequence of the interrelated nature of these columns.  

Given more time I would try to seperate out these confounding features more and see if I could get a more comprehensive picture on how these features clump together.  I did try a nested for loop to see if any columns were independent of others using the chi squared test.  That double loop was in my original exploration work and I used an alpha of .75.  This is not a statistical result per se but I just used a high alpha to see if I could extract out the columns that seem to be independent of any of the other columns.  I was then left with a set of columns that are totally dependent on all other columns and another set of columns that have less dependence on at least one other column.   Such an inquiry came up empty as there were time considerations, but I would, if given more time explore this further.  

Also another driver seemed to be fiber optic.  There seemed to be a high proportion of fiber optic customers that were dissatisfied.  Interestingly enough the fiber optic ended up in the independent column which seems to indicate that it is a standalone feature that causes dissatisfaction.  There seeems to be less confounding factors with this feature.  Perhaps a deeper analysis into this feature will lead to stronger conclusions as to what is going on there.

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]