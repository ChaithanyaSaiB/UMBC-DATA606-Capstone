# The Template and Guideline for the Final Report

- This document serves as a guide for developing project proposal which will eventually become the proposal and final report.
- You start with the end in mind and adopt an agile approach:
  - Making progress continuously towards your goal.
  - Updating this document continuously along the way.
 
## 1. Title and Author

- **Project Title**

  Topic Modelling on 2015 Health News in Twitter
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- **Author Name**

  Chaithanya Sai Bommavaram
- [Link to the author's GitHub profile](https://github.com/ChaithanyaSaiB)
- [Link to the author's LinkedIn profile](https://www.linkedin.com/in/chaithanya-sai-bommavaram/)
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

- **What is it about?**

  Aimed at applying topic modeling techniques to identify common themes of the articles under consideration
- **Why does it matter?**

  Topic modelling for news content analysis is a powerful exploratory method to get insight into the diversity of topics in the focus of media that implies indirectly the focus of our society.
- **What are your research questions?**

  What were the most frequently mentioned topics for the considered time? 

## 3. Data 

- **Data sources**

  Data was taken from UCI Machine Learning Repository
- **Data Size**

  All the files for the data make up almost 9 MB
- **Data Shape**

  Data initially would be 3 columns and almost 58000 instances
- **Time period**

  Data is collected from Twitter in the year 2015
- **What does each row represent?**

  From the data description in UCI, **each row in the data stands for tweet on health news by various news agencies**
- **Data dictionary**
  - **Columns Name**

    Tweet Id, Date and Tweet
  - **Data Type**

    Number, DateTime and Text
  - **Definition**

    Unique number to differentiate each tweet, date and time of the tweet and actual content of the tweet
  - **Which variable/column will be your target/label in your ML model?**
  - **Which variables/columns may be selected as features/predictors for your ML models?**

    We have URL from the Tweet column which could be further used for web scraping for  additional information
    Since this is unsupervised problem, there are only features that are mentioned above and no target variable(s)

## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using **Plotly Express**)
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows? 
- Find out if the data require splitting, merging, pivoting, melting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 
