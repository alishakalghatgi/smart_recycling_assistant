# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Step 1: Load your Excel dataset
df = pd.read_excel('backend/dataset.xlsx') # Replace with your actual filename

# Step 2: Prepare features and labels
X = df['item_name']  # Column with item names
y = df['category']   # Column with waste categories

# Step 3: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create a pipeline (TF-IDF + Naive Bayes)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

# Step 7: Try a sample prediction
sample = "plastic wrapper"
prediction = model.predict([sample])
print(f"Prediction for '{sample}': {prediction[0]}")

# Step 8: Save the trained model
joblib.dump(model, 'waste_classifier.pkl')
print("Model saved as waste_classifier.pkl")