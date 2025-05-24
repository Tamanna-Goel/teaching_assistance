import pickle
import pandas as pd
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Load the trained pipeline (model + preprocessing)
pipeline = pickle.load(open('model.pkl', 'rb'))

# Load the label encoder used for target variable (Class attribute)
le = pickle.load(open('label_encoder.pkl', 'rb'))  # Load the saved LabelEncoder

# Route to display the home page with the form
@app.route('/')
def home():
    return render_template('tech.html')

# Route to handle prediction logic
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input values from the form
        native_teacher = int(request.form['Native_teacher'])
        instructor = int(request.form['Instructor'])
        course = int(request.form['Course'])
        semester = int(request.form['Semester'])
        class_size = int(request.form['Class_size'])

        # Prepare the input data as a pandas DataFrame (same structure as the training data)
        input_data = pd.DataFrame([[native_teacher, instructor, course, semester, class_size]], 
                                  columns=['Native_teacher', 'Instructor', 'Course', 'Semester', 'Class size'])

        # Make prediction using the trained pipeline (which includes preprocessing)
        prediction_encoded = pipeline.predict(input_data)

        # Inverse transform the encoded prediction to get the original class label (1, 2, 3)
        prediction = le.inverse_transform(prediction_encoded)

        # Display the predicted 'Class attribute' on the webpage
        return render_template('tech.html', prediction_text=f'Predicted Class Attribute: {prediction[0]}')

    except Exception as e:
        return str(e)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
