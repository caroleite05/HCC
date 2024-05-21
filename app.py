#importando as bibliotecas
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# título
st.write("Prevendo Carcinoma Hepatocelular (HCC)")

# dataset
df = pd.read_csv("hcc_dataset_filled.csv")
columns_to_keep = ['Gender', 'Alcohol', 'Age', 'Diabetes', 'PS', 'Ascites', 'Symptoms', 'Hemoglobin', 'Class']
df = df[columns_to_keep]

# cabeçalho
st.subheader("Informações dos dados")

# nome do usuário
user_input = st.sidebar.text_input("Digite o seu nome:")

# escrevendo o nome do usuário
st.write("Paciente:", user_input)

# dados de entrada
x = df.drop(['Class'], axis=1)
y = df['Class']

# separa dados em treinamento e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# dados dos usuários com a função
def get_user_data():
    gender_options = {'Female': 0, 'Male': 1}
    gender = st.sidebar.selectbox("Gender", options=list(gender_options.keys()))
    
    age = st.sidebar.slider("Age", 0, 110, 25)  
    
    alcohol_options = {'No': 0, 'Yes': 1}
    alcohol = st.sidebar.selectbox("Alcohol", options=list(alcohol_options.keys()))
    
    diabetes_options = {'No': 0, 'Yes': 1}
    diabetes = st.sidebar.selectbox("Diabetes", options=list(diabetes_options.keys()))
    
    ps_options = {'Active': 0, 'Ambulatory': 1, 'Disabled': 2, 'Restricted': 3, 'Selfcare': 4}
    ps = st.sidebar.selectbox("PS", options=list(ps_options.keys()))
    
    ascites_options = {'Mild': 0, 'Moderate': 1, 'None': 2}
    ascites = st.sidebar.selectbox("Ascites", options=list(ascites_options.keys()))
    
    symptoms_options = {'No': 0, 'Yes': 1}
    symptoms = st.sidebar.selectbox("Symptoms", options=list(symptoms_options.keys()))
    
    hemoglobin = st.sidebar.slider("Hemoglobin", 0, 19, 13)

    # dicionário para receber informações
    user_data = {
        'Gender': gender_options[gender],
        'Age': age,
        'Alcohol': alcohol_options[alcohol],
        'Diabetes': diabetes_options[diabetes],
        'PS': ps_options[ps],
        'Ascites': ascites_options[ascites],
        'Symptoms': symptoms_options[symptoms],
        'Hemoglobin': hemoglobin,
    }

    features = pd.DataFrame(user_data, index=[0])
    return features

user_input_variables = get_user_data()

user_input_variables = user_input_variables[x_train.columns]

# Gráfico
graf = st.bar_chart(user_input_variables)

# Seletor de modelo
model_choice = st.sidebar.selectbox("Escolha o modelo", ("Decision Tree", "KNN"))

if model_choice == "Decision Tree":
    model = DecisionTreeClassifier(max_depth= 7)
elif model_choice == "KNN":
    model = KNeighborsClassifier(algorithm= 'auto', n_neighbors=5, weights='uniform')

# Treinamento do modelo
model.fit(x_train, y_train)

# Acurácia do modelo
st.subheader('Acurácia do modelo')
accuracy = accuracy_score(y_test, model.predict(x_test)) * 100
st.write(f"{accuracy:.2f}%")


# Previsão do resultado
prediction = model.predict(user_input_variables)

# Mapear previsões para "Dies" e "Lives"
prediction_mapped = ["Dies" if pred == 0 else "Lives" for pred in prediction]

# Exibir previsão de forma mais bonita
st.subheader('Previsão:')
if prediction_mapped[0] == "Dies":
    st.error(f"{user_input}, a previsão é: {prediction_mapped[0]}")
else:
    st.success(f"{user_input}, a previsão é: {prediction_mapped[0]}")