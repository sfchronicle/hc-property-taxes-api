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

`docker run -d -p 8081:8000 --name tax-data-api hc-property-taxes-api`

### 4️⃣ Verify the Running Container

To check if the container is running:

`docker ps`

You should see tax-appeal-api running.

### 5️⃣ Access the API Locally

Open your browser or use Postman:http://localhost:8081/docs (Swagger UI)

Or test using curl:

`curl http://localhost:8081`

### 6️⃣ Stopping and Removing the Container

To stop the container:

`docker stop tax-data-api`

To remove the container:

`docker rm tax-data-api`

---

## Deploying on devhub01 and devhub02

The application is deployed on two DevHub Rackspace servers: [devhub01](devhub01.dfw3.hearstnp.com) and [devhub02](devhub02.dfw3.hearstnp.com). _Repeat the following steps on both servers!_

**Prerequisites:**

- A user account on devhub1 and devhub2.
- A github ssh key in your user folder on devhub1 and devhub2.
    - Test by logging into the server and running: `ssh -T git@github.com`
    - If that doesn't work, SFTP/copy your ssh `config`, `id_ed25519`, and `id_ed25519.pub` files to your .ssh folder on the server (`/home/<user-name>/.ssh`)

**Steps to deploy:**
_Repeat the following steps on both servers!_

1. SSH into the server: `ssh devhub1`
2. Navigate to the project directory: `cd /var/www/deploy/public/hc-property-taxes-api`
3. Pull the latest from Github: `git pull origin main`
4. Restart the docker container:
  `docker stop tax-data-api`
  `docker rm tax-data-api`
  `docker build -t hc-property-taxes-api .`
  `docker run -d -p 8080:8080 --restart=always --name tax-data-api hc-property-taxes-api`
5. Verify the container is running: `docker ps`
6. _Repeat these steps on devhub2._


**One-time setup:**
_Remember to set this up on both servers!_

- Copy the following two files to the project folder (`/var/www/deploy/public/hc-property-taxes-api`) via SFTP:
    - .env
    - bad_words.txt

---
