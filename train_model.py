import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset (replace with actual path or use a small subset)
df = pd.read_csv("weatherAUS.csv")



# Drop rows with missing target
df = df.dropna(subset=["RainToday", "RainTomorrow"])

# Encode categorical columns
le = LabelEncoder()
df["RainToday"] = le.fit_transform(df["RainToday"])
df["RainTomorrow"] = le.fit_transform(df["RainTomorrow"])

# Select features (simplified)
features = ["MinTemp", "MaxTemp", "Rainfall", "Humidity9am", "Humidity3pm"]
df = df.dropna(subset=features)
X = df[features]
y = df["RainTomorrow"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)
