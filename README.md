# FastAPI with TypeScript frontend Demo

运行

```bash
cd frontend
yarn install
yarn build
cd ..
# install some python packages (omit)
uvicorn run backend.main:app
```

上面的运行方法会对外暴露两个 endpoint:

- `/invoke`: 一个 POST 接口, 既被用于 `/playground`, 也可以被单独调用
- `/playground`: GET, 用于网页浏览模式, 用户可以与之进行交互, 触发 `frontend/dist/script.js`, 而这个 javascript 脚本会触发对 `/invoke` 的调用

用法 1: 单独调用 `/invoke`

```python
import requests
resp = requests.post(
    "http://localhost:8000/invoke",
    json={"text": "12345"}
)
print(resp.json())
```

用法 2: 打开 `http://localhost:8000/playground`, 在输入框输入并点击 invoke 按钮
