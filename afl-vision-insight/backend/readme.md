# AFL Vision Backend

### Setup Instructions
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs