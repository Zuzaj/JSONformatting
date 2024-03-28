
import json
import re
import sys

#Function to check if Resource field consists of exactly 1 asterisk
def check_resource(filePath:str) -> bool:
        if (verify_format(filePath) == True):  #file format verification
            with open(filePath) as f:
                data = json.load(f)
                resourceValues = [data["PolicyDocument"]["Statement"][i]["Resource"] for i in range(len(data["PolicyDocument"]["Statement"]))]
                if '*' in resourceValues:
                    return False
                else:
                    return True
        else:
            return verify_format(filePath)

#Function to check format correctness     
def verify_format(filePath: str) -> bool:

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
 
    with open(filePath) as f:
        try:
            data = json.load(f)
            try:   
                conditions = [
                data.keys() == format_template.keys(),
                type(data["PolicyName"]) == str, 
                re.match('[a-zA-Z0-9_+=,.@-]+', data["PolicyName"]),
                len(data["PolicyName"]) >= 1 and len(data["PolicyName"]) <= 128,
                type(data["PolicyDocument"]) == dict,
                data["PolicyDocument"].keys() == format_template["PolicyDocument"].keys(),
                type(data['PolicyDocument']["Statement"]) == list,
                all([type(data['PolicyDocument']["Statement"][i]) == dict for i in range(len(data['PolicyDocument']["Statement"]))]),
                all([set(data['PolicyDocument']["Statement"][i].keys()).issubset(("Sid", "Effect", "Principal", "Action", "Resource", "Condition")) for i in range(len(data['PolicyDocument']["Statement"]))]),
                all(["Effect" in data['PolicyDocument']["Statement"][i] and "Action" in data['PolicyDocument']["Statement"][i] for i in range(len(data['PolicyDocument']["Statement"]))]),
                all([type(data['PolicyDocument']["Statement"][i]["Action"]) in [list, str] for i in range(len(data['PolicyDocument']["Statement"]))]), 
                all([data['PolicyDocument']["Statement"][i]["Effect"] in ["Allow", "Deny"] for i in range(len(data['PolicyDocument']["Statement"]))]),
                all([type(data['PolicyDocument']["Statement"][i]["Resource"]) in [list, str] for i in range(len(data['PolicyDocument']["Statement"]))])
                 ]
                if all(conditions):
                    return True
                else:
                    return "Input not in AWS::IAM::Role Policy format"
            except:
                return "Input not in AWS::IAM::Role Policy format"   
        except:
            return "Input not in .json file format"   





def main(argv):
    try:
        input_file = argv
    except:
        raise ValueError("Pass *.json file as parameter")
    print(check_resource(input_file))



# if __name__ == '__main__':
#     main(sys.argv)


main("tests/testFiles/testFile2.json")