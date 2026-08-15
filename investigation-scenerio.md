***Cross-Account Access Investigation***



*## Scenario*



**Alert:** Potentially Unauthorized CrossAccountS3AccessRole was assumed.

&#x20;  **Priority** - Medium

&#x20;  **Impact** - Low

&#x20;  **Description** - Microsoft Defender for Cloud receives an alert indicating that the user

&#x20;  (Oladiran Komolafe) assumed the role CrossAccountS3AccessRole to access s3 Bucket from the

&#x20;  IP Address (12.456.78.90).



*## Investigation*



* CloudTrail was queried for AssumeRole events.
* The event showed that the role was assumed by the Lambda function CrossAccountSTSReader.
* The Lambda subsequently accessed the S3 object confidential-report.txt.



*## Findings*



The access was authorized because:



1\. Oladiran Komolafe was trusted by CrossAccountS3AccessRole.

2\. LambdaExecutionRole was permitted to call sts:AssumeRole.

3\. CrossAccountS3AccessRole allowed s3:GetObject.

4\. The requested object was within the permitted S3 bucket.



*## Conclusion*



The activity was determined to be expected behavior from the configured Lambda function.

