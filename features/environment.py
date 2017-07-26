from app import create_app


def before_all(context):
    context.client = create_app().test_client()
