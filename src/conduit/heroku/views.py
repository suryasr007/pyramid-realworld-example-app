from pyramid.request import Request
from pyramid.view import view_config

import json
import structlog
import typing as t

logger = structlog.getLogger("heroku.views")


@view_config(
    route_name="heroku_resources", renderer="json", request_method="POST", openapi=False
)
def provision(request: Request) -> t.Dict[t.Any, t.Any]:

    heroku_data = json.loads(request.body)

    logger.info(heroku_data)

    return {
        "id": heroku_data["uuid"],
        "message": "Your add-on is created and is available",
        "config": {"KEY1": "VALUE1"},
    }


@view_config(
    route_name="heroku_resources_single",
    renderer="json",
    request_method="PUT",
    openapi=False,
)
def plan_change(request: Request) -> t.Dict[t.Any, t.Any]:
    """Update an article."""

    addon_id = request.matchdict["slug"]
    return {"message": "Plan change is not supported"}


@view_config(
    route_name="heroku_resources_single",
    renderer="json",
    request_method="DELETE",
    openapi=False,
)
def deprovision(request: Request) -> t.Dict[t.Any, t.Any]:
    """Update an article."""

    addon_id = request.matchdict["slug"]
    return {"message": "De-provision not supported"}
