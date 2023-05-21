#!/bin/sh -e

flake8 app/
black app/
isort app/