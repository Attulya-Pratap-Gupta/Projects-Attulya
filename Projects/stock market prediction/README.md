Finance & Econ 2
-Everyone in general helped in presentation
Bonnema, Colin - Helped Create ARMA Model
Gupta, Attulya - Created Data Importation,exploritory analysis, and LSTM model
Mandell, Jack - Created ARIMA Model to be used and framework for AR and ARMA Models
Sahai, Jayant - Helped Create AR Model and did a lot of the presentation in terms of math explanations too
Vondersitt, Brit - Did SVR model along with some others that weren't included in final draft, added confusion matrices and accuracy score
# ABSTRACT
### Introduction
In the intricate and fast-paced world of finance, stock market prediction using machine learning stands out as a crucial endeavor, blending advanced analytics with economic expertise. This approach is not merely about charting the course of stock prices but delves into a series of concrete, data-driven questions that underpin strategic investment decisions. The key question we seeked to answer was what were the differences between popular prediction models and what model is generally the best at predicting the stock price and whats in MSE for the Finance and Utility sector of the market.
To answer this question we first downloaded and loaded up stock data from yahoo finance and formatted it in a usable manner for our models.  Next we used the utilities dataset to run each model to and compared the MSE against eachother and then the best two models would then be compared using some of the other datasets to get a more representative comparison.  The models selected were among the most widely used with a learning curve to use that can be learned without too much technical knowledge.

### Run Instructions:
- Make sure that all required packages are downloaded, user may have to pip install packages that are not downloaded. See here on documentation to pip install: https://packaging.python.org/en/latest/tutorials/installing-packages/
- After packages installed run documents to download datasets as seen below.
- Run each model, note this will take roughly 10-15 minutes to complete.
- Notice results from models

- Debugging: Some users encountered issues when running LSTM model, this maybe caused by Operating System of Graphics Card.  Running on google collab fixes this.  Jupyerhub isn't using correct OS/GPU. Another reason for issues with LSTM model is numpy and tensorflow dependency issue. Use numpy==1.19.5 and tensorflow==2.4.1

### Sections

- Imports

- Data Importation and Manipulation

- Exploratory Analysis

- Initial Comparisom

- Final Comparison

- Results

- Conclusion

- Citations

### Imports

The imports selected for this project were the yfinance dataset to get recent and accurate data from yahoo finance on stocks mainly the opening and closing prices.  The opening price is the price of a stock at the beggining of the trading day (from 9:30am - 4pm).  The closing price is the price at the end of the day.  This is what we are attempting to predict given a days open.  Our models were created with statsmodel and tensorflow packages, these models were then represented in plots using matplotlib.  These packages were selected because of the amount of resources available online to learn their use.  Specifically the choice of models to use for this research project were models among the most widely used with a learning curve to use that can be learned without too much technical knowledge.

### Data Importation and Manipulation

We imported the data from yahoo finance and then formatted it to fit our needs, we have more datasets than used to allow for us and the users to attempt with different datasets if need be.

### Exploratory Data Analysis

* __Visulaizing Moving Average of each Sector:__
The Moving Average (MA) is a handy tool in technical analysis, offering a clear view of market trends by averaging out price fluctuations over a chosen period. 

* __Stock Price Movements by Sector:__
Created an Interactive Plotly Graph to Visualize Stock Market Movement across all sectors combined and indivdual sectors (Technology, Financial Services, Healthcare, Consumer Goods, Energy, Industrial, Telecommunications, Utilities, Materials) from 2018-2023

### Initial Comparison using just utilities dataset:

 Our first round of comparisons used the utilities dataset which contained 3 companies.  For each company create a model using all previous data, excluding test data, and predict the previous 21 days of data.  Plot these models and then average their MSE for the test data.  The best two models will advance to the next stage.  An important note to make is that on a given day we are trying to predict the model is given the opening of that day as our goal is prediction per day over 21 days.

