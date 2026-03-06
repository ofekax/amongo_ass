import uuid

import uvicorn
from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED

from src.models.deployment.deployment import Deployment
from src.rest_api.croud.create.create_deployment import create_deployment
from src.rest_api.croud.create.create_deployment_route import add_new_deployment

app = FastAPI()

@app.post("/deployments/", status_code=HTTP_201_CREATED, response_model=str)
def add_new_deployment() -> str:
    deployment: Deployment = Deployment(id=str(uuid.uuid4()), db_name="userexample_db", status="CREATED",
                                        username="userexample", creation_time=str(datetime.datetime.now()))
    create_deployment(deployment)
    return deployment.id


def send_request() -> None:
    uvicorn.run("create_deployment_route:app", host="127.0.0.1", port=8080, reload=True)

def main() -> None:
    send_request()


if __name__ == '__main__':
    main()
