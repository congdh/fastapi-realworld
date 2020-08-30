# Implement notes step by step from scratch

## Cấu trúc project
> Tham khảo template [Full Stack FastAPI PostgreSQL](https://github.com/tiangolo/full-stack-fastapi-postgresql)

- [x] **Poetry** for package management
- [ ] ??? for Code quality
- [ ] ??? for CI
- [ ] Docker image
- [ ] Docker run

## Poetry
```
brew install poetry
poetry init
poetry install
poetry shell
```

### First step
Cấu trúc thư mục và hực hiện theo tutorial [FastAPI Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

> Bỏ route items do chỉ cần setup 1 API đơn giản nhất để test cấu hình và môi trường

Cấu trúc thư mục
```
❯ tree -L 3                                                         [17:30:11]
.
├── BACKEND_INSTRUCTIONS.md
├── FRONTEND_INSTRUCTIONS.md
├── MOBILE_INSTRUCTIONS.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── main.py
│   └── routers
│       ├── __init__.py
│       ├── __pycache__
│       └── users.py
├── logo.png
├── notes.md
├── poetry.lock
├── postman
│   ├── Conduit.postman_collection.json
│   ├── README.md
│   ├── run-api-tests.sh
│   └── swagger.json
├── pyproject.toml
└── readme.md
```

Run & test
```
uvicorn app.main:app --reload
```
Open docs http://127.0.0.1:8000/docs

## Debugging
Làm theo tutorial [FastAPI Debugging](https://fastapi.tiangolo.com/tutorial/debugging/)
> Khi chạy nếu báo lỗi
> ```Traceback (most recent call last):
>  File "[path to project]/app/main.py", line 4, in <module>
>    from .routers import users
>  ImportError: attempted relative import with no known parent package
> ```
> thì phải sửa lại cách import sử dụng relative path từ
>
> ```from .routers import users```
>
> thành absolute path
>
>```from app.routers import users```

## Running API tests locally
Follow guide [RealWorld API Spec](postman/README.md)