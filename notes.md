# Implement notes step by step from scratch

> Tham khảo template [Full Stack FastAPI PostgreSQL](https://github.com/tiangolo/full-stack-fastapi-postgresql)

## Features

- [x] **Poetry** for package management
- [ ] ??? for Code quality
- [ ] ??? for CI
- [ ] Docker image
- [ ] Docker run

## Poetry
```commandline
brew install poetry
poetry init
poetry install
poetry shell
```
> **_`Knowledge`_**
> - Quản lý package và môi trường ảo bằng Poetry => Tốt hơn cách cũ dùng virtualenvwrapper + pip

## First step
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

> **_`Knowledge`_**
> - FastAPI Helloworld

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

> **_`Knowledge`_**
> - [x] Debug ứng dụng FastAPI

## Running API tests locally
Follow guide [RealWorld API Spec](postman/README.md)

> **_`Knowledge`_**
> - [x] Sử dụng postman để run testcase theo lô

## First unit testcase
Follow guide [Testing](https://fastapi.tiangolo.com/tutorial/testing/) and [Async Tests](https://fastapi.tiangolo.com/advanced/async-tests/)
> Refactor sử dụng fixture client tham khảo [Full Stack FastAPI PostgreSQL](https://github.com/tiangolo/full-stack-fastapi-postgresql)

Cấu trúc thư mục tests
```
.
└── tests
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── test_users.py
    │   └── test_users_async.py
    └── conftest.py
```
> **_`Knowledge`_**
> - Unittest cho FastAPI sử dụng pytest

## First API: Register new user, login user
> Tham khảo [SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)

Cấu trúc file
```
.
├── LICENSE
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── deps.py
│   │   └── routers
│   ├── core
│   ├── crud
│   ├── db
│   ├── main.py
│   ├── models
│   ├── schemas
├── logo.png
├── notes.md
├── poetry.lock
├── postman
│   ├── Conduit.postman_collection.json
│   ├── README.md
│   ├── run-api-tests.sh
│   └── swagger.json
├── pyproject.toml
├── readme.md
└── tests
    ├── __init__.py
    ├── api
    └── conftest.py
```

- **db** SQLAlchemy parts:urit. Khai báo, cấu hình database
- **models** Database models. Class của các đối tượng ORM tương tác trực tiếp với database
- **schemas** Pydantic models. Đọc và ghi dữ liệu giao tiếp với API
- **api/deps.py** Chứa các biến phụ thuộc sử dụng trong các hàm API
- **api/routers** Chứa các Rest API function
- **crud** Chứa các class thao tác trực tiếp với dữ liệu trong database
- **core** Chứa các hàm/biến core để chạy app như config, sec
- **tests** Thư mục unittest sử dụng pytest

API implement
- POST /users: Đăng ký user mới
- POST /users/login: Đăng nhập user

> **_`Knowledge`_** 
> - Sử dụng SQL Database
> - Hoàn thành 1 API hoàn chỉnh
> - Cấu trúc thư mục cho 1 ứng dụng lớn sử dụng FastAPI
> - Sử dụng Faker để fake dữ liệu khi unittest

## Users API
API implement
- GET /users: Get Current User
- PUT /users: Update Current User

> **_`Knowledge`_** 
> - Utils function for unittest để setup dữ liệu cho testcase
> - pytest coverage report
>   ```commandline
>   pytest --cov-report term-missing --cov=app tests/
>   ```