install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

run-backend:
	cd backend && uvicorn main:app --reload

run-frontend:
	cd frontend && npm run dev

structure:
	tree /F /A | findstr /V /G:.gitignore
