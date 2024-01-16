import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def create_confusion_matrix(csv_file_path):
    # Load the dataset
    mnist_data = pd.read_csv(csv_file_path)
    
    # Correcting column names by stripping leading spaces
    mnist_data.columns = mnist_data.columns.str.strip()

    # Extracting actual and predicted values
    actual = mnist_data['actual']
    predicted = mnist_data['predicted']

    # Creating confusion matrix
    cm = confusion_matrix(actual, predicted)

    # Plotting the confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix for LLaVA MNIST Handwritten Digits')
    plt.show()

# Plot graph
csv_file_path = 'mnist-res.csv'
create_confusion_matrix(csv_file_path)

