# ![RealWorld Example App](logo.png)

> ### [FastAPI] codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.


### [Demo](https://github.com/gothinkster/realworld)&nbsp;&nbsp;&nbsp;&nbsp;[RealWorld](https://github.com/gothinkster/realworld)


This codebase was created to demonstrate a fully fledged fullstack application built with **[FastAPI]** including CRUD operations, authentication, routing, pagination, and more.

We've gone to great lengths to adhere to the **[FastAPI]** community styleguides & best practices.

For more information on how to this works with other frontends/backends, head over to the [RealWorld](https://github.com/gothinkster/realworld) repo.


# How it works

> Describe the general architecture of your app here
```
 ❯ tree -L 3                                                                                                                                 [18:15:07]
.
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

5 directories, 13 files
```

# Getting started

```
poetry shell
uvicorn app.main:app --reload
```

Open [Swagger docs](http://127.0.0.1:8000/docs) or [Redoc](http://127.0.0.1:8000/redoc)

