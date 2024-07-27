from fastapi import HTTPException

class ItemNotFoundException(HTTPException):
    def __init__(self, item_id: int):
        super().__init__(status_code=404, detail=f"Item with id {item_id} not found")

class UserNotAuthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="User not authorized to perform this action")

