# AFL Vision Insight

A real-time player tracking and crowd monitoring system for AFL, using computer vision and FastAPI.

## Structure

- `backend/` - FastAPI backend with inference APIs
- `frontend/` - React.js dashboard
- `models/` - Trained YOLOv8 and segmentation models
- `docs/` - Technical documentation
---
## Getting Started
```bash

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/afl-vision-insight.git
   cd afl-vision-insight
   ```
   2. **Set up backend environment**
   ```bash
   cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # For PowerShell
pip install -r ../requirements.txt
```
```bash
3. **Start FastAPI backend**
uvicorn main:app --reload
```
4. Frontend(React) setup
```bash
cd ../frontend
npm install
npm start
```
---
Contributing
-Follow GitHub flow with feature branches.

- se meaningful commit messages.

- Tag team leads in PRs for review.

- Write weekly documentation in /docs/reports.
---