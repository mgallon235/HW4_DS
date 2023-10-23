
from sklearn.linear_model import LogisticRegression
import pandas as pd 
from sklearn.model_selection import train_test_split


# Function that returns features (X) and target (Y)
class TrainAndPredict:
    def __init__(self, df_train, df_test, feature_columns, target_column):
        self.df_train = df_train
        self.df_test = df_test
        self.feature_columns = feature_columns
        self.target_column = target_column

    def train_and_test_log_model(self):
        X_train = self.df_train[self.feature_columns]
        y_train = self.df_train[self.target_column]

        # Extract feature and target data from the test dataset
        X_test = self.df_test[self.feature_columns]
        y_test = self.df_test[self.target_column]

        # Calculate training and test scores (hard-coded the hyperparameters for now)
        self.model = LogisticRegression(C=0.1, penalty='l2', solver='liblinear')
        # Fit the model to the training data
        self.model.fit(X_train, y_train)

        train_score = self.model.score(X_train, y_train)
        test_score = self.model.score(X_test, y_test)

        return train_score, test_score

    def predict_probs(self, x_train, y_train,x_test):
        train_model = train_log_model(x_train, y_train)
        train_probabilities = train_model.predict_proba(x_train)[:, 1]
        test_probabilities = train_model.predict_proba(x_test)[:, 1]
        train_probabilities =  pd.Series(train_probabilities)
        test_probabilities =  pd.Series(test_probabilities)
        return train_probabilities, test_probabilities
    


"""testing"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
os.chdir("/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/homework_four")

class DiabetesDataLoader:
    def __init__(self):
        self.file_path = os.path.join(os.getcwd(), 'sample_diabetes_mellitus_data.csv')
        self.df = pd.read_csv(self.file_path)

    def train_and_test_data(self):
        df_train, df_test = train_test_split(self.df, test_size=0.2, random_state=42)
        return df_train, df_test

data_loader = DiabetesDataLoader()
# Call the train_and_test_data method to get the split datasets
df_train, df_test = data_loader.train_and_test_data()

# Print the shapes of the training and test datasets to verify they were correctly split
print("Training set shape:", df_train.shape)
print("Test set shape:", df_test.shape)

df_train.head(20)

X = ["age", "height", "weight", "aids", "cirrhosis", "hepatic_failure", "immunosuppression", "leukemia", "lymphoma", "solid_tumor_with_metastasis"]
Y = ["diabetes_mellitus"]

# Create an instance of the TrainAndPredict class
testing = TrainAndPredict(df_train, df_test, X, Y)

# Call the train_and_test_log_model method to train and test the model
train_score, test_score = testing.train_and_test_log_model()

# Print or display the training and test scores
print("Train Score:", train_score)
print("Test Score:", test_score)