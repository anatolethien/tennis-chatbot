import pandas as pd
from sklearn import preprocessing
from sklearn import tree
import streamlit as st

weather = pd.read_csv(
    filepath_or_buffer='assets/weather-raw.csv'
).set_index(
    'day'
)

for column in weather.columns:
    le = preprocessing.LabelEncoder()
    le.fit(weather[column])
    weather[column] = le.transform(weather[column])

X = weather[['outlook', 'temperature', 'humidity', 'windy']]
y = weather['play']
model = tree.DecisionTreeClassifier().fit(X, y)

st.markdown("""
# Chatbot

Can you play tennis today?

---
""")

outlook_options = ("Overcast", "Rainy", "Sunny")
temperature_options = ("Hot", "Cool", "Mild")
humidity_options = ("High", "Normal")
windy_options = ("False", "True")

with st.form("Tennis"):
    outlook = outlook_options.index(
        st.selectbox("Outlook?", outlook_options))
    temperature = temperature_options.index(
        st.selectbox("Temperature?", temperature_options))
    humidity = humidity_options.index(
        st.selectbox("Humidity?", humidity_options))
    windy = windy_options.index(
        st.selectbox("Windy?", windy_options))
    submitted = st.form_submit_button("Submit")
    if submitted:
        user_input = {"outlook": outlook, "temperature": temperature,
                      "humidity": humidity, "windy": windy}
    else:
        user_input = None
        

if user_input != None:
    if model.predict(pd.DataFrame([user_input]))[0] == 0:
        st.write("""
        Stay home... It's a bad day to play tennis... 😕
        """)
    elif model.predict(pd.DataFrame([user_input]))[0] == 1:
        st.write("""
        Take your shoes and call your friends! It's a perfect day to play tennis! 😎
        """)
