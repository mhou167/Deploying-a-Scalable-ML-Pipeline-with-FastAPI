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
Peformance on precision: Very Accurate.  80% of the values have a precision value over 60% meaning this model rarely produces false positives.
performance on recall: Adequate.  37% of the values are 60% or higher, most of which are perfect 100%.  The model does an adequate job of capturing most of the relevant positive cases.
performances on fbeta: Good.  The overall fbeta value is .70 which is good and indicates better performance and a stronger emphasis on recall.


## Ethical Considerations
The data used is publicly available through the Census Bureau and does not include any sensitive data for ethical considerations.


## Caveats and Recommendations
There are no Caveats nor recommendations.