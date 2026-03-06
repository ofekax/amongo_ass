import datetime
import uuid

import uvicorn
from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED

from src.models.deployment.deployment import Deployment
from src.rest_api.croud.create import create_deployment

app = FastAPI()


@app.post("/deployments/", status_code=HTTP_201_CREATED, response_model=str)
def add_new_deployment() -> str:
    deployment: Deployment = Deployment(id=str(uuid.uuid4()), db_name="usernamedb_name", status="CREATED",
                                        username="username", creation_time=str(datetime.datetime.now()))
    create_deployment(deployment)
    return deployment.id


def main() -> None:
    print(add_new_deployment())
    uvicorn.run("create_deployment_route:app", host="127.0.0.1", port=8080, reload=True)


if __name__ == '__main__':
    main()
