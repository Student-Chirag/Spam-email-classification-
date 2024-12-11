import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

data = pd.read_csv("C:\python\spam.csv")

data.drop_duplicates(inplace = True)
data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam', 'Spam'])

mess = data['Message']
cat = data['Category']

(mess_train, mess_test, cat_train, cat_test)

cv = CountVectorizer(stop_words='english')
cv.fit_transform(mess_train)

#creating model
model = MultinomialNB()
model.fit(features, cat_train)

#Test our model
features_test = cv.transform(mess_test)
# print(model.score(features_test, cat_test))

#predict Data
def predict(message):
  input_message = cv.transform ([message]).toarray()
  result = model.predict(message)
  return result

  st.header('Spam Detection')
  
  output = predict('Congratulations, you won a lottery')
 st.text_input('Enter Message Here')

if st.button('Validate'):
  output = predict (input_mess)
  st.markdown = output
  

      

*

