from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _lambda_python
from constructs import Construct


class LambdaAPIStack(Stack):
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
