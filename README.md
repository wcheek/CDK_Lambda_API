# Deploy a machine learning prediction platform using the python flavored AWS CDK and API Gateway Proxy Integration With Lambda

[Dev.to article](https://dev.to/wesleycheek/deploy-an-api-fronted-lambda-function-using-aws-cdk-2nch)

This project quickly deploys an API Gateway fronted custom Lambda function.
Through the API, the Lambda function can be queried by any web client to provide machine learning predictions and other tasks.

## If starting from scratch:

1) `mkdir project && cd project`
2) `cdk init --language python`
3) Follow instructions below to activate venv, install libraries.
Note: Besides for the standard cdk libraries, you should include `aws-cdk.aws-lambda-python-alpha`.
This experimental library allows CDK to build the Lambda function including additional libraries at deployment time.
You will need `Docker` to use this deployment method.
4) Make sure you have activated your AWS credentials and `cdk deploy`



## Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
