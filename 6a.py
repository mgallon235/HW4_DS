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