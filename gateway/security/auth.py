from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from config import settings

# This tells FastAPI to look for a key in the request headers
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Security(api_key_header)):
    # Check if the key matches what we have in config
    if api_key != settings.GATEWAY_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    return api_key