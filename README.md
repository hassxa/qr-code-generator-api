# QR Code Generator API

A lightweight, stateless REST API built with **Python**, **FastAPI**, and **Docker** that generates customizable QR codes from text or URLs.

The project demonstrates API development, containerization, automated testing, and cloud deployment practices using AWS.

> **Project Status:** Docker implementation completed and tested locally. AWS deployment in progress.

## Tech Stack

- **Python 3.12** – Backend development
- **FastAPI** – REST API framework
- **Uvicorn** – ASGI server
- **QRCode & Pillow** – QR code generation
- **Docker** – Application containerization
- **Pytest** – Automated testing
- **AWS ECR** – Container image registry (in progress)
- **AWS ECS & Fargate** – Cloud container deployment (planned)

## Features

- Generate QR codes from text or URLs.
- Customize QR code size and border.
- Download generated QR codes as PNG images.
- Input validation using FastAPI.
- Automatic API documentation with Swagger UI.
- Health check endpoint.
- Stateless architecture without database dependencies.
- Containerized execution using Docker.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check API health status |
| GET | `/qr?text=hello` | Generate a QR code in PNG format |
| GET | `/docs` | Interactive Swagger UI documentation |

### QR Code Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | string | Required | Text or URL to encode (1–1000 characters) |
| `box_size` | integer | 10 | Size of each QR code module (2–20) |
| `border` | integer | 4 | Border width in modules (1–10) |

### Example Request

```http
GET /qr?text=https://www.google.com&box_size=10&border=4
```

The API returns a PNG image containing the generated QR code.

All QR codes are generated in memory. No user data is stored.

## Local Development

### Prerequisites

- Python 3.12+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/hassxa/qr-code-generator-api.git

cd qr-code-generator-api
```

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
py -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements-dev.txt
```

### 4. Start the Application

```powershell
uvicorn app.main:app --reload
```

The application will be available at:

http://localhost:8000/docs

## Docker Deployment

The application is containerized using Docker, allowing consistent execution across different environments.

### 1. Build the Docker Image

```bash
docker build -t qr-code-generator-api:1.0 .
```

This command builds a Docker image using the instructions defined in the Dockerfile.

### 2. Verify the Image

```bash
docker images
```

### 3. Run the Container

```bash
docker run --rm -p 8000:8000 qr-code-generator-api:1.0
```

This command creates and starts a container from the previously built image.

The application runs on port 8000.

### 4. Verify the Deployment

**Health Check**

http://localhost:8000/health

Expected response:

```json
{
  "status": "ok"
}
```

**Swagger Documentation**

http://localhost:8000/docs

**QR Code Generation**

http://localhost:8000/qr?text=HelloWorld

### Docker Implementation Details

The Docker configuration includes:

- Python 3.12 slim base image.
- Optimized dependency installation using Docker layer caching.
- Non-root user execution for improved security.
- Environment variables for Python runtime behavior.
- Container health checks.
- Port 8000 exposure and port mapping.
- `.dockerignore` to exclude unnecessary files.
- Stateless container architecture.

## Docker Demonstration

The application has been successfully built and executed locally using Docker Desktop.

### Docker Image

The Docker image was successfully created using the project's Dockerfile.

![Docker Image](docs/screenshots/docker-image.png)

### Running Container

The container executes the FastAPI application and exposes port 8000.

![Docker Container](docs/screenshots/docker-container.png)

### API Demonstration

The application generates QR codes through its REST API.

The following screenshot shows a successful HTTP 200 response and the generated PNG image using Swagger UI.

![QR Code Generation](docs/screenshots/qr-generation.png)

## Automated Testing

The project includes automated tests using **Pytest** and FastAPI's TestClient.

The tests cover:

- Health check endpoint.
- Successful PNG generation.
- Empty text validation.
- Missing required parameters.
- Maximum text length validation.
- Invalid QR code size validation.

Run the tests using:

```bash
pytest -q
```

## AWS Deployment

The cloud deployment is currently in progress.

The planned architecture uses:

- **Amazon ECR** to store Docker container images.
- **Amazon ECS** to manage container deployment.
- **AWS Fargate** to execute containers without managing servers.
- **Amazon CloudWatch** for application logging and monitoring.

**AWS Region:** Europe (Spain) – `eu-south-2`

Deployment instructions and verification screenshots will be added once the AWS deployment is completed.

## Future Improvements

- Deploy the application on AWS ECS with Fargate.
- Implement Infrastructure as Code using Terraform.
- Deploy the application locally using Kubernetes.
- Configure a CI/CD pipeline with GitHub Actions.

## License

This project is licensed under the MIT License.