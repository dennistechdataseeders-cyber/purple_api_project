from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .mongo import pl_collection, pdp_collection
from .utils import insert_unique_items
import uuid
from datetime import datetime
from django.http import JsonResponse
from .mongo import pl_collection, logs_collection
import json


@api_view(["POST"])
@renderer_classes([JSONRenderer])
def pl_endpoint(request):
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

    message = f"{len(inserted)} inserted, {len(duplicates)} duplicates."

    # --------------------------
    # CREATE JOB LOG ENTRY
    # --------------------------
    # generate unique job id
    while True:
        job_id = str(uuid.uuid4())[:8]
        if not logs_collection.find_one({"job_id": job_id}):
            break

    now = datetime.now()

    log_entry = {
        "job_id": job_id,
        "payload": {
            "keywords": keywords,
            "pincodes": pincodes
        },
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "status_code": 200,
        "message": message
    }

    # insert into logs collection
    try:
        logs_collection.insert_one(log_entry)
    except Exception as e:
        print("Log Insert Error:", e)

    # --------------------------

    return Response({
        "status": "success",
        "message": message,
        "inserted_count": len(inserted),
        "duplicate_count": len(duplicates),
        "job_id": job_id,
        "log_saved": True
    }, status=200)

@api_view(["POST"])
@renderer_classes([JSONRenderer])
def pdp_endpoint(request):
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

    message = f"{len(inserted)} inserted, {len(duplicates)} duplicates."

    # --------------------------
    # CREATE JOB LOG ENTRY
    # --------------------------

    # generate unique job id
    while True:
        job_id = str(uuid.uuid4())[:8]
        if not logs_collection.find_one({"job_id": job_id}):
            break

    now = datetime.now()

    log_entry = {
        "job_id": job_id,
        "payload": {
            "urls": urls,
            "pincodes": pincodes
        },
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "status_code": 200,
        "message": message
    }

    # insert into logs collection
    try:
        logs_collection.insert_one(log_entry)
    except Exception as e:
        print("Log Insert Error:", e)

    # --------------------------

    return Response({
        "status": "success",
        "message": message,
        "inserted_count": len(inserted),
        "duplicate_count": len(duplicates),
        "job_id": job_id,
        "log_saved": True
    }, status=200)