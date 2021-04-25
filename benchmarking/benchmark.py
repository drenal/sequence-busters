import pandas as pd
import argparse

def benchmark(predictions_file, labels_file):
    def accuracy(inputs, labels) -> float:
        """ Returns accuracy
        Args:
            inputs: tensor with predicted values
            labels: tensor with correct values
        """

        return (sum((inputs == labels)) / len(labels))

    predictions = pd.read_csv(predictions_file, sep=',')
    labels = pd.read_csv(labels_file, sep=',')

    q3_accuracy = accuracy(predictions['q3'], labels['q3'])
    q8_accuracy = accuracy(predictions['q8'], labels['q8'])

    metrics = {'q3': q3_accuracy, 'q8': q8_accuracy}
    print(metrics)
    return metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions')
    parser.add_argument('--labels')

    args = parser.parse_args()
    print("Benchmarks:", benchmark(args.predictions, args.labels))
