# The Template and Guideline for the Final Report

- This document serves as a guide for developing project proposal which will eventually become the proposal and final report.
- You start with the end in mind and adopt an agile approach:
  - Making progress continuously towards your goal.
  - Updating this document continuously along the way.
 
## 1. Title and Author

- Topic Modelling on 2015 Health News in Twitter
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Chaithanya Sai Bommavaram
- [Link to the author's GitHub profile](https://github.com/ChaithanyaSaiB)
- [Link to the author's LinkedIn profile](https://www.linkedin.com/in/chaithanya-sai-bommavaram/)
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

- Aimed at applying topic modeling techniques to identify common themes of the articles under consideration
- Topic modelling for news content analysis is a powerful exploratory method to get insight into the diversity of topics in the focus of media that implies indirectly the focus of our society.
- What were the most frequently mentioned topics for the considered time? 

## 3. Data 

- Data was taken from UCI Machine Learning Repository
- All the files for the data make up almost 9 MB
- Data initially would be 3 columns and almost 58000 instances
- From the data description in UCI, 
- **Each row in the data stands for tweet on health news by various news agencies**
- Data dictionary
  - Tweet Id, Date and Tweet
  - Number, DateTime and Text
  - Unique number to differentiate each tweet, date and time of the tweet and actual content of the tweet
  - We have URL from the Tweet column which could be further used for web scraping for additional information
Since this is unsupervised problem, there are only features that are mentioned above and no target variable(s)
