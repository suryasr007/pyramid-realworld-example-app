from pyramid.config import Configurator


def includeme(config: Configurator) -> None:
    """Pyramid knob."""
    config.add_route("heroku_resources", "/heroku/resources")
    config.add_route("heroku_resources_single", "/heroku/resources/{slug}")
