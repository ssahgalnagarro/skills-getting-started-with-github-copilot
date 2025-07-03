.PHONY: help setup install install-dev run test format lint clean

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Setup virtual environment and install dependencies
	python3 -m venv venv
	@echo "Virtual environment created. Activate it with: source venv/bin/activate"
	@echo "Then run: make install"

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run: ## Run the development server
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8000

test: ## Run tests
	pytest tests/ -v

format: ## Format code with black
	black src/ --line-length 88
	isort src/

lint: ## Lint code with flake8
	flake8 src/ --max-line-length 88 --exclude __pycache__

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	rm -rf .coverage htmlcov/

dev: ## Start development server with auto-reload
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8000

prod: ## Run production server
	uvicorn src.app:app --host 0.0.0.0 --port 8000
