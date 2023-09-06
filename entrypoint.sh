#!/bin/sh

cd ./src

alembic upgrade heads

cd ..

exec python ./src/run.py