## 1. Topic Modelling on 2015 CNN Health News in Twitter

- **Project Title**: Topic Modelling on 2015 CNN Health News in Twitter
- **Prepared for**: UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name**: Chaithanya Sai Bommavaram
- [Link to my GitHub profile](https://github.com/ChaithanyaSaiB)
- [Link to my LinkedIn profile](https://www.linkedin.com/in/chaithanya-sai-bommavaram/)
- [Link to my PowerPoint presentation file](https://docs.google.com/presentation/d/e/2PACX-1vRoa19X5rhn3RlqlQiu9MAq88RfasTohyQtasPRqXfpwDsAizOmMk1HTYv40vNZBKDTZ-mupfyhO2L6/pub?start=true&loop=false&delayms=3000)
- [Link to my YouTube video](https://www.youtube.com/watch?v=yG3pQJc0LCE)

## 2. Background

- **What is it about?**

    This project focuses on extracting, preprocessing, and analyzing health news articles from tweets to identify key topics using machine learning techniques. The focus is on tweets from prominent health news agencies like NPR Health, CNN Health, CBC Health, Everyday Health, and LA Times Health. By extracting the content linked in these tweets and applying topic modeling, I aim to uncover the main themes discussed in health news.

- **Why does it matter?**

    Health news is a crucial source of information for the public, influencing perceptions and decisions about health and wellness. Understanding the main topics in health news can:

  1. **Inform Public Health Strategies**: By identifying the most discussed health issues, policymakers and health professionals can better address public concerns and allocate resources more effectively.
  2. **Guide Media Production**: News agencies can tailor their content to focus on the most relevant and engaging topics, improving public awareness and education.
  3. **Enhance Health Communication**: Recognizing prevalent topics helps in crafting better health messages and campaigns, ensuring they resonate with the public.
  4. **Monitor Health Trends**: Analyzing health news can reveal emerging trends and issues, providing early warnings about potential public health crises.

- **Research Questions**
  1. What are the main topics discussed in health news articles shared on Twitter by major health news agencies?
  2. How frequently do these topics appear in the dataset?
  3. What are the key terms associated with each identified topic?

## 3. Data 

- **Data sources**

    The datasets used in this project are collected from tweets by the following prominent health news agencies:
    - NPR Health
    - CNN Health
    - CBC Health
    - Everyday Health
    - LA Times Health

    These tweets contain links to health news articles, which are the primary content for analysis.

- **Data Size**

    All the files for the data make up almost 2.91 MB.

- **Data Shape**

    The data initially consists of 3 columns and almost 20,049 instances.

- **Time period**

    Data is collected from Twitter in the year 2015 according to the UCI Machine Learning Repository dataset page.

- **What does each row represent?**

    Each row in the data stands for a tweet on health news by various news agencies.

- **Data dictionary**
  - **Column Names**

    Tweet ID, Date, and Tweet

  - **Data Types**

    Number, DateTime, and Text

  - **Definitions**

    Unique number to differentiate each tweet, date and time of the tweet, and the actual content of the tweet.

  - **Which variable/column will be your target/label in your ML model?**

    The target/label in the machine learning model is the '**topic**' of the health news article. This will be determined through topic modeling (e.g., using LDA) and then used for classification or other ML tasks.

  - **Which variables/columns may be selected as features/predictors for your ML models?**

    We have URLs from the Tweet column which are further used for web scraping to gather the article content. Upon this, further cleaning, preprocessing, and modeling are done to get the topic name for the article under analysis.

## 4. Exploratory Data Analysis (EDA)

- **Handling Missing Content from Web Scraper and Missing Values**:

   - Missing content from the web scraper is handled by implementing exception handling mechanisms during the content extraction process. If there's an error fetching the content or if the content extraction fails, it prints an error message but doesn't halt the process entirely.
   - Rows with missing content are removed after the extraction and preprocessing steps. If the content extraction returns `None`, indicating an issue, the corresponding rows are dropped from the dataset.

- **Text Preprocessing Steps**:
   - Text preprocessing involves several steps:
     - Removing HTML tags using BeautifulSoup.
     - Substituting hyphens with empty spaces.
     - Removing non-alphabetic characters.
     - Converting text to lowercase.
     - Lemmatization and stop word removal using NLTK.
     - Custom stop word removal, including common English words and single letters.

- **Tidiness of the Dataset**:
   - The dataset appears structured, with each row representing a tweet or a piece of content extracted from a tweet, and each column containing attributes such as tweet ID, date-time, tweet content, URL, and extracted content after preprocessing.
   - While the dataset seems organized, there might be room for improvement depending on specific analysis goals, such as identifying and removing duplicate tweets and restructuring or aggregating data for further analysis or modeling.

## 5. Model Training

- **Models for Predictive Analytics**:
   - The project primarily focuses on topic modeling using Latent Dirichlet Allocation (LDA) to analyze health-related articles. Latent Dirichlet Allocation (LDA) is widely used for topic modeling due to its effective approach in uncovering hidden thematic structures within large sets of text datad

- **Training the Models**:
   - The LDA model is trained using the Gensim library on the preprocessed text data. The training process involves iterating over the corpus multiple times (controlled by the `passes` parameter) to learn the topic distributions.
   - No explicit train-test split is performed for this task. However, in predictive analytics, you would typically split your data into training and testing sets, where the training set is used to train the model and the testing set is used to evaluate its performance.

- **Python Packages**:
   - For training the LDA model, the Gensim library is used.
   - Text preprocessing is performed using NLTK (Natural Language Toolkit) for tasks like tokenization, part-of-speech tagging, lemmatization, and stop word removal.
   - Other libraries like Pandas, NumPy, Matplotlib, and Plotly are used for data manipulation, visualization, and analysis.

- **Measuring Model Performance**:
   - The best hyperparameter optimized LDA model has coherence score of 0.53. Though this score says it certainly can do better. I believe more domain based knowledge combined with better cleaning of text since its collected at source could yield better results

## 6. Application of the Trained Model

I developed a web app for people to interact with the trained model using Streamlit, as shown below:
![UMBC Logo](https://www.umbc.edu/wp-content/uploads/2020/10/umbc-logo.png)

![Initial Screenshot](https://www.umbc.edu/wp-content/uploads/2020/10/umbc-logo.png)

![Output Screenshot](https://www.umbc.edu/wp-content/uploads/2020/10/umbc-logo.png)

## 7. Conclusion

In this project, I aimed to analyze health-related articles from various news agencies using topic modeling techniques. I retrieved health news tweets from multiple sources, extracted article content from the URLs mentioned in the tweets, preprocessed the text data, and applied Latent Dirichlet Allocation (LDA) for topic modeling. Additionally, I explored the distribution of topics in the dataset and identified key themes.

### Potential Applications

The potential applications of this work include:

1. **Healthcare Content Analysis**: The derived topics can provide insights into prevalent themes in health-related articles, which can be useful for content creators, journalists, and healthcare professionals.
  
2. **Audience Engagement**: Understanding the topics that resonate with audiences can help news agencies tailor their content to better engage with their readers or viewers.

3. **Research Insights**: Researchers can use the identified topics to gain insights into public discourse on health-related issues, which can inform further studies or policy decisions.

### Limitations

- **Limited Scope**: The analysis is limited to a specific set of news agencies and their health-related articles. It may not capture the entire spectrum of health-related discourse.
  
- **Data Quality**: The quality of the extracted article content depends on the accuracy of the URLs provided in the tweets. Inaccurate or missing URLs could lead to incomplete or erroneous data.

- **Model Selection**: While LDA is a popular technique for topic modeling, it has limitations such as the need to specify the number of topics beforehand and the assumption of fixed topic distributions for documents.

### Lessons Learned

- **Data Preprocessing Challenges**: Preprocessing text data from web sources can be challenging due to variability in HTML structure, encoding issues, and missing or incomplete content.

- **Model Tuning**: Experimenting with different hyperparameters and techniques for model evaluation is crucial for obtaining meaningful results in topic modeling.

- **Interpretation of Results**: Interpreting the derived topics requires domain knowledge and careful consideration of the context in which the articles were written.

### Future Research Direction

- **Integration of Additional Data Sources**: Augmenting the dataset with additional sources of health-related data, such as social media posts, scholarly articles, or government reports, could provide a more comprehensive understanding of health discourse.

- **Enhanced Topic Modeling Techniques**: Exploring advanced topic modeling techniques, such as Dynamic Topic Modeling or Hierarchical Dirichlet Process, could capture temporal dynamics or hierarchical relationships between topics.

- **Sentiment Analysis**: Incorporating sentiment analysis techniques to assess the sentiment expressed in health-related articles could provide deeper insights into public perceptions and attitudes towards health issues.

## 8. References

1. [UCI Machine Learning Repository - Health News in Twitter](https://archive.ics.uci.edu/dataset/438/health+news+in+twitter)
2. [KDnuggets](https://www.kdnuggets.com/)
3. [Analytics Vidhya](https://www.analyticsvidhya.com/)
4. [Towards Data Science](https://towardsdatascience.com/)
5. [Machine Learning Mastery](https://machinelearningmastery.com/)
