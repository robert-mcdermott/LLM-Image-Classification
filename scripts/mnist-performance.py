import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model_performance(csv_file_path):
    # Load the dataset
    mnist_data = pd.read_csv(csv_file_path)
    
    # Correcting column names by stripping leading spaces
    mnist_data.columns = mnist_data.columns.str.strip()

    # Extracting actual and predicted values
    actual = mnist_data['actual']
    predicted = mnist_data['predicted']

    # Generating a classification report
    report = classification_report(actual, predicted, output_dict=True)

    # Converting the report to a DataFrame for better visualization
    report_df = pd.DataFrame(report).transpose()

    return report_df

# Print performance 
csv_file_path = 'mnist-res.csv'
model_performance = evaluate_model_performance(csv_file_path)
print(model_performance)
