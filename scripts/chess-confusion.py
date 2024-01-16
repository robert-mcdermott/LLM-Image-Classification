import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def create_confusion_matrix(csv_file_path):
    # Load the dataset
    data = pd.read_csv(csv_file_path)

    # Correcting column names by stripping leading spaces
    data.columns = data.columns.str.strip()

    # Extracting actual and predicted values
    actual = data['actual']
    predicted = data['predicted']

    # Getting sorted unique labels
    labels = sorted(pd.unique(actual))

    # Creating confusion matrix with labels
    cm = confusion_matrix(actual, predicted, labels=labels)

    # Plotting the confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels, cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix for LLaVA vs. Chess Pieces')
    plt.show()

# Plot graph
csv_file_path = 'chess-res.csv'
create_confusion_matrix(csv_file_path)

