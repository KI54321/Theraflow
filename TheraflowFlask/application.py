from flask import Flask, request

import boto3
application = Flask(__name__)


@application.route("/entities")
def entitiesAWS():
    return boto3.Session(aws_access_key_id="AKIARNXTHJNHJGGLVUSB", aws_secret_access_key="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").client("comprehendmedical", region_name="us-west-2").detect_entities_v2(Text=request.args["text"])


if (__name__ == "__main__"):
    application.run()
