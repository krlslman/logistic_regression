import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('/home/koral/Desktop/FullStackTraining/regression/krediVeriseti.csv', delimiter=';', header=0, names=['krediMiktari', 'yas', 'evDurumu', 'aldigi_kredi_sayi', 'telefonDurumu', 'KrediDurumu'])
print(df)

# Split the data into features and target
X = df.drop('KrediDurumu', axis=1)
y = df['KrediDurumu']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a logistic regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Test the model on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = model.score(X_test, y_test)
print('\n', 'Accuracy:', accuracy, '\n')
