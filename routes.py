from flask_restful import Resource
from flask import jsonify
from Models_psgr import BookModel, db

class Books(Resource):
    def get(self):
        books = BookModel.query.all()
        return jsonify([b.as_dict() for b in books])


class Book(Resource):
    def get(self, pk):
        book = BookModel.query.get(pk)
        if book:
            return jsonify(book.to_dict())
        return {"error": "Not found"}, 404


