# AWS-STS-Cross-Account-Security-Monitoring
## About
This project demonstrates how to securely implement cross-account AWS resource access using AWS Security Token Service (STS), IAM roles, Amazon S3, AWS Lambda, AWS CloudTrail, and CloudWatch.

### Two AWS were created to execute this projects:
* Account A — This account hosts the AWS Lambda that uses an IAM role to  execute the function, requesting temporary credentials through STS.
* Account B — This account hosts the S3 bucket with a confidential file and can be accessed by the IAM role that Account A is allowed to assume.

After the IAM role in Account A is assumed, CloudTrail records the cross-account AssumeRole activity, while AWS EventBridge detects the activity and sends an alert through AWS SNS when the designated cross-account role is assumed.

## Objectives

### The primary objectives of this project were to:

* Understand AWS STS and temporary security credentials
* Implement cross-account IAM role assumption
* Apply least-privilege IAM permissions
* Secure access to an S3 bucket
* Use Lambda to perform cross-account operations
* Configure CloudTrail to monitor S3 and STS activity
* Create an EventBridge security detection
* Configure SNS email alerting
* Investigate and reduce unnecessary security alerts
* Understand how AWS services work together in a cloud security monitoring architecture

## AWS Services Used
### This is a list of all the AWS Services used for both Account A and B with its purpose within the project.
| AWS Service |	Purpose |
| --- | --- |
| AWS IAM |	Created and controlled cross-account roles and permissions |
| AWS STS |	Provided temporary credentials through AssumeRole |
| AWS Lambda | Initiated the cross-account access request |
| Amazon S3 |	Protected resource accessed from Account A |
| AWS CloudTrail | Recorded API activity and security events |
| Amazon EventBridge | Detected suspicious/specific STS activity |
| Amazon SNS	| Delivered security alerts through email |

## Project Structure
<img width="500" src="cross_account_sts_architecture.png"/>

### Account A
#### Account A contains:
* IAM Role
* Lambda function
  * The Lambda function uses AWS STS to request temporary credentials for a role located in Account B.
<img src="images/Lambda-Execution-Role.png"/>
This image is the IAM Role "Lambda-Execution-Role" that is used by Lambda to request temporary credentials from AWS STS

### Account B
#### Account B contains:
* CrossAccountS3AccessRole
* Secure S3 bucket
* CloudTrail
* EventBridge rule
* SNS topic
<img src="images/CrossAccountS3AccessRole.png"/>
