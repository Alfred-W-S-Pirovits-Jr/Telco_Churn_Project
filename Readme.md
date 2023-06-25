# <a name="top"></a>TELCO CHURN 
![]()

by: Alfred W. Pirovits

<p>
  <a href="https://github.com/mdalton87" target="_blank">
    <img alt="Matthew" src="https://img.shields.io/github/followers/mdalton87?label=Follow_Matt&style=social" />
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
The purpose of this project is to determaine the main drivers of churn for the Telco Company and try and build a model that can predict, based on chosen factors, which customers will turn over and leave the company.  The analysis included looking at some 43 variables and determining which are most predictive of whether or not Telco will retain a customer.  Many of these were redundant columns.  Of those left, twenty one of showed a significant debendance between that variable and whether or not a customer churns.  The goals were to determine which of these factors had the most significant impact on customer retention.
***
## <a name="planning"></a>Project Planning:    
[[Back to top](#top)]
The main goal of the project was to explore the data presented and see what I could discover.  Since there was a lot of data to go through, the main plan of the project was one of discovery.

### Project Outline:
- Explore the enormous dataset to find patterns
- Organize features creating dummies where appropriate and eliminating redundant features

        
### Hypothesis
There were many hypotheses, however the general meta hypothesis was whether or not a churn was dependent on the features chosen one by one.  The general Null hypothesis was that the given feature and the target (churn_Yes) were independant while the Alternate Hypothesis was that they were dependent.  An alpha of 0.01 was chosen given the number of observations there were and the fact that there were so many features to choose from to analyze.  A secondary hypothesis was that there would be quite a few confounders in the dataset, but it proved difficult to extract the main drivers as it seemed difficult almost untenable to find the main driving factors amongst the sea of contributing factors.  In the end I found a combination of two factors which seemed to really be the driving force behind it all.   


### Target variable
The target variable is churn_Yes, coded in boolean 0 or 1.  Zero for false and 1 for True.  


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
The key basic finding is that the most important driver of churn seems to be the relationship between how much customers pay and how long they have been customers.  Newer customers who pay more per month clearly leave at a significant rate while old customers who pay the least tend to stay.

One thing to look at in the future is the viability of the Month-to-month contract.  This feature had the lowest p-value when compared to the churn column of any of the features with a result of ten to the minus 256 power.  

Now some may say that p-value does not indicate "more significance" however we should revisit what a p-value is.  It is the probability that this result would happen by chance if the Null Hypothesis were true.  This combined with the result about new customers churning at a higher rate seems to point to the fact that Telco needs to do something about the new customers if they wish to retain more of them.  One would be to lower their costs and another would seem to be to lock the customers into a longer term contract.  Presumably the month-to-month contract exists to entice customers to try out the service and that a higher turnover is to be expected.  However, a more in depth cost to benefit analysis is required to try and figure out if this is a good strategy or not.



***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

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

### Stats Test 1: ANOVA Test: One Way

Analysis of variance, or ANOVA, is a statistical method that separates observed variance data into different components to use for additional tests. 

A one-way ANOVA is used for three or more groups of data, to gain information about the relationship between the dependent and independent variables: in this case our clusters vs. the log_error, respectively.

To run the ANOVA test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> f_oneway

- f_oneway, in this case, takes in the individual clusters and returns the f-statistic, f, and the p_value, p:
    - the f-statistic is simply a ratio of two variances. 
    - The p_vlaue is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:


#### Summary:


### Stats Test 2: T-Test: One Sample, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare the individual clusters to the total population. 
    - Cluster1 to the mean of ALL clusters
    - Cluster2 to the mean of ALL clusters, etc.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:

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