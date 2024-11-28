### Introduction
> The project is about the Financial Inclusion in Africa' dataset that was provided as part of the Financial Inclusion in Africa hosted by the Zindi platform. 
The term financial inclusion means:  individuals and businesses have access to useful and affordable financial products and services that meet their needs – transactions, payments, savings, credit and insurance – delivered in a responsible and sustainable way.
The dataset contains demographic information and what financial services are used by approximately 33,600 individuals across East Africa. The ML model role is to predict which individuals are most likely to have or use a bank account.

### Dataset Cleaning:
The dataset contains no missing values and No duplicate values

### Data Preprocessing:
LabelEncoder was use to encode the categoriacal values and pd.map was used to encode the month to maintain its order. The data set is unbalance so random_oversampler was used to balance the dataset.
### Modeling
The data was trained with three different model which are Logistic regression, Decision Tree classifier and  RandomForestClassifier, but the best performning  on both train and test data is RandomForestClassifier with the training accuracy of 97% and test accuracy of 93%

### Model deployment
The application is deployed for better user interaction on streamlit

# Limitation
The dataset contains some outliers which was handled by standardscaler normalization
The dataset is inbalance, this was mannaged by applying randomoversampler to balance it

### Conclussion
The project was an end to end Supervised classification project, which give general overview on bank marketting outcome.