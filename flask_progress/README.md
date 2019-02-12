# Final_Project 

Identifying Cardiovascular Disease
- Cardiovascular disease refers to several types of conditions affecting the heart and blood vessels, also known as the circulatory system. Some common cardiovascular diseases and conditions include heart disease, stroke and hypertension (high blood pressure). Heart disease and stroke are two of the leading causes of death in the United States, major causes of disability and the principal causes of cardiovascular disease death.” - CDC
- Identifying factors related to common cardiovascular diseases would enable targeted preventative health intervention for populations at highest risk to potentially reduce poor health outcomes and associated medical costs. 
- This project aims to investigate factors that lead to poor cardiovascular health as well as explore which machine learning methods most accurately predict patients who are most likely to suffer from cardiovascular diseases. 
- Keywords: Machine Learning, Cardiovascular Health, Diagnosis, Classification

Project Progress: Due Date February 23rd

Step 1: Research / Planning / Project Setup
- create a repository in github for the final project (Brian): https://github.com/Brybtb/Final_Project 
- add README.md file to repository that describes our project (Darren)
- upload initial dataset to repository (Cassie)

Step 2: ETL / ML: 
Create a jupyter notebook for data cleaning and running models (Brian)
Jupyter notebook should include:
1) Data Cleaning
- Load Dataset, inspect basics. 
- Deal with Missing data: 3% BMI data is missing -  need to Impute values; 30% Smoking Data is missing - need to delete column
- Check for outliers: potentially remove them? Process = (1) Log transformations (2) Standardizations (3) Remove outliers
- Convert categorical to numeric
- Explore our target variable’s balance:  Our dataset is unbalanced - need to (source) - (1) balance with over-sampling on our training data with SMOTE, (2) account for cross-validation, (3) perform over- or under-sampling on each fold independently to get an honest estimate of model performance
2) Data Exploration to decide which variables to keep:
- Distributions of variables
- Descriptive stats
- Check relationships among variables
3) Split data into training and testing: Number of iterations? Split ratio? 
- Because we have a small dataset, we will use cross validation since no single split (like 90:10, 80:20, etc) is going to give satisfactory variance in its estimates. 
4) Use different supervised classification machine learning models to predict diagnosis: 
- 1) Train logistic regression
- 2)  train a random forest - Possibly improve it with hyperparameter tuning
- 3) Train a Support Vector Machines (SVM)
5) Assess and Compare the models

Step 3: define conclusions and create visualizations <br>
TODO: create/format files so that we can use flask and heroku to display our findings:
- Set up index / css / python / js files
- Set up files to deploy with heroku
 
 
References: 
- Project Setup and Organization: University of Chicago’s Data Science for Social Good Fellowship Resources
- V. Ramalingam, V., Dandapath, A., & Karthik Raja, M. (2018). Heart disease prediction using machine learning techniques : a survey. International Journal of Engineering & Technology, 7(2.8), 684-687. doi:http://dx.doi.org/10.14419/ijet.v7i2.8.10557
- Microsoft’s Health Cortana Analytics Reporting Application (github)
- Association of American Medical Colleges (AAMC) & National Association of Accountable Care Organizations. (2016). High-Risk-Patient Identification: Strategies for Success (Rep.). Retrieved January 19, 2019, from Association of American Medical Colleges website: https://www.aamc.org/download/470456/data/riskid.pdf. 
- Niehaus, K. E., & Clifton, D. A. (2016). Machine learning for chronic disease. Machine Learning for Healthcare Technologies, 2, 227.  - Fryar CD, Chen T, Li X. Prevalence of Uncontrolled Risk Factors for Cardiovascular Disease: United States, 1999–2010. NCHS Data Brief, No. 103. Hyattsville, MD: National Center for Health Statistics, Centers for Disease Control and Prevention, US Dept of Health and Human Services; 2012.
