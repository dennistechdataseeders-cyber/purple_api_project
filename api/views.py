from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .auth import validate_api_key
from .mongo import pl_collection, pdp_collection
from .utils import insert_unique_items


# ---------------- PL ENDPOINT ---------------- #

@api_view(["POST"])
@renderer_classes([JSONRenderer])
def pl_endpoint(request):

    # 🔐 Validate API Key
    auth_error = validate_api_key(request)
    if auth_error:
        return auth_error

    keywords = request.data.get("keywords", [])
    pincodes = request.data.get("pincodes", [])

    items_to_insert = [
        {"keyword": kw, "pincode": pin}
        for kw in keywords
        for pin in pincodes
    ]

    inserted, duplicates = insert_unique_items(
        collection=pl_collection,
        items=items_to_insert,
        pincode_field="pincode",
        item_field="keyword"
    )

    return Response({
        "status": "success",
        "message": f"{len(inserted)} inserted, {len(duplicates)} duplicates.",
        "inserted_count": len(inserted),
        "duplicate_count": len(duplicates),
        "inserted": inserted,
        "duplicates": duplicates
    }, status=200)



# ---------------- PDP ENDPOINT ---------------- #

@api_view(["POST"])
@renderer_classes([JSONRenderer])
def pdp_endpoint(request):

    # 🔐 Validate API Key
    auth_error = validate_api_key(request)
    if auth_error:
        return auth_error

    urls = request.data.get("urls", [])
    pincodes = request.data.get("pincodes", [])

    items_to_insert = [
        {"url": url, "pincode": pin}
        for url in urls
        for pin in pincodes
    ]

    inserted, duplicates = insert_unique_items(
        collection=pdp_collection,
        items=items_to_insert,
        pincode_field="pincode",
        item_field="url"
    )

    return Response({
        "status": "success",
        "message": f"{len(inserted)} inserted, {len(duplicates)} duplicates.",
        "inserted_count": len(inserted),
        "duplicate_count": len(duplicates),
        "inserted": inserted,
        "duplicates": duplicates
    }, status=200)