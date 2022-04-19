# Deploying an API fronted Lambda function using AWS CDK

This project aims to be a minimum working example of deploying a Lambda function accessible through an API Gateway using Python flavored AWS CDK. The API allows you to pass data directly into the Lambda function and get a response back with a result.

## What is possible using this pattern?

1)   Pass data to the function, get a machine learning prediction back.
2)   Request a file stored on `S3`, get a secure link back.
3)   Send parameters to the function, get complex calculations back.
4)   Database retrieval.
     etc...

The [Github repository can be found here.](https://github.com/wcheek/CDK_Lambda_API)

## CDK init & deploy

I won’t cover setting up CDK and bootstrapping the environment. You can find that information [here.](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

Once you have set up CDK, we need to set up the project:

1. `mkdir CDK_Lambda_API && cd CDK_Lambda_API`

2. `cdk init --language python`

3. `source .venv/bin/activate`

4. Optional: If you need additional libraries in your Lambda function, add `aws-cdk.aws-lambda-python-alpha` to requirements.txt to allow custom builds during stack deployment using Docker.

5. `pip install -r requirements.txt && pip install -r requirements-dev.txt`

    Now deploy empty stack to AWS:

6. `cdk deploy`

## Stack design

This stack will deploy a lambda function using `aws-lambda-python-alpha` to build the function with all its additional libraries using a docker container. Make sure to have Docker installed and the daemon running before running `cdk deploy`.

```python
# lambda_api_stack.py

from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _lambda_python
from constructs import Construct


class LambdaModelPredictionsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # in __init__ I like to initialize the infrastructure I will be creating
        self.prediction_lambda = None
        self.gateway = None
        # Additional useful infrastructure might include an S3 bucket,
        # an EFS store, SQS queue, etc.

        self.build_infrastructure()

    def build_infrastructure(self):
        # For convenience, consolidate infrastructure construction
        self.build_lambda()
        self.build_gateway()

    def build_lambda(self):
        self.prediction_lambda = _lambda_python.PythonFunction(
            scope=self,
            id="PredictionLambda",
            # entry points to the directory
            entry="lambda_funcs/APILambda",
            # index is the file name
            index="API_lambda.py",
            # handler is the function entry point name in the lambda.py file
            handler="handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            # name of function on AWS
            function_name="ExampleAPILambda",
        )

    def build_gateway(self):
        # This will attach an API gateway as a trigger to our
        # lambda function above. The return of the handler function also
        # gets routed back to the API gateway.
        self.gateway = apigw.LambdaRestApi(
            self, "Endpoint", handler=self.prediction_lambda
        )

```

## Minimum Working Lambda Function

You can see [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) an example of the response format the API gateway is expecting.

```python
# lambda_funcs/APILambda/API_lambda.py

from logging import getLogger

logger = getLogger()
logger.setLevel(level="DEBUG")


def handler(event, context):
    logger.debug(msg=f"Initial event: {event}")
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": f"Nice! You said {event['queryStringParameters']['q']}",
    }
    return response

```

Now you can do `cdk deploy`. The lambda function will be built using docker and uploaded to the bootstrapped ECR repository. Once the project is built, it will synth a `CloudFormation` template and begin deploying the infrastructure. You can watch your stack deploy on `AWS CloudFormation` - it should be quick since the infrastructure is relatively simple.

Once the process is completed, CDK will output the endpoint URL of the API Gateway:

![graphic](D:\Projects\Notes\My Articles\CDK_Lambda_API\Assets\graphic.png)

## Query the API Gateway

To query the API gateway and get a response back from your lambda function, just send a get request using `requests` or `Postman`

![graphic2](D:\Projects\Notes\My Articles\CDK_Lambda_API\Assets\graphic2.png)

