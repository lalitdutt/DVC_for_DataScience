**# _DataVersioning_:
Data and Model versioning for Iterative ML process**
-----------------------------------------------------
Researchers are required to cite and identify the exact dataset used as a research input in order to support research reproducibility and trustworthiness. This means the researcher needs to be able to accurately indicate exactly which version of a dataset underpins their research findings. This becomes particularly challenging where the data to be cited are ‘dynamic’ - for example, a subset of a large dataset accessed via a web service.

These typical scenarios demonstrate why data versioning is important:

Scenario 1:

"A researcher has used a data collection to verify a research hypothesis, and has published the research result. The researcher should cite exactly the version of the data collection used to enable other researchers to verify the research result and/or do comparison studies".

Scenario 2:

"A researcher has submitted a manuscript to a journal, and was subsequently asked to re-run an experiment during the reviewing process. A different result was obtained after re-running the experiment. After checking models and software, the researcher suspects the data might have changed. The researcher therefore needs to obtain the version used earlier to produce the same result, or to understand the differences between versions in order to make a judgment about whether changes in the data would affect the research output, or even the research hypothesis".

Version information makes a revision of a dataset uniquely identifiable. Uniqueness can be used by data consumers to determine whether and how data has changed over time and to determine specifically which version of a dataset they are working with. Good data versioning enables consumers to understand if a newer version of a dataset is available. Explicit versioning allows for repeatability in research, enables comparisons, and prevents confusion. Using unique version numbers that follow a standardized approach can also set consumer expectations about how the versions differ. Intended outcome: Humans and software agents will easily be able to determine which version of a dataset they are working with.


** # Steps to setup DVC for data and model versioning**

*A) Project Setup with DVC and local cache(for Data and ML Model):*

> pip install dvc

> mkdir <Your Project>

> cd <Your Project>

> git init

> dvc init

> git commit -m 'initialize repo with DVC'

> mkdir data

> mkdir model

> cat data/data_file.txt #type content

> dvc add data/*

> ls -ls data/*
data_file.txt
data_file.txt.dvc
.gitignore

> dvc add data/data_file.txt
Saving 'data/data_file.txt' to cache '.dvc/cache'.
Saving information to 'data/data_file.txt.dvc'.
To track the changes with git run: 
git add data/data_file.txt.dvc

> git add data/data_file.txt.dvc


     After DVC initialization, a new directory .dvc will be created with config and .gitignore files and cache directory. 
     These files and directories are hidden from a user in general and a user does not interact with these files directly.
     The last command, git commit, puts .dvc/config and .dvc/.gitignore files under Git control.

     For more details please refer:
     https://dvc.org/doc/user-guide/dvc-files-and-directories



*B) Project Setup with DVC and Remote storage(for Data and ML Model):*
1) AWS CLI Configuration to access S3:

> pip install awscli

> aws configure
AWS Access Key ID [****************HJ5A]: XXXXXXXXXXXXXXXXXXX
AWS Secret Access Key [****************3Ghf]: XXXXXXXXXXXXXXXXXXXX
Default region name [None]:
Default output format [None]:

2) Setting up project with DVC and S3 storage
> pip install dvc

> mkdir <Your Project>

> cd <Your Project>

> git init

> dvc init

> git commit -m 'initialize repo with DVC'

> mkdir data

> mkdir model

> cat data/data_file.txt #type content

> dvc add data/*

> ls -ls data/*
data_file.txt
data_file.txt.dvc
.gitignore

> dvc add data/data_file.txt
Saving 'data/data_file.txt' to cache '.dvc/cache'.
Saving information to 'data/data_file.txt.dvc'.
To track the changes with git run: 
 git add data/data_file.txt.dvc

> git add data/data_file.txt.dvc

> dvc remote -add <My_Remote> <S3_Location>

> dvc push
Preparing to push data to <S3_Location>
[##############################] 100% Collecting information
(1/1): [##############################] 100% data_file.txt



**Demo1: Logistic Regression** 
**_DataSet_**:
The datasets consist of several medical predictor (independent) variables and one target (dependent) variable, Outcome. Independent variables include the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

**_Columns_**:
1) {**Name**:Pregnancies,**Data Type**:Numeric,**Description**:Number of times pregnant}
2) {**Name**:Glucose,**Data Type**:Numeric,**Description**:Plasma glucose concentration a 2 hours in an oral glucose tolerance test}
3) {**Name**:BloodPressure,**Data Type**:Numeric,**Description**:Diastolic blood pressure (mm Hg)}
4) {**Name**:SkinThickness,**Data Type**:Numeric,**Description**:Triceps skin fold thickness (mm)}
5) {**Name**:Insulin,**Data Type**:Numeric,**Description**:2-Hour serum insulin (mu U/ml)}
6) {**Name**:BMI,**Data Type**:Numeric,**Description**:Body mass index (weight in kg/(height in m)^2)}
7) {**Name**:DiabetesPedigreeFunction,**Data Type**:Numeric,**Description**:Diabetes pedigree function}
8) {**Name**:Age,**Data Type**:Numeric,**Description**:Age (years)}
9) {**Name**:Outcome,**Data Type**:Numeric,**Description**:Class variable (0 or 1) 268 of 768 are 1, the others are 0}

Reference: https://www.kaggle.com/uciml/pima-indians-diabetes-database/version/1

