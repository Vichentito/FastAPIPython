from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from uuid import uuid4 as uuid

app = FastAPI()

posts = [
    {
        "id": "a7be68a0-87f6-4972-acf1-3207bf43629c",
        "title": "titulo 1",
        "author": "autor 1",
        "content": "contenido 1",
        "created_at": "2022-07-06T23:06:03.446943",
        "published_at": None,
        "published": False
    },
    {
        "id": "73327b23-84cb-4f6e-a6f1-89615e476393",
        "title": "titulo 2",
        "author": "autor 2",
        "content": "contenido 2",
        "created_at": "2022-07-06T23:06:03.446943",
        "published_at": None,
        "published": False
    },
    {
        "id": "ff1a98e7-7c9c-4238-b6ad-2181a1c2b36d",
        "title": "titulo 3",
        "author": "autor 3",
        "content": "contenido 3",
        "created_at": "2022-07-06T23:06:03.446943",
        "published_at": None,
        "published": False
    },
    {
        "id": "a932802b-1309-44fd-918f-1ad72cee223e",
        "title": "titulo 4",
        "author": "autor 4",
        "content": "contenido 4",
        "created_at": "2022-07-06T23:06:03.446943",
        "published_at": None,
        "published": False
    }
]

# Create a model for the schema of the post


class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


@app.get("/posts")
def get_posts():
    return posts


@app.post("/posts")
def create_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return post


@app.get("/posts/{post_id}")
def get_post(post_id: str):
    print(post_id, type(post_id))
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.put("/posts/{post_id}")
def update_post(post_id: str, post: Post):
    for post_index, post_item in enumerate(posts):
        if post_item["id"] == post_id:
            posts[post_index]["title"] = post.title
            posts[post_index]["author"] = post.author
            posts[post_index]["content"] = post.content
            return post_item
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for post_index, post_item in enumerate(posts):
        if post_item["id"] == post_id:
            posts.pop(post_index)
            return {"message": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")
