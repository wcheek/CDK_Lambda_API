# from aws_cdk import CfnOutput as Output
from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_efs as efs
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _lambda_python

# from aws_cdk import aws_sqs as sqs
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
        # self.build_lambda_store()
        self.build_gateway()
        self.define_outputs()

    def build_lambda(self):
        self.prediction_lambda = _lambda_python.PythonFunction(
            scope=self,
            id="dryerPredictionLambda",
            entry="lambda_funcs/dryerPredictionLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="handler",
            index="dryer_prediction_lambda.py",
            function_name="dryerPredictionLambda",
            environment={},
        )

    def build_lambda_store(self):
        self.lambda_store = efs.FileSystem(scope=self, id="lambda store")

    def build_gateway(self):
        self.gateway = apigw.LambdaRestApi(
            self, "Endpoint", handler=self.prediction_lambda
        )

    def define_outputs(self):
        # if self.gateway:
        #     Output(scope=self, id="API Gateway", value=self.gateway.url)
        return None
