# amplefastapi

Fastapi middleware for ampleanalytics

## Usage

```python
from amplefastapi import AmpleMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(AmpleMiddleware, project_id="project_id")
```
