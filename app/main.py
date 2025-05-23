print("✅ Loading main.py ...")

# นำเข้า FastAPI จากไลบรารี
from fastapi import FastAPI

# สร้าง instance หลักของแอป FastAPI
app = FastAPI()

# Endpoint หลัก เมื่อเข้า http://localhost:8000/
@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}

# Endpoint สำหรับ Health Check
# เมื่อเข้า http://localhost:8000/health
@app.get("/health")
async def health():
    return {"status": "ok"}
