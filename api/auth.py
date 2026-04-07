from django.http import JsonResponse

VALID_API_KEYS = {
    "1b3e2a4939ef4c789821fba000123": "default-client"
}

def validate_api_key(request):
    key = request.headers.get("X-API-KEY")

    if not key or key not in VALID_API_KEYS:
        return JsonResponse({
            "status": "error",
            "message": "Unauthorized: Invalid or missing API key",
            "status_code": 401
        }, status=401)

    request.client_name = VALID_API_KEYS[key]  # optional
    return None