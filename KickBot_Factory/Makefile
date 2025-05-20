install:
	pip install -r backend/requirements.txt
	cd frontend && npm install --force

run-backend:
	cd backend && uvicorn main:app --reload

run-frontend:
	cd frontend && npx vite --force

structure:
	git ls-tree -r --name-only HEAD

display:
	display.bat

start:
	@echo Installing backend and frontend dependencies...
	@$(MAKE) install
	@echo Starting backend and frontend...
	cmd /c start cmd /k "cd backend && uvicorn main:app --reload"
	cmd /c start cmd /k "cd frontend && npx vite --force"
