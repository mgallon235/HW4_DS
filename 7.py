#Question 7
from sklearn.metrics import roc_auc_score

# Add a new column "predictions" to df_test
df_test['predictions'] = predicted_probabilities[:, 1]  # Assuming you're interested in the probabilities of the positive class

# Compute the ROC AUC score (substitute )
roc_auc = roc_auc_score(df_test['diabetes_mellitus'], df_test['predictions'])

print(f"ROC AUC Score: {roc_auc}")