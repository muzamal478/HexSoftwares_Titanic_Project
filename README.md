# HexSoftwares_Titanic_Project 🚢

## Overview 🎉
This professional portfolio project transforms the Kaggle Titanic challenge into an interactive web app using Streamlit. It features exploratory data analysis, machine learning model training, and survival predictions in a modern, dark-themed interface with animations and responsive design.

## Features ✨
- **Responsive Design**: Optimized for mobile and desktop.
- **Dark Theme**: Sleek, eye-friendly UI with purple/blue accents.
- **Animations**: Fade-ins and hover effects for buttons.
- **Lazy Loading**: Efficient image/plot rendering via caching.
- **Pages**: Home, EDA, Model Training, Prediction.

## Installation 🛠️
1. Clone the repository: `git clone https://github.com/muzamal478/HexSoftwares_Titanic_Project.git`
2. Create a virtual environment: `python -m venv env` and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`

## Usage 📖
- Navigate using the sidebar to explore:
  - **Home**: Project introduction.
  - **EDA**: Visualizations of survival and age.
  - **Model Training**: Train and evaluate a Random Forest model.
  - **Prediction**: Input passenger details to predict survival.

## Dataset 📊
- Source: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Columns: PassengerId, Survived (0/1), Pclass (1-3), Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.

## Deployment 🌐
Deploy to Streamlit Sharing:
1. Sign up at https://share.streamlit.io.
2. Connect your GitHub account.
3. Select this repo, set `app.py` as the main file, and deploy.
4. Share the live URL (e.g., https://hexsoftwares-titanic-project.streamlit.app/).

## File Structure 📁

HexSoftwares_Titanic_Project/ 
├── app.py 
├── pages/ 
│ ├── eda.py 
│ ├── model_training.py 
│ └── prediction.py 
├── .streamlit/ 
│ └── config.toml 
├── requirements.txt 
└── README.md

## Contributions 🤝
Fork and submit pull requests for improvements!

## License 📄
MIT License.

## Author 👨‍💻
Muzamal Asghar | Data Science Intern @ Hex Softwares