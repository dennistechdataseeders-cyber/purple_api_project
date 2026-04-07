from rest_framework.response import Response
from rest_framework import status

VALID_API_KEY = "1b3e2a4939ef4c789821fba000123abc"

def validate_api_key(request):
    api_key = request.headers.get("X-API-KEY")

    if not api_key:
        return Response(
            {"status": "error", "message": "Missing API Key"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if api_key != VALID_API_KEY:
        return Response(
            {"status": "error", "message": "Invalid API Key"},
            status=status.HTTP_403_FORBIDDEN
        )

    return None