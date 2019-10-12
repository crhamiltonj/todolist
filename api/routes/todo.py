from flask import Blueprint, request
from flask_restplus import Api, Resource, fields, reqparse
from api.models.todoitems import TodoItem
from api.models.todoitems import ma, todo_schema, todos_schema
from api.db import db

td_bp = Blueprint("api", __name__, url_prefix="/api/v1_0")
api = Api(td_bp, doc="/doc/")

td = api.namespace("todos", description="TODO operations")


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


@td.route("/")
class TodoItems(Resource):
    """Show a list of todo items and POST to add a new item"""

    @td.doc("Show all todo items")
    def get(self):
        results = TodoItem.query.all()
        return todos_schema.dump(results)

    @td.doc("Add a new todo item")
    def post(self):
        if request.method == "POST":
            todoitem = todo_schema.load(request.get_json())
            db.session.add(todoitem)
            db.session.commit()
            return {"message": "New Item Added"}


@td.route("/<int:id>")
@td.response(404, "Todo item not found")
@td.param("id", "The task identifier")
class Todo(Resource):
    """View, Update or Delete a todo item"""

    @td.doc("get todo")
    def get(self, id):
        result = TodoItem.query.get(id)
        return todo_schema.dump(result)

    @td.doc("delete the todo item for id")
    def delete(self, id):
        item = TodoItem.query.get(id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item Deleted"}

    @td.doc("Update text of todo")
    @td.param("id", "The task identifier")
    def put(self, id):
        item = TodoItem.query.get(id)
        req = request.get_json()
        print(req["text"])
        item.text = req["text"]
        db.session.commit()
        return todo_schema.dump(item)



