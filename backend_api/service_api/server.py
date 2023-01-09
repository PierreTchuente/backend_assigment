from pyramid.config import Configurator

from service_api.config import Config
from service_api.helpers import pyramid_renderers as renderer_factory


def serve(global_config, **settings):
    pyramid_config = Configurator(settings=settings)
    config = Config.get_instance()
    logger = config.get_logger()

    pyramid_config.scan()
    pyramid_config.add_renderer(
        name=None, factory=renderer_factory.create_json_renderer()
    )
    pyramid_config.add_renderer(
        name="json", factory=renderer_factory.create_json_renderer()
    )
    pyramid_config.add_static_view(name="swagger", path="api_docs")

    logger.info("WSGI App being returned...")
    return pyramid_config.make_wsgi_app()
