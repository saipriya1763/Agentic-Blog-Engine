from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.planner import plan_article
from agents.writer import write_article
from agents.editor import edit_article

# Define State Schema
class BlogState(TypedDict):
    topic: str
    outline: str
    draft: str
    final_post: str

# Define Node Functions
def planner_node(state: BlogState):
    print("📝 Planning outline...")
    outline = plan_article(state["topic"])
    return {"outline": outline}

def writer_node(state: BlogState):
    print("✍️ Writing draft...")
    draft = write_article(state["topic"], state["outline"])
    return {"draft": draft}

def editor_node(state: BlogState):
    print("🔍 Editing and polishing post...")
    final_post = edit_article(state["topic"], state["draft"])
    return {"final_post": final_post}

# Build State Graph
builder = StateGraph(BlogState)

builder.add_node("planner", planner_node)
builder.add_node("writer", writer_node)
builder.add_node("editor", editor_node)

builder.set_entry_point("planner")
builder.add_edge("planner", "writer")
builder.add_edge("writer", "editor")
builder.add_edge("editor", END)

app = builder.compile()

# Run Engine
if __name__ == "__main__":
    topic = "The Future of Multi-Agent Systems in AI"
    print(f"🚀 Launching Agentic Blog Engine for topic: '{topic}'")

    initial_state = {"topic": topic, "outline": "", "draft": "", "final_post": ""}
    final_state = app.invoke(initial_state)

    print("\n==================== FINAL EDITED BLOG ====================\n")
    print(final_state["final_post"])

    # Save to file
    with open("blog_post.md", "w", encoding="utf-8") as f:
        f.write(final_state["final_post"])

    print("\n💾 Article saved to blog_post.md!")