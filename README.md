# QR Code Generator API

A small, stateless API that generates PNG QR codes from text or URLs. Built with **Python**, **FastAPI**, and **Docker**.

> AWS ECS/Fargate deployment is planned; it has **not** been deployed yet.

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Return `{"status": "ok"}` |
| GET | `/qr?text=hello` | Generate a QR code as a PNG image |
| GET | `/docs` | Interactive OpenAPI documentation |

`/qr` also accepts `box_size` (2–20, default 10) and `border` (1–10, default 4). Text is limited to 1,000 characters. QR codes are generated in memory; nothing is stored.

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs and try `/qr` with `text=https://example.com`.

## Run with Docker

```powershell
docker build -t qr-code-generator-api:local .
docker run --rm -p 8000:8000 qr-code-generator-api:local
```

Then visit http://localhost:8000/qr?text=hello to see a QR code. Stop the container with **Ctrl+C**.

## Run tests

```powershell
pytest -q
```

## Next steps

- Build and test the Docker image locally.
- Push the image to Amazon ECR.
- Launch a short-lived deployment in Amazon ECS with Fargate.
- Document the infrastructure and remove AWS resources after testing to control costs.
