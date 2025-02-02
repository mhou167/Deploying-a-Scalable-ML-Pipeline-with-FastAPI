# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a classification model created from data that is publicly available from Census Bureau.
The model being used is Random Forest Classifer.


## Intended Use
This model is expected to perform well with large datasets, that have a combination of categorical as well as numerical data.  This model will also do well with a dataset that has missing values.

This model would be unsuitable for real time predictions on very, very large datasets as it runs at a slower speed and could become a cost burden.


## Training Data
80% of the data is used for the training data.

## Evaluation Data
The data used is publicly available.  The dataset is from the Census Bureau.  It is processed during the process_data step which includes processesinthe data using One Hot Encoder for the categorial features and label binarizer for the labels.


## Metrics
The metrics used in this model are precision, recall and fbeta score.
Peformance on precision: TODO
performance on recall: TODO
performances on fbeta: TODO
_Please include the metrics used and your model's performance on those metrics._Then delete this line.

## Ethical Considerations
The data used is publicly available through the Census Bureau and does not include any sensitive data for ethical considerations.


## Caveats and Recommendations
There are no Caveats nor recommendations.