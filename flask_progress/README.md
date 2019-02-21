# Final Project: Predicting Cardiovascular Disease

<h3>Introduction</h3>
<ul>
<li>According to the CDC, cardiovascular disease refers to several types of conditions affecting the heart and blood vessels, such as heart disease, stroke and hypertension (high blood pressure). Heart disease and stroke are two of the leading causes of death, major causes of disability, and the principal causes of cardiovascular disease death in the United States[<a href="https://www.cdc.gov/healthcommunication/toolstemplates/entertainmented/tips/CardiovascularHealth.html">1</a>], [<a href="https://www.ncbi.nlm.nih.gov/books/NBK83160/">2</a>].</li>
<li>Identifying factors related to common cardiovascular diseases would enable targeted preventative health intervention for populations at highest risk to potentially reduce poor health outcomes and associated medical costs.</li>
<li>This project aims to investigate factors that lead to cardiovascular disease as well as to explore which supervised machine learning methods most accurately predict cardiovascular disease risk given certain patient measurements and demographic information. The stroke dataset used for our Cardiovascular Disease Predictor can be found <a href="https://www.kaggle.com/asaumya/healthcare-dataset-stroke-data">here</a>.</li>
<li><i>Keywords: Machine Learning, Cardiovascular Disease, Diagnosis, Classification</i></li>
</ul>

<h3>Process</h3> 
<h4>Step 1: Research / Planning / Project Setup</h4>
<ul>
<li>Research project topics, datasets, and appropriate machine learning methods related to healthcare [<a href="https://www.aamc.org/download/470456/data/riskid.pdf">3</a>], [<a href="https://www.sciencepubco.com/index.php/ijet/article/view/10557">4</a>].</li>
<li>Define project workflow and conceptualize data pipeline [<a href="https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/0_before_you_start/pipelines-and-project-workflow">5</a>].<br>
<img src="https://raw.githubusercontent.com/dssg/hitchhikers-guide/master/curriculum/0_before_you_start/pipelines-and-project-workflow/pipeline_diagram.png" style="width:100%" alt="data pipeline diagram"></li>
<li>Create a <a href="https://github.com/Brybtb/Final_Project/tree/master">shared repository</a> in github, add README.md file to repository, upload initial dataset</li>
</ul>

<h4>Step 2: Create a Jupyter Notebook for ETL and Building Machine Learning Models</h4>
<ul>
<li>Data Cleaning: load dataset, inspect basics; handle missing data; handle outliers; binary encoding; define target variable</li>
<li>Data Exploration: view dataset balance; view variable distributions; view descriptive statistics; view relationships among variables, evaluate variable importance</li>
<li>Create a balanced dataset then train supervised classification machine learning models on both the original and re-sampled datasets: (1) logistic regression, (2) support vector classifier, (3) decision trees, and (4) random forest classifier.</li>
<li>Evaluate models and choose one of the 8 as the final model; export chosen scaler and model for flask application</li>
</ul>

<h4>Step 3: Create flask app for a prediction dashboard and deploy with Heroku</h4> 
<ul>
<li>Set up index.html, style.css, app.py, app.js files</li>
<li>Set up additional files for heroku deployment</li>
</ul>

<h3>Conclusions</h3>
<ul>
<li>We used 6 predictor variables from Kaggle’s stroke dataset to classify patients based on the the presence of cardiovascular disease (using their combined risk of having heart disease, stroke and/or hypertension). The six variables included: average glucose level (number between 0 and 300 mg/dL), BMI (number between 0 and 100), age (integer between 0 and 100), marriage status (Ever married? yes or no), gender (male or female), and residence type (urban or rural).</li>
<li>We then used multiple models to predict the presence of disease. Based on the 8 models that we evaluated, the random forest classifier model using the resampled data was chosen as our final model, as it had the best harmonic mean between precision and recall (F1 score = 0.83).</li>
<li>Furthermore, we determined that the best predictors of cardiovascular disease are the patient's (1) average glucose level, (2) BMI, and (3) age.</li>
 <li> Our <a href="https://heartdiseaseprediction.herokuapp.com">final heroku application</a> demonstrates a real-life utilization of our model such that a prediction of cardiovascular risk level is determined based on input, enabling identification of patients who would benefit most from intervention.</li>
</ul>
 
<h3>Possible Improvements</h3>
<ul>
<li>In the future, we could use k-fold cross-validation when splitting our dataset since we have a small dataset and no single split (like 90:10, 80:20, etc.) is going to give satisfactory variance in its estimates.</li>
<li>We could also attempt to further improve our random forest model with hyperparameter tuning through a grid search.</li>
 </ul>

<h3>References</h3>
<ul>
<li>Centers for Disease Control and Prevention. (2017, September 15). Cardiovascular Health. Retrieved February 1, 2019, from https://www.cdc.gov/healthcommunication/toolstemplates/entertainmented/tips/CardiovascularHealth.html</li>
<li>Institute of Medicine (US) Committee on a National Surveillance System for Cardiovascular and Select Chronic Diseases. A Nationwide Framework for Surveillance of Cardiovascular and Chronic Lung Diseases. Washington (DC): National Academies Press (US); 2011. 2, Cardiovascular Disease. Available from: https://www.ncbi.nlm.nih.gov/books/NBK83160/</li>
<li>V. Ramalingam, V., Dandapath, A., & Karthik Raja, M. (2018). Heart disease prediction using machine learning techniques : a survey. International Journal of Engineering & Technology, 7(2.8), 684-687. doi:http://dx.doi.org/10.14419/ijet.v7i2.8.10557</li>
<li>Data Science for Social Good | Center for Data Science and Public Policy, University of Chicago. (2018). Pipelines and Project Workflow. Retrieved February 1, 2019, from https://github.com/dssg/hitchhikers-guide/tree/master/curriculum/0_before_you_start/pipelines-and-project-workflow</li>
<li>Association of American Medical Colleges (AAMC) & National Association of Accountable Care Organizations. (2016). High-Risk-Patient Identification: Strategies for Success (Rep.). Retrieved January 19, 2019, from Association of American Medical Colleges website: https://www.aamc.org/download/470456/data/riskid.pdf.</li>
<li>Niehaus, K. E., & Clifton, D. A. (2016). Machine learning for chronic disease. Machine Learning for Healthcare Technologies, 2, 227.</li>
<li>Fryar CD, Chen T, Li X. Prevalence of Uncontrolled Risk Factors for Cardiovascular Disease: United States, 1999–2010. NCHS Data Brief, No. 103. Hyattsville, MD: National Center for Health Statistics, Centers for Disease Control and Prevention, US Dept of Health and Human Services; 2012.</li>
</ul>   
