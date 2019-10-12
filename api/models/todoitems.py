from api.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Todo {self.text}>'


class TodoSchema(ma.ModelSchema):
    class Meta:
        model=TodoItem
        sqla_session = db.session

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
