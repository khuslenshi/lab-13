from fastapi import HTTPException


def validate_priority(priority: str):
    allowed = {"low", "medium", "high"}
    if priority and priority not in allowed:
        raise HTTPException(status_code=400, detail=f"Priority must be one of: {', '.join(allowed)}")


def validate_status(status: str):
    allowed = {"todo", "in_progress", "done"}
    if status and status not in allowed:
        raise HTTPException(status_code=400, detail=f"Status must be one of: {', '.join(allowed)}")


def validate_limit(limit: int):
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 100")


def validate_search_query(search: str):
    if search and len(search.strip()) == 0:
        raise HTTPException(status_code=400, detail="Search query cannot be empty")
    if search and len(search) > 200:
        raise HTTPException(status_code=400, detail="Search query too long (max 200 chars)")
    return search.strip() if search else search

