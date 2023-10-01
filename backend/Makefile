db:
	docker-compose up db -d --build
down:
	docker-compose down
	rm -r data
	mkdir data
dev:
	uvicorn main:app --host 0.0.0.0 --port 9999 --reload

test:
	pytest .