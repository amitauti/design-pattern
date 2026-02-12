# Model Deployment Example (skeleton)

Minimal skeleton demonstrating a containerized model-serving app.

Files:

- `app.py` — minimal Flask app that serves a dummy prediction.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — builds a container image.
- `docker-compose.yml` — local compose for quick start.

Run locally:

```bash
docker-compose up --build
# then visit http://localhost:5000/predict
```