### Results:

 ####  LSTM Model
 MSE Error AVG =  1.484
 
 LSTM models, which stand for Long Short-Term Memory models, are a special kind of artificial intelligence used for predicting things that change over time, like stock prices. They are especially good at this because they don't just look at recent trends, but also remember important information from longer ago. This ability to remember both short-term and long-term patterns makes them useful for stock market predictions.

 ####  AR Model 
   MSE Error AVG = 0.347
   
  An AR Model is short for an Autoregressize model. This model uses a combination of regression along with the time series values to make an accurate prediction of the data. Time series meaning that it takes into account the timing of the prediction values, in order to help follow trends within the data.
  
  

  #### ARMA Model 
   MSE Error AVG = 0.348
   
  Is an expansion of the AR model, the ARMA model adds in moving average into the equation which encompasses past values along with the errors of those predictions to predict the next value. This generaly creates a more stable model to outliers, however, it requires more computation.
  
  
  
 ####  ARIMA Model 
   MSE Error AVG = 0.369
   
  Is a further expansion of the AR and ARMA models. The full name of this model is the Auto Regressive Integrated Moving Average Model. It includes all the attributes of the ARMA model, however, it includes integration (differencing) which makes the data more about changes in the price everyday rather than the price itself. This makes the data stationary which removes trends and seasonal structures in predictions which is beneficial for stock predictions which can be effected by seasonality as the markets can be seasonal. Just as with the ARMA Model though, more computational power is required to run this model.
  
  
  

  #### SVR Model 
   MSE Error AVG = 0.353

The SVR Model is short for Support Vector Regression model.  This model works by attempting to optimize the minimization of error within a range,  that being generateded using support vectors to create a margin thats optimal from our training data, rather than error in total, and we also use kernels to increase the dimensionality of data in order to find more patterns that can be picked up on in order to get more accurate results.  In this case we used the linear kernel.



### Final Comparison using top contenders were:
#### Note ARIMA was not included due to its similar performance in terms of MSE to AR
 #### SVR Model 

 MSE Error AVG = 4.38

 #### AR Model 

 MSE Error AVG = 4.58

### Conclusion

In our comprehensive analysis of predictive models for stock price trends, the Support Vector Regression (SVR) Model emerged as the superior predictor. This model demonstrated remarkable consistency, evidenced by its Mean Squared Error (MSE) scores of 0.353 for utility companies and 4.59 for finance companies. Both of these scores are good as finance companies are usually have more volatility.


However, the Auto Regression (AR) model exhibited was quite similar in prediction accuracy. While it achieved commendable results with utility datasets, its performance was markedly less consistent with finance datasets, however is it to be expected. This variance highlights the AR model's superior robustness, as it consistently yielded accurate predictions for seven companies across two distinct sectors.


The performance of ARMA and ARIMA models was unexpectedly less efficient in terms of the extra processing power required. Initially presumed to be more effective due to their complexity, these models performed slightly worse in terms of MSE when  compared to the simpler AR model. However, it is important to mention that in terms of accurately predicting positive or negative movement that ARIMA did perform slightly better than AR and ARMA (who had the same), this does not underscore its extra computational requirement with not so seen benefit.  This descrpency between AR,ARMA, and ARIMA is most likely cause by how we set up our experiment.  By testing its predictions over 21 days with the given prediction being made per day with the that days open, the models didn't have much room for error.  If you were attempting to predict 21 days in the future rather than running the model over those 21 days to predict the next day, there would be a much better yielded difference.

Lastly, the LSTM model did good as well with a score of 1.484, however its computational requirement is quite step.

### Citations

Hayes, A. (n.d.). Autoregressive integrated moving average (ARIMA) prediction model. Investopedia. https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp#:~:text=An%20autoregressive%20integrated%20moving%20average%2C%20or%20ARIMA%2C%20is%20a%20statistical,values%20based%20on%20past%20values 

Kellibelcher. (2022, May 26). JPX Stock Market Analysis &amp; Prediction with LGBM. Kaggle. https://www.kaggle.com/code/kellibelcher/jpx-stock-market-analysis-prediction-with-lgbm/notebook 

Sethi, A. (2023, September 14). Support vector regression tutorial for machine learning. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2020/03/support-vector-regression-tutorial-for-machine-learning/ 

What is an arma model?. 365 Data Science. (2023a, April 21). https://365datascience.com/tutorials/time-series-analysis-tutorials/arma-model/ 

What is an autoregressive model?. 365 Data Science. (2023b, April 27). https://365datascience.com/tutorials/time-series-analysis-tutorials/autoregressive-model/ 