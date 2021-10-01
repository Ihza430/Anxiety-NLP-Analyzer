# "Are you feeling anxious right now? Take this moment to take a breath."

*By Azin Faghihi, Ihza Gonzales and Suelem Lee

## Project Structure

1. README.md
2. Executive Summary
3. Jupyter Notebooks
4. Python File
4. PDF File
5. Datasets

## Identified Need
About 19% of adults have an anxiety disorder (Anxiety disorders, 2017). To put this in perspective that is over 40 million people in the US with anxiety. Now one’s choice of words even punctuation can hint at the mental or emotional status of a person (Havigerová et al., 2019). There are systems already created for the purpose of analyzing text to provide feedback about a person like the system, TensiStrength (Thelwall, 2016).

In the United States, the most common type of mental disorders is different kinds of anxiety.<br>
1. Panic attack symptoms are so severe that they lead patients to believe they are suffering heart attacks. <br>
2. The actual increased Risk of Heart Attack Panic attacks and chronic anxiety put a lot of stress on the heart with increased blood pressure and pulse.<br>
3. More Stress Hormones too much adrenaline or cortisol over a long period of time can cause, cognitive decline, Increased risk for other mental illnesses, Higher cholesterol <br>
4. Insomnia can lead to Weakened immune system, Unwanted weight gain...<br>

While medications can treat many of these problems, we see the importance of preventive medicine in which needs to be addressed.<br>
<img src="./imgs/depression_instagram.png" alt="Drawing" style="width: 400px;"/>


## Problem Statement
From anxiety subreddit can we classify them into varying degrees of anxiety and provide tailored messages to address anxiety levels with a Chatbot response system?

## Data Description

Posts evaluated from anxiety and writing (neutral sentiment) subreddit: Web Scraping of following websites:<br>
https://www.reddit.com/search/?q=anxiety<br>
https://www.reddit.com/r/writing/<br>

Decision making were based on a easy to perform initial screening tool for generalized anxiety disorder provided by the National HIV Curriculum: <br>https://www.hiv.uw.edu/page/mental-health-screening/gad-7 https://www.hiv.uw.edu/page/mental-health-screening/gad-2


## Methodology

1. EDA
2. Modeling for anxiety Classification
3. Sentiment analysis validating Classification
4. Chatbot for immediate response
5. Sentiment analysis to further classify severity of anxiety

**The analysis of scrapped texts will be used in hopes of classifying users messaging anxiety levels as Binary Classification:**<br>
>Not Anxious<br>
>Anxious<br>

Writing subreddit helps Classification for it's predominant positive neutral language.

<img src="./imgs/sentiment_small.png" alt="Drawing" style="width: 500px;"/>
<img src="./imgs/sentiment_dist_(1).png" alt="Drawing" style="width: 400px;"/>

## Best parameters

**Adjusted term weights:** <br> Methods to detect expressions of stress within short informal messages were SentimentIntensityAnalyser extended from Classifying models, where the ajdusted term weights were evaluated to improve performance of Classification.

>1. Repeated consecutive letters<br>
>2. Frequency of Punctuation use<br>
>3. Various different use of Emoticons<br>
<img src="./imgs/worried.png" alt="Drawing" style="width: 300px;"/>

**Evidence of improvement:** The improvements suggest that additional fine tuning of the term strengths is necessary. The supervised version of our 3 models are preferable to the unsupervised variant, using Tfdif Vectorizer and Count Vectorizer only. Using bigrams hyperparameters for combined additional linguistic negation. After Classifying existance of anxiety on each post, we used a SentimentIntensityAnalyser to classify the intensity of the anxiety of that particular post.

## Threshold denomination
<img src="./imgs/sentiment_threshold.png" alt="Drawing" style="width: 400px;"/>

## Best Prediction Results

**Logistic Regression:**<br>
Best Score: 0.951<br>
> Best Parameters: <br>{'logr__C': 3,<br> 
>'logr__max_iter': 2000,<br> 
>'logr__penalty': 'l2',<br> 
>'logr__solver': 'saga'}<br>

Train Score: 0.992<br>
Test Score: 0.948<br>

**Random Forest:**
Best Score: 0.953<br>
>Best Parameters: {'rf__max_depth': None,<br> 
>'rf__max_features': 'sqrt',<br> 
>'rf__n_estimators': 80,<br> 
>'tvec__max_features': 2000,<br> 
>'tvec__ngram_range': (1, 2),<br> 
>'tvec__stop_words': None}<br>

Train Score: 0.998<br>
Test Score: 0.955<br>

## Conclusion

Overall performance of models and sentiment analysis confirms how well we can accurately classify 3 levels of anxiety. It needs to be extended and tested in different contexts and tailored with specific types of anxiety linguistics.

At this stage, the effectiveness of this Classifier depends on the nature of of the posts classified, rich in words and expressions of anxiety terms being more problematic in an analysable context.

Relaxation is an important aspect of our lives and becoming even more relevant to our virtually connected lives. This anxiety detection app can help to enable smarter applications as well as extending our understanding of our conditions, helping to monitor our overall mental health and ultimately resulting in a punctual accessible more intimate solution for this great demand.

## Recommendation for next steps

1. Analyze further types of ambiguous expressions such as sarcasm.

2. Further analyze events, perceptions or experiences that can cause anxiety or expressed on texts.

3. Further analyze how to physically classify anxiety levels through cellphone cameras and touchscreens, detecting bodily responses, like sweat, heart rate, flushed skin tone, temblings and breathings.

4. Further analyze how to extend to another classification method to analyse long term health related anxiety or short-term anxiety, identifying trends and maybe even predict future occurances, of panic attack or anxiety break.

## Research Sources

Thelwall, M. (2016, July 12). TensiStrength: Stress and relaxation magnitude detection for social media texts. Science Direct. Retrieved September 16, 2021, from https://www.sciencedirect.com/science/article/abs/pii/S0306457316302321. 
Havigerová, J. M., Haviger, J., Kučera, D., & Hoffmannová, P. (2019, March 18).<br>

Text-based detection of the risk of depression. Frontiers. Retrieved September 16, 2021, from https://www.frontiersin.org/articles/10.3389/fpsyg.2019.00513/full. <br>

National Alliance of Mental Illness. (2017, December). Anxiety disorders. NAMI. Retrieved September 16, 2021, from https://www.nami.org/About-Mental-Illness/Mental-Health-Conditions/Anxiety-Disorders. <br>

Python | Sentiment Analysis using VADER https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/<br>