from pyramid.response import Response
from pyramid.view import view_config

from service_api.config import Config

logger = Config.get_logger()


@view_config(route_name="swagger", request_method="GET")
def swagger(request):
    logger.info(f"logging the request {request}")
    return Response("OK")


@view_config(route_name="get_status", request_method="GET")
def get_status(request):
    return {"ok": True}
