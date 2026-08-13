from typing import List, TypedDict

class BlogState(TypedDict):
    topic: str
    outline: List[str]
    draft: str
    feedback: str
    revision_count: int
    is_approved: bool