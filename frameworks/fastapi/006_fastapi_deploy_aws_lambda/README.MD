# Requirements
The Serverless Framework – Makes it easy to use AWS Lambda and other managed cloud services to build applications that auto-scale, cost nothing when idle, and overall result in radically low maintenance.
https://github.com/serverless/serverless

Mangum is an adapter for running ASGI applications in AWS Lambda to handle Function URL, API Gateway, ALB, and Lambda@Edge events.  
https://github.com/jordaneremieff/mangum


# Auto deploy

```sh
# I) Installing Serverless Framework
# 1. Install Node.js and npm: Serverless Framework requires Node.js and npm.

# On macOS:
brew install node
# On Ubuntu:
sudo apt update
sudo apt install nodejs npm

# 2. Install Serverless Framework:
npm install -g serverless

# 1. Deploy Using Serverless Framework:
serverless deploy
```
[deploy.sh](proj%2Fdeploy.sh) serverless deploy

# Manual deploy
```sh
# II) Alternative Method: Using AWS CLI
# If you prefer not to use the Serverless Framework, you can manually package and deploy your FastAPI application 
using AWS CLI.

# 1. Prepare Your Environment
# Ensure you have virtualenv installed:
pip install virtualenv

# 2. Create and Activate a Virtual Environment
virtualenv venv
source venv/bin/activate

# 3. Install Dependencies
pip install fastapi mangum
pip freeze > requirements.txt

# 4. Create a Deployment Package

zip -r9 function.zip .

# 5. Upload to AWS Lambda
# Create an S3 bucket to store your deployment package:
aws s3 mb s3://your-bucket-name

# Upload the zip file to the S3 bucket:
aws s3 cp function.zip s3://your-bucket-name/

# Create a Lambda function using the uploaded zip file:
aws lambda create-function --function-name your-function-name --runtime python3.11 --role 
arn:aws:iam::your-account-id:role/your-lambda-execution-role --handler app.handler --code S3Bucket=your-bucket-name,S3Key=function.zip --timeout 30 --memory-size 512

#6. Set Up API Gateway
# You need to create an API Gateway to trigger your Lambda function.
# Create an API:
aws apigateway create-rest-api --name 'FastAPI via Lambda'

# Get the API ID:
aws apigateway get-rest-apis

# Create a resource:
aws apigateway create-resource --rest-api-id your-api-id --parent-id your-parent-id --path-part "{proxy+}"

# Create a method:
aws apigateway put-method --rest-api-id your-api-id --resource-id your-resource-id --http-method ANY --authorization-type "NONE"

# Integrate the method with Lambda:
aws apigateway put-integration --rest-api-id your-api-id --resource-id your-resource-id --http-method ANY --type AWS_PROXY --integration-http-method POST --uri arn:aws:apigateway:your-region:lambda:path/2015-03-31/functions/arn:aws:lambda:your-region:your-account-id:function:your-function-name/invocations

# Deploy the API:
aws apigateway create-deployment --rest-api-id your-api-id --stage-name prod
```

[Simple Serverless FastAPI with AWS Lambda](https://www.youtube.com/watch?v=6fE31084Uks&ab_channel=DeadbearCode)

[AWS Lambda + FastAPI (Serverless Deployment): Complete CI/CD Pipeline Using GitHub Actions](https://medium.com/thelorry-product-tech-data/aws-lambda-fastapi-ci-cd-pipeline-with-github-actions-c414866b2d48)


**Summary**

Serverless Framework: Install and deploy using npm install -g serverless and serverless deploy.
Manual Deployment: Package your application, upload to S3, create a Lambda function, and set up API Gateway using AWS CLI.