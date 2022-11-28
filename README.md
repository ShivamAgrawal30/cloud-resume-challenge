# Cloud Resume Challenge on Amazon Web Service
- To create a website showing your CV, hosted on AWS using various AWS services.

- Techincal Requirements:
    - Front-end: HTML, CSS and JavaScript files in S3, CloudFront
    - Back-end: API Gateway, Lambda with Python, DynamoDB
    - Infrastructure as code (Terraform, SAM, CDK)
    - CICD (continuous integration, continuous deployment) with Github Actions

## Let's Start the challenge

### 1. Mindmap + Architecture

![CRC Mindmap](/images/mindmap_aws_challenge.jpg)

![CRC AWS Architecture](/images/crc_aws_architecture.png)

## Final Output
- Link to my CV website - https://d3n4j6eaq72lpc.cloudfront.net/

### Areas to improvise
- Could have integrated Route53.
- Could have done unit testing, integration testing etc.
- Could have used Terraform (IaC) since it's not any cloud platform specific.
- Make CI/CD more robust
- Remove hardcoding values and use configuration or values.yaml file.
- Throttle API requests
