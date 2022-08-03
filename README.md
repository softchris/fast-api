# My first Fast API app

## Install Fast API

1. Create a virtual environment:

   ```console
   python3 -m venv fast-env
   ```

   This creates a virtual environment **fast-env**.

1. Active the virtual environment

   ```console
   source fast-env/bin/activate
   ```

1. Create a *requirements.txt* file and add **fastapi** at the top of the file:

   ```console
   touch requirements.txt
   ```

1. Install fastapi by installing dependencies from *requirements.txt*:

   ```console
   python -m pip install -r requirements.txt
   ```

1. Install a tool `uvicorn` that will help you run your app:

   ```console
   pip install "uvicorn[standard]"
   ```

## Create your app

1. Create *main.py* and give it the following content:

   ```python
   from fastapi import FastAPI

   app = FastAPI()
    
   @app.get("/")
   async def root():
      return {"message": "Hello World"}
   ```

1. Run the following command in the console to run the app:

   ```console
   uvicorn main:app --reload
   ```

   > The command uvicorn main:app refers to:

   > main: the file main.py (the Python "module").
app: the object created inside of main.py with the line app = FastAPI().
   > --reload: make the server restart after code changes. Only use for development.

   You will see output similar to:

   ```output
    INFO:     Will watch for changes in these directories: ['/Users/chnoring/Documents/dev/projects/python-projects/fast-demo']

    INFO:     Uvicorn running on <http://127.0.0.1:8000> (Press CTRL+C to quit)
    INFO:     Started reloader process [93679] using WatchFiles
    INFO:     Started server process [93684]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
   ```

1. Navigate to **<http://127.0.0.1:8000/>** in a browser and you will see the following JSON output:

   ```json
   {
      "message": "Hello World"
   }
   ```

## Open API docs

1. Navigate to <http://127.0.0.1:8000/docs>

   You will see the following:

   ![swagger](swagger.png)

1. Navigate to <http://127.0.0.1:8000/redoc> if you want to see the same docs using Redoc standard.

1. To see the Open API JSON doc, go to <http://127.0.0.1:8000/openapi.json>

   Here's the JSON output:

   ```json
   {
    "openapi": "3.0.2",
        "info": {
            "title": "FastAPI",
            "version": "0.1.0"
        },
        "paths": {
            "/": {
                "get": {
                    "summary": "Root",
                    "operationId": "root__get",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {
                                "application/    json": {
                                        "schema": {}
                                    }
                            }
                        }
                    }
                }
            }
        }
    }
    // 20220801165325
    // <http://127.0.0.1:8000/openapi.json>
    ​
    {
      "openapi": "3.0.2",
      "info": {
        "title": "FastAPI",
        "version": "0.1.0"
      },
      "paths": {
        "/": {
          "get": {
            "summary": "Root",
            "operationId": "root__get",
            "responses": {
              "200": {
                "description": "Successful Response",
                "content": {
                  "application/json": {
                    "schema": {
    
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

   ```
