from flask import current_app


def before_all(context):
    context.client = current_app.test_client()
