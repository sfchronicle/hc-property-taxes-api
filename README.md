# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!


---

## Running Locally on Rancher Desktop

### 1️⃣ Install Rancher Desktop

Download and install Rancher Desktop
Ensure that Docker runtime is enabled

### 2️⃣ Build the Docker Image
Navigate to the project directory where the Dockerfile is located and run:
`docker build -t hc-property-taxes-api .`

### 3️⃣ Run the Container

`docker run -d -p 8000:8081 --name tax-data-api hc-property-taxes-api`

### 4️⃣ Verify the Running Container

To check if the container is running:

`docker ps`

You should see tax-appeal-api running.

### 5️⃣ Access the API Locally

Open your browser or use Postman:http://localhost:8000/docs (Swagger UI)

Or test using curl:

`curl http://localhost:8000`

### 6️⃣ Stopping and Removing the Container

To stop the container:

`docker stop tax-data-api`

To remove the container:

`docker rm tax-data-api`
