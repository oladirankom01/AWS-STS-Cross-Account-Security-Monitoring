# AWS-STS-Cross-Account-Security-Monitoring
This project demonstrates how to securely implement cross-account AWS resource access using AWS Security Token Service (STS), IAM roles, Amazon S3, AWS Lambda, AWS CloudTrail, and CloudWatch.

Two AWS were created to execute this projects serving 2 different purposes:

Account A — Hosts an AWS Lambda function that requests temporary credentials through STS.
Account B — Hosts the S3 bucket and IAM role that Account A is allowed to assume.
