## 1. Topic Modelling on 2015 CNN Health News in Twitter

- **Project Title**: Topic Modelling on 2015 CNN Health News in Twitter
- **Prepared for**: UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- **Author Name**: Chaithanya Sai Bommavaram
- [Link to the author's GitHub profile](https://github.com/ChaithanyaSaiB)
- [Link to the author's LinkedIn profile](https://www.linkedin.com/in/chaithanya-sai-bommavaram/)
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

- **What is it about?**

This project is about extracting, preprocessing, and analyzing health news articles from tweets to identify key topics using machine learning techniques. The focus is on tweets from prominent health news agencies like NPR Health, CNN Health, CBC Health, Everyday Health, and LA Times Health. By extracting the content linked in these tweets and applying topic modeling, the project aims to uncover the main themes discussed in health news.

- **Why does it matter?**

Health news is a crucial source of information for the public, influencing perceptions and decisions about health and wellness. Understanding the main topics in health news can:

  1. Inform Public Health Strategies: By identifying the most discussed health issues, policymakers and health professionals can better address public concerns and allocate resources more effectively.
  2. Guide Media Production: News agencies can tailor their content to focus on the most relevant and engaging topics, improving public awareness and education.
  3. Enhance Health Communication: Recognizing prevalent topics helps in crafting better health messages and campaigns, ensuring they resonate with the public.
  4. Monitor Health Trends: Analyzing health news can reveal emerging trends and issues, providing early warnings about potential public health crises.

- **Research Questions**
  1. What are the main topics discussed in health news articles shared on Twitter by major health news agencies?
  2. How frequently do these topics appear in the dataset?
  3. What are the key terms associated with each identified topic?

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

    Since it is topic modeling problem, it doesn't have any target/label data as such
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
