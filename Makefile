#!/bin/bash

VER=$(shell grep __version__ negar_cli/config.py|cut -d= -f2|tr -d '\" '|head -1)

.ONESHELL:

ver:
	@echo negar-cli ver. "$(VER)"

.PHONY: uninstall
uninstall:
	@echo "Uninstalling negar-cli ..."
	pip uninstall negar-cli

setup: ver
	python setup.py sdist
	python setup.py bdist_wheel

lins: ver setup
	pip install "dist/negar_cli-$(VER)-py3-none-any.whl"

pins: ver
	pip install negar-cli=="$(VER)"

upypi: setup
	twine upload "dist/negar-cli-$(VER).tar.gz"

utest: setup
	twine upload -r testpypi "dist/negar-cli-$(VER).tar.gz"

upload: setup upypi utest

clean:
	@find . -type d -name __pycache__ -exec rm -rfv {} +
	@rm negar_cli.egg-info/ -rfv
	@rm build/ -rfv
	@rm dist/ -rfv
	@rm gui.build/ -rfv
	@rm gui.dist/ -rfv
	@rm negar*.spec -rfv
