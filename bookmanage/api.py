from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

#- 책 목록을 보여주는 GET 엔드포인트를 만듭니다.
# 새 책을 추가하는 POST 엔드포인트를 만듭니다.
#- 특정 책의 정보를 업데이트하는 PUT 엔드포인트를 만듭니다.
#- 특정 책을 삭제하는 DELETE 엔드포인트를 만듭니다.
# 책의 데이터는 메모리 내의 간단한 리스트로 관리합니다.

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

# 엔드포인트 구현...
@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
        return books
    # 200일땐 그냥 돌려주는것 같고...

    @book_blp.arguments(BookSchema) #put같은 경우, arguments를 통해 스키마 검증을 함
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) +1    #len에 1 추가하면 새 id값으로 적절하겠지?
        books.append(new_data)
        return new_data
    # 201일땐 책 추가해 주는거고

@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.")
        return book
    
    # put(수정)
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.")
        book.update(new_data)
        return book
    
    # delete(삭제)
    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.")
        books = [book for book in books if book['id'] != book_id]
        return ''