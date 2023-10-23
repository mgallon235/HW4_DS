
import pandas as pd

df=pd.read_csv("/Users/ruimaciel/Desktop/Barcelona/Computing_for_Data_Science/homework_four/CDS_4/sample_diabetes_mellitus_data.csv")

class DropMissingValuesGenderEthnicity:
    def __init__(self, df):
        self.df = df

    def process(self, columns=["age", "gender", "ethnicity"]):
        return self.df.dropna(subset=columns)

class FillMissingValuesWithMeanHeightWeight:
    def __init__(self, df):
        self.df = df

    def process(self, columns=["height", "weight"]):
        for column in columns:
            self.df[column] = self.df[column].fillna(self.df[column].mean())
        return self.df



# Create an instance and apply both transformations
transformation_handler = FillMissingValuesWithMeanHeightWeight(df).process()
final_df = DropMissingValuesGenderEthnicity(transformation_handler).process()

print(final_df.isnull().sum())



