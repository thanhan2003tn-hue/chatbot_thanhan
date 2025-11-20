# Hệ thống Chatbot Hỗ trợ Sinh viên
## 1. Giới thiệu
Đây là một dự án **Web Application kết hợp Streamlit và FastAPI** nhằm hỗ trợ sinh viên và tư vấn tuyển sinh tại **Trường Đại học Kỹ thuật Công nghiệp, Thái Nguyên**.  
Hệ thống cho phép:
- Sinh viên tra cứu thông tin học tập, quy chế đào tạo, tuyển sinh,...
- Quản trị viên quản lý dữ liệu, upload tài liệu, và train lại chatbot.
- Người dùng giao tiếp trực tiếp với Chatbot để nhận thông tin chính xác và nhanh chóng.

---

## 2. Cấu trúc dự án
├─ app.py # Frontend Streamlit, giao diện người dùng, đăng nhập và Chatbot

├─ serve.py # Backend FastAPI, xử lý upload file, retrain, RAG chain và trả lời câu hỏi

├─ main.py # FastAPI demo cơ bản (có thể dùng để kiểm tra server)

├─ data/ # Thư mục chứa các file dữ liệu: PDF, DOCX, TXT, CSV, Excel

├─ vectordb/ # Lưu trữ vector store của hệ thống Chatbot

├─ config.yaml # Cấu hình đăng nhập người dùng (admin, sinh viên)

├─ requirements.txt # Thư viện cần thiết


---
<img width="1851" height="3840" alt="image" src="https://github.com/user-attachments/assets/54ff0268-d6b8-4d50-8510-a44ef0be0613" />
---


## 3. Chức năng chính

### **A. Giao diện Streamlit (`app.py`)**
- Đăng nhập người dùng: `admin` hoặc `sinhvien`.
- Hiển thị **header và sidebar** chuyên nghiệp.
- **Admin**:
  - Upload file PDF, DOCX, TXT, CSV, XLSX.
  - Train lại toàn bộ dữ liệu để cập nhật chatbot.
- **Sinh viên**:
  - Tra cứu thông tin học tập dựa trên mã sinh viên.
  - Nhận gợi ý môn học tiếp theo dựa trên tín chỉ đã học.
- Chat trực tiếp với **Chatbot** để nhận câu trả lời từ dữ liệu đã upload.

### **B. Backend FastAPI (`serve.py`)**
- **Endpoints chính**:
  - `/ask`: Nhận câu hỏi từ frontend, trả lời dựa trên RAG chain.
  - `/retrain`: Train lại toàn bộ vector store từ dữ liệu mới.
  - `/uploadfile/`: Upload tài liệu, chia nhỏ, lưu vào vector store.
- Xử lý:
  - Load dữ liệu từ file (PDF, TXT, DOCX, CSV, Excel).
  - Chia nhỏ văn bản và tạo **vector store**.
  - Xử lý RAG chain để trả lời câu hỏi dựa trên dữ liệu.
  - Phân loại câu hỏi: liên quan sinh viên, tuyển sinh, hoặc chung.

---

## 4. Công nghệ sử dụng
- **Frontend**: Streamlit, Streamlit Option Menu
- **Backend**: FastAPI, Pydantic
- **Xử lý dữ liệu**: pandas, langchain, huggingface embeddings
- **Xử lý file**: PyPDFLoader, TextLoader, Docx2txtLoader, CSVLoader, UnstructuredExcelLoader
- **Bảo mật đăng nhập**: bcrypt, streamlit_authenticator
- **Môi trường**: Python >= 3.10, uvicorn

---


