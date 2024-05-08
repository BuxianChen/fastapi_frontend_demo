from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 静态文件目录
app.mount("/dist", StaticFiles(directory="frontend/dist"), name="dist")

@app.get("/playground")
async def serve_playground():
    try:
        return FileResponse('frontend/index.html')
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

# 示例API路由
@app.post("/invoke")
async def invoke_api(data: dict):
    # 这里可以添加处理逻辑
    return {"result": f"Received: {data.get('text', 'No text provided')}"}