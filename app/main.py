"""HTTP endpoints for generating QR codes without persistent storage."""

from io import BytesIO

import qrcode
from fastapi import FastAPI, Query
from fastapi.responses import Response

app = FastAPI(
    title="QR Code Generator API",
    description="Generate downloadable PNG QR codes from text or URLs.",
    version="1.0.0",
)


@app.get("/health", tags=["Health"])
def health() -> dict[str, str]:
    """Lightweight readiness endpoint for local use and container checks."""
    return {"status": "ok"}


@app.get(
    "/qr",
    tags=["QR codes"],
    response_class=Response,
    responses={200: {"content": {"image/png": {}}, "description": "QR code PNG"}},
)
def generate_qr(
    text: str = Query(min_length=1, max_length=1000, description="Text or URL to encode"),
    box_size: int = Query(default=10, ge=2, le=20),
    border: int = Query(default=4, ge=1, le=10),
) -> Response:
    """Create a QR code in memory, returning a PNG without saving user input."""
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    output = BytesIO()
    qr_image.save(output, format="PNG")
    return Response(content=output.getvalue(), media_type="image/png")
