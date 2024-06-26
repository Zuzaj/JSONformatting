# JSON file verifier

Presented program is dedicated to check if JSON file's  *Resource* field consists of one asterisk.

## Input
Only files in proper [AWS::IAM::Role Policy formatting](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html) will be tested correctly. 

## Output
Program returns:
-  **False** if an input JSON *Resource* field contains a single asterisk
-  **True** in any other case




## Usage

Make sure you have internet connection and Python 3.10 installed. Clone this repository.

```
git clone https://github.com/Zuzaj/JSONformatting.git
cd JSONformatting
```

To have your file in .json format tested run following commands:

```
python main.py [PATH TO .json FILE]
```

The verification result will be shown in your terminal. When you are in JSONformatting folder path should look like this:
```
"tests/testFiles/*"
```

To test the program's robustness use test files available in **testFiles** folder. 
Unit tests are available in unittests.py file. To run them use command:
```
#Firstly install pytest package
pip install pytest

#Run available tests
pytest unittests.py
```
