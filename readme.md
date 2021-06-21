## Project Title: Sentiment Analysis of Amazon review dataset 2018

## Project Description:
As nowadays we usually do shopping based on other users reviews on amazon. So reviews matters a most. 
Here Based on that reviews I have developed a system which tells whether particular review is positive or not.

## Requirement

Python 3.x

## Steps to run

1. Download the `reviews` for as much as categories you want from [here](http://deepyeti.ucsd.edu/jianmo/amazon/index.html) and put this all `json.gz` files in `data` folder.
2. Run the `data_preprocessing.ipynb` file which takes input from `data` folder(which is having all gzs files) and output will be cleaned data, we call it `data.csv`
3. The `model_generation_loading.ipynb` takes input as data.csv and gives Machine Learning models we call it `count_tf_gs.joblib`. Later on this model can be used to predict any new review.


## Explanation
### Data pre-processing steps
1. `preprocess.py` which converts gz to json, and make DataFrame combined with all categories we call it `final_data.csv`
2. pandas_profiling helps us to generate report including most of all details about DataFrame with visualization. See more about it [here](https://github.com/pandas-profiling/pandas-profiling)
3. From 1-5 range reviews. we taking 1-2 as Negative, 3 as Neutral and 4-5 as Positive.
4. While we found we have lots of data in category of `pos`, it needs to be balanced so we are doing balancing of this data.
5. As we can see, this is reviewText are raw text data. So we are applying some **text pre-processing techniques** to make clean texts.
6. Then combined all data in one DataFrame and saving as `data.csv`

### Modeling
1. Taking generated data.csv and splitting this in train and test split by **sklearn** library. Here I have taken 25% in test set.
2. In this step, we are making **pipeline** for all further data processing and prediction from `sklearn.pipeline`.  
   1. We are converting text data into `CountVector`. see more about it [here](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html).
   2. Then transforming a count matrix to a normalized **tf-idf representation**.
   3. Then ML model **LinearSVC** (Linear Support Verctor Classifier) is applied. as we have linear data distribution so linear SVM is good suites for us. 
3. saving the model with **joblib** library. So in future we can direct load the model and get our results easily.
4. We are Generating **Classification report** to understand our model better and plotting pie chart for **precision(positive predictive value)**. we have accuracy of around `76%`, which is way better for this amount of data. 
5. Loading model for future use and prediction with new reviews.


### For Future

-> Go for more categories in order to get more and more data.

-> For reviewText can do more text pre-processing like via embedding, spelling correction and find similarities between reviews.

-> Deep Learning model like GRU or LSTM as they work with sequence data.
   


## Appendix
1. [Pre-trained model](https://drive.google.com/file/d/1-2g3Rgwn_7RY973_rtGxFLXsSXwEsCqJ/view?usp=sharing)
2. [data.csv(which can be used as model input)](https://drive.google.com/file/d/1-36UfSyEk3rMEWqfifID_1n6JS9_P1YC/view?usp=sharing)
    

 