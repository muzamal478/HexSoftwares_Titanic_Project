import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load and train model
@st.cache_resource
def train_model():
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'FamilySize']
    X = df[features]
    y = df['Survived']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_model()

st.title("Survival Prediction 🔮")
st.write("Enter passenger details to predict survival.")

# User inputs with colorful widgets
pclass = st.selectbox("Passenger Class", [1, 2, 3], help="1 = First, 2 = Second, 3 = Third")
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 30, help="Passenger's age")
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 500.0, 32.0, step=0.1)
embarked = st.selectbox("Embarked", ["S", "C", "Q"], help="S = Southampton, C = Cherbourg, Q = Queenstown")
family_size = sibsp + parch + 1

if st.button("Predict Survival", key="predict_button"):
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [0 if sex == "male" else 1],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked': [0 if embarked == "S" else 1 if embarked == "C" else 2],
        'FamilySize': [family_size]
    })
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("🟢 Survived! 🎉")
    else:
        st.error("🔴 Did not survive. 😔")