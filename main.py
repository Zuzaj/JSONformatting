
import json
import re

#Function to check if Resource field consists of exactly 1 asterisk
def checkResource(filePath: str) -> bool:
        if (verifyFormat(filePath)):  #file format verification
            with open(filePath) as f:
                data = json.load(f)
                resourceValue = data["PolicyDocument"]["Statement"][0]["Resource"]
                if(resourceValue) == '*':
                    return False
                else:
                    return True

#Function to check format correctness     
def verifyFormat(filePath: str) -> bool:
    with open(filePath) as f:
        try:
            data = json.load(f)
            try:
                if (data.keys() == format_template.keys() and 
                type(data["PolicyName"]) == str and  
                re.match('[\w+=,.@-]+', data["PolicyName"]) and
                type(data["PolicyDocument"]) == dict and 
                data["PolicyDocument"].keys() == format_template["PolicyDocument"].keys() and
                type(data['PolicyDocument']["Statement"]) == type(format_template['PolicyDocument']["Statement"]) and
                data['PolicyDocument']["Statement"][0].keys() == format_template['PolicyDocument']["Statement"][0].keys() and
                type(data['PolicyDocument']["Statement"][0]["Action"]) == type(format_template['PolicyDocument']["Statement"][0]["Action"]) and
                type(data['PolicyDocument']["Statement"][0]["Sid"]) == type(format_template['PolicyDocument']["Statement"][0]["Sid"]) and
                type(data['PolicyDocument']["Statement"][0]["Effect"]) == type(format_template['PolicyDocument']["Statement"][0]["Effect"]) and
                type(data['PolicyDocument']["Statement"][0]["Resource"]) == type(format_template['PolicyDocument']["Statement"][0]["Resource"])
                ):
                    return True
                else:
                    print("Input not in AWS::IAM::Role Policy format") 
            except:
                print("Input not in AWS::IAM::Role Policy format")    
        except:
            print("File format other than .JSON")   
    return False


#AWS::IAM::Role Policy format template
format_template = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}


#Example of usage

#File with Resource = '*'
testFile1 = "testFile1.json"

#File with Resource != '*'
testFile2 =  "testFile2.json"

print(f'File has * in Resource field so returns {checkResource(testFile1)}')
print(f'File doesn\'t have * in Resource field so returns {checkResource(testFile2)}')

