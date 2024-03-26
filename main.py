
import json
import re
import sys

#Function to check if Resource field consists of exactly 1 asterisk
def check_resource(filePath: str) -> bool:
        if (verify_format(filePath)):  #file format verification
            with open(filePath) as f:
                data = json.load(f)
                resourceValue = data["PolicyDocument"]["Statement"][0]["Resource"]
                if(resourceValue) == '*':
                    return False
                else:
                    return True

#Function to check format correctness     
def verify_format(filePath: str) -> bool:
    with open(filePath) as f:
        try:
            data = json.load(f)
            try:
                conditions =[
                data.keys() == format_template.keys(), 
                type(data["PolicyName"]) == str, 
                re.match('[\w+=,.@-]+', data["PolicyName"]),
                type(data["PolicyDocument"]) == dict,
                data["PolicyDocument"].keys() == format_template["PolicyDocument"].keys(),
                type(data['PolicyDocument']["Statement"]) == type(format_template['PolicyDocument']["Statement"]),
                data['PolicyDocument']["Statement"][0].keys() == format_template['PolicyDocument']["Statement"][0].keys(),
                type(data['PolicyDocument']["Statement"][0]["Action"]) == type(format_template['PolicyDocument']["Statement"][0]["Action"]),
                type(data['PolicyDocument']["Statement"][0]["Sid"]) == type(format_template['PolicyDocument']["Statement"][0]["Sid"]),
                type(data['PolicyDocument']["Statement"][0]["Effect"]) == type(format_template['PolicyDocument']["Statement"][0]["Effect"]),
                type(data['PolicyDocument']["Statement"][0]["Resource"]) == type(format_template['PolicyDocument']["Statement"][0]["Resource"])
                ]
                if all(conditions):
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


def main(argv):
    if len(argv) < 2 or argv[1][-5:] != ".json":
        raise ValueError("Pass *.json file as parameter")
    input_file = argv[1]
    print(check_resource(input_file))



if __name__ == '__main__':
    main(sys.argv)

