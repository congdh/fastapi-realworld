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

## Refactor code

- [x] Editor config
- [x] Improve OpenAPI document
- [x] Unittest CRUD
- [x] Alembic
- [ ] Async SQL (Relational) Databases? => reference [FastAPI Users
](https://frankie567.github.io/fastapi-users/configuration/databases/sqlalchemy/)

> **_`Knowledge`_** 
> - Editor config
> - devtool: Python's missing debug print command and other development tools.
> - [Schema Extra - Example](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
> - Protect password field with SecretStr type
> - [ ] Design users management system
> - [x] Migrate SQL database
> - [x] Unittest database
> - [ ] Async SQL Database with FastAPI
> - [ ] FastAPI on_event startup, shutdown

### Refactor code - Alembic
> Reference: [FastAPI with SQLAlchemy, PostgreSQL and Alembic and of course Docker [Part-1]](https://medium.com/@ahmed.nafies/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)

Add alembic package using poetry
```commandline
poetry add alembic
``` 

Init alembic
```commandline
alembic init alembic
```

that will create config file `alembic.ini` and directory `alembic`

In config file `alembic.ini`, change line 38
```ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```

to URI connection of database (SQLite)
```ini
sqlalchemy.url = sqlite:///./sql_app.db
```

Create `base.py` file in directory `app/db` and import all models before uses it in alembic. File `base.py` look like this
```python
# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.users import User  # noqa
```

In file `alembic/env.py`, set target metadata from `None` to `app.db.base.Base.metadata` 

```python
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from app.db.base import Base
target_metadata = Base.metadata
```

Add 2 line below at head line for add sys.path relative to the current running script
```python
import sys, pathlib
sys.path.append(str(pathlib.Path().absolute()))
```
OK, now lets delete old SQLite file and make our first migration
```shell script
find . -name sql_app.db | xargs rm
alembic revision --autogenerate -m "First migration"
```
then migrate database
```shell script
alembic upgrade head
```

> **_`Knowledge`_**
> - Migrate SQL database using Alembic

### Refactor code - Formating & Linting
> References:
>
> - [MY PYTHON PROJECT SETUP](https://srcco.de/posts/my-python-poetry-project-setup-calver-2020.html)
>
> - [Blazing fast CI with GitHub Actions, Poetry, Black and Pytest](https://medium.com/@vanflymen/blazing-fast-ci-with-github-actions-poetry-black-and-pytest-9e74299dd4a5)

Install packages

```commandline
poetry add --dev black --allow-prereleases
poetry add --dev isort
poetry add --dev autoflake
poetry add --dev mypy
poetry add --dev flake8
```

Create [Makefile](Makefile)
Run make command with option you want

```commandline
make format
make lint
```

> **_`Knowledge`_**
> - Code formating tools: Black, autoflake, isort
> - Code linting tools: Flake8, MyPy
> - Make to leverage muscle memory