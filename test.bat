set PYTHONPATH=%PYTHONPATH%;pwd
coverage run --timid --branch --source fe,be --concurrency=thread -m pytest %1 -v --ignore=be/utils
coverage combine
coverage report
coverage html