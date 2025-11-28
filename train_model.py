import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# 1. Load the data
print("Loading data...")
data = pd.read_csv('USA_Housing.csv')

# 2. Select the inputs (Features) and the target (Price)
# We are using 3 columns to predict the Price
X = data[['Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']]
y = data['Price']

# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
print("Training model...")
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Save the trained model to a file
joblib.dump(model, 'house_model.pkl')
print("Success! Model saved as 'house_model.pkl'")