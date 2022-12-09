# Cannot import name 'parse_rule' from 'werkzeug.routing'

https://bobbyhadz.com/blog/python-importerror-cannot-import-name-parse-rule-from-werkzeug-routing


pip install werkzeug==2.1.2
pip3 install werkzeug==2.1.2

## 👇️ if you don't have pip in PATH environment variable
python -m pip install werkzeug==2.1.2
python3 -m pip install werkzeug==2.1.2

## 👇️ py alias (Windows)
py -m pip install werkzeug==2.1.2

## 👇️ for Jupyter Notebook
!pip install werkzeug==2.1.2



# Additional Docker instructions 
## set working directory
- in Dockerfile add the following
```Dockerfile
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
```

## check config in docker logs
- add to `__init__.py`
```python
import sys
print(app.config, file=sys.stderr)
```
- docker-compose up -d --build
- docker-compose logs
- docker-compose down
- docker-compose exec api python -m pytest "src/tests"
## entrypoint chmod
 chmod 755 or 777 instead of +x.