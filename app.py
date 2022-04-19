import aws_cdk as cdk

from cdk_lambda_model_predictions.lambda_api_stack import (
    LambdaModelPredictionsStack,
)

app = cdk.App()
LambdaModelPredictionsStack(app, "LambdaModelPredictionsStack")

app.synth()
