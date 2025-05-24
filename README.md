🧑‍🏫 Teaching Assistant Performance Evaluation

🔧 Tools: Python, SMOTE, Scikit-learn

🧠 Model: Random Forest Classifier

🎯 Accuracy: 74%

Challenges and Risks
 - Categorical Data Transformation: Applied label encoding for the target variable and one-hot encoding for categorical features like Instructor and Course.
 - Class Imbalance: Addressed using SMOTE for oversampling and class weight adjustment during model training.
 - Multicollinearity: Managed by conducting correlation analysis and removing or combining highly correlated features.

Created a classification model to evaluate the performance of teaching assistants based on instructor feedback, class size, and course context. Addressed severe class imbalance using SMOTE and evaluated results using confusion matrix and F1-score. Project demonstrates strong use of educational data mining. The Teaching Assistant Performance Evaluation project successfully predicted TA performance based on various factors such as native language, instructor, course, semester type, and class size. Through comprehensive data cleaning, preprocessing, and exploratory data analysis, we identified key correlations and relationships within the dataset. Various machine learning models, including Logistic Regression, Random Forest, Gradient Boosting, and Support Vector Machine, were tested, with Random Forest demonstrating the highest accuracy and overall performance. Challenges such as handling categorical data, managing class imbalance, and addressing overfitting were effectively overcome using techniques like encoding, SMOTE, and pruning. The Random Forest model was recommended as the best-performing model for predicting TA performance.
