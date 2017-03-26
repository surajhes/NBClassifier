# NBClassifier
This project is about creating a supervised NB classifier. This is a 2 step process:
1. It creates a NB model from already tagged data.
2. Use this model to tag unseen data.

In this project we are revieweing the reviews of hotels and classifying into 4 tags :
  1. Positive
  2. Negative
  3. Truthful
  4. Deceptive
 
We use Naive Bayes theorem to construct a NB Model. we build the model using a corpus which is already tagged by a human.
From the tagged sentenses, we build the NB Classifier. For handling unseen words, we perform Laplace Smoothing by performing 
add 1 smoothing.
  
This is written in Python  
