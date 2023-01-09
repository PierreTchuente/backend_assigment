import datetime

from pyramid.renderers import JSON


def datetime_adapter(obj, request):
    return obj.isoformat()


def decimal_adapter(obj, request):
    return float(obj)


def create_json_renderer():
    renderer = JSON()
    renderer.add_adapter(datetime.date, datetime_adapter)
    renderer.add_adapter(datetime.datetime, datetime_adapter)
    return renderer
