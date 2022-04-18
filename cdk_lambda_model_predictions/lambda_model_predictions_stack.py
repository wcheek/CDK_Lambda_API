# from aws_cdk import CfnOutput as Output
from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _lambda_python
from constructs import Construct


class LambdaModelPredictionsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.prediction_lambda = None
        self.lambda_store = None
        self.gateway = None

        self.build_infrastructure()

    def build_infrastructure(self):
        self.build_lambda()
        self.build_gateway()

    def build_lambda(self):
        self.prediction_lambda = _lambda_python.PythonFunction(
            scope=self,
            id="PredictionLambda",
            entry="lambda_funcs/PredictionLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="handler",
            index="prediction_lambda.py",
            function_name="PredictionLambda",
            environment={},
        )

    def build_gateway(self):
        self.gateway = apigw.LambdaRestApi(
            self, "Endpoint", handler=self.prediction_lambda
        )
