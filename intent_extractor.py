from pydantic import BaseModel
from typing import List, Optional

class AppIntent(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]
    constraints: Optional[dict] = None

def main():
    user_input = input("Enter your app requirements: ")
    
    # Now, assume you have a parsing function (you could call an LLM or write rules)
    parsed_data = parse_user_input(user_input)
    
    try:
        intent = AppIntent(**parsed_data)
        print("Validated Intent:", intent)
    except Exception as e:
        print("Invalid input:", e)
