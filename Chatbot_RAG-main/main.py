from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi

app = FastAPI() # gọi constructor và gán vào biến app


@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id = "default_item"):
    return {"item_id": item_id}