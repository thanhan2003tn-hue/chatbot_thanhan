#uvicorn serve:app --reload
import os
import shutil
from typing import Dict, Any, List, TypedDict
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, CSVLoader, \
    UnstructuredExcelLoader
from pathlib import Path
import logging

# Thêm các import cần thiết từ các file của bạn
from core.embeding.HuggingEmbed import HuggingEmbed
from core.chunking.fixsize_chunks import ProcessData
from core.llm.gemini_llm import LLM

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv("Gemini_api_key")

DOCUMENT_DIR = "data"
VECTOR_DB_PATH = "vectordb"

# Tạo thư mục data nếu chưa tồn tại
os.makedirs(DOCUMENT_DIR, exist_ok=True)


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


vector_Hugging = HuggingEmbed()
processor = ProcessData()


def load_documents_from_dir(directory: str) -> List[Document]:
    all_documents = []
    if not os.path.exists(directory):
        logger.warning(f"Directory {directory} does not exist. Please create it and add your documents.")
        return all_documents

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        logger.info(f"Loading file: {filename}")

        loader = None
        if filename.lower().endswith(".csv"):
            loader = CSVLoader(file_path)
        elif filename.lower().endswith((".xlsx", ".xls")):
            loader = UnstructuredExcelLoader(file_path, mode="elements")
        elif filename.lower().endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif filename.lower().endswith(".txt"):
            loader = TextLoader(file_path)
        elif filename.lower().endswith((".docx", ".doc")):
            loader = Docx2txtLoader(file_path)
        else:
            logger.info(f"Skipping unsupported file type: {filename}")
            continue

        try:
            all_documents.extend(loader.load())
        except Exception as e:
            logger.error(f"Error loading {filename}: {e}")
    return all_documents


def retrain_vector_store_full():
    logger.info("Starting FULL vector store retraining process...")

    all_documents = load_documents_from_dir(DOCUMENT_DIR)

    if not all_documents:
        logger.warning("No documents found to train the vector store. Skipping retraining.")
        vector_Hugging.vector_db = None
        if os.path.exists(VECTOR_DB_PATH):
            shutil.rmtree(VECTOR_DB_PATH)
        return

    chunks = processor.split_text(all_documents)
    logger.info(f"Total chunks created: {len(chunks)}")

    if not chunks:
        logger.warning("No chunks created from documents. Skipping vector store creation.")
        vector_Hugging.vector_db = None
        if os.path.exists(VECTOR_DB_PATH):
            shutil.rmtree(VECTOR_DB_PATH)
        return

    if os.path.exists(VECTOR_DB_PATH):
        logger.info(f"Deleting old vector store at {VECTOR_DB_PATH}...")
        try:
            shutil.rmtree(VECTOR_DB_PATH)
        except OSError as e:
            logger.error(f"Error deleting old vector store {e.filename}: {e.strerror}.")

    new_vector_store = vector_Hugging.create_vector_store(chunks)
    logger.info("New vector store created")
    vector_Hugging.save_vector_store(VECTOR_DB_PATH)
    logger.info("New vector store saved successfully")

    return new_vector_store



# --- LOGIC KHỞI TẠO VÀ RAG CHAIN ---

# Khởi tạo vector store khi ứng dụng khởi động
try:
    vector_Hugging.load_vector_store(VECTOR_DB_PATH)
    logger.info("Vector store loaded successfully on startup.")
except RuntimeError as e: # Bắt lỗi cụ thể của FAISS nếu tệp không tồn tại
    if "could not open" in str(e):
        logger.info("Vector store index.faiss not found on startup. Checking for documents...")
        retrain_vector_store_full() # <--- HÀM NÀY SẼ TẠO DB MỚI
    else:
        raise
except Exception as e:
    logger.error(f"An unexpected error occurred during vector store loading: {e}")
    retrain_vector_store_full()


def retrivel(state: State) -> State:
    if vector_Hugging.vector_db is None:
        logger.warning("Vector store is not initialized. Cannot perform retrieval.")
        return {**state, "context": []}
    similarity_search = vector_Hugging.vector_db.similarity_search(query=state['question'], k=5)
    return {**state, "context": similarity_search}


def generate(state: State):
    llm = LLM(api_key=api_key)
    context_text = "\n".join([doc.page_content for doc in state['context']])

    student_keywords = ["sinh viên", "mã số", "điểm", "kết quả học tập", "học sinh", "thời khóa biểu", "khóa", "lớp",
                        "đồ án"]
    admission_keywords = ["tuyển sinh", "ngành", "chuyên ngành", "đăng ký", "học phí", "thời gian", "điều kiện",
                          "đào tạo", "chỉ tiêu"]

    question_lower = state['question'].lower()
    is_student_query = any(keyword in question_lower for keyword in student_keywords)
    is_admission_query = any(keyword in question_lower for keyword in admission_keywords)

    if is_student_query and not is_admission_query:
        prompt = (
            f"Bạn là trợ lý thông tin sinh viên của Trường Đại học Kỹ thuật Công nghiệp, Thái Nguyên. "
            f"Ưu tiên trả lời câu hỏi dựa trên các thông tin từ bảng hoặc file Excel nếu có. "
            f"Dựa trên các thông tin sau, hãy trả lời câu hỏi của người dùng một cách chính xác và ngắn gọn. "
            f"Nếu thông tin không liên quan hoặc không đủ để trả lời, hãy nói 'Tôi không tìm thấy thông tin phù hợp về sinh viên này'.\n"
            f"Nội dung được cung cấp:\n{context_text}\n"
            f"Câu hỏi của sinh viên: {state['question']}")
    elif is_admission_query and not is_student_query:
        prompt = (
            f"Bạn là trợ lý tư vấn tuyển sinh của Trường Đại học Kỹ thuật Công nghiệp, Thái Nguyên. "
            f"Dựa trên nội dung sau, hãy trả lời câu hỏi của người dùng một cách đầy đủ và chính xác. "
            f"Nếu không có thông tin phù hợp, hãy nói 'Tôi không tìm thấy thông tin phù hợp về tuyển sinh'.\n"
            f"Nội dung được cung cấp:\n{context_text}\n"
            f"Câu hỏi về tuyển sinh: {state['question']}")
    else:
        prompt = (
            f"Bạn là trợ lý của Trường Đại học Kỹ thuật Công nghiệp, Thái Nguyên. "
            f"Dựa trên nội dung sau, hãy trả lời câu hỏi của người dùng một cách chính xác và đầy đủ. "
            f"Nếu không tìm thấy thông tin liên quan trong nội dung đã cung cấp, hãy nói 'Tôi không tìm thấy thông tin phù hợp với câu hỏi của bạn'.\n"
            f"Nội dung được cung cấp:\n{context_text}\n"
            f"Câu hỏi: {state['question']}")

    logger.info("Generated prompt:", prompt)
    answer = llm.post_request(prompt)
    return {**state, "answer": answer}


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QuestionRequest) -> Dict[str, Any]:
    if not request.question:
        raise HTTPException(status_code=400, detail="Question is required")

    logger.info(f"Received question: {request.question}")
    state = {"question": request.question, "context": [], "answer": ""}
    state = retrivel(state)
    final_state = generate(state)
    logger.info(f"Generated answer: {final_state['answer']}")
    return final_state


@app.post("/retrain")
async def retrain_model_full():
    try:
        retrain_vector_store_full()
        vector_Hugging.load_vector_store(VECTOR_DB_PATH)
        return {"message": "Model retrained successfully. Vector store has been updated."}
    except Exception as e:
        logger.error(f"Failed to retrain model: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrain model: {str(e)}")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    file_location = os.path.join(DOCUMENT_DIR, file.filename)
    try:
        # Lưu file mới
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"File '{file.filename}' uploaded successfully to {DOCUMENT_DIR}.")

        # Load và chia nhỏ file mới
        documents = load_documents_from_dir(DOCUMENT_DIR)
        new_chunks = processor.split_text(documents)

        # Cập nhật vector store với các chunks mới
        vector_Hugging.add_documents_to_store(new_chunks, VECTOR_DB_PATH)

        return {"message": f"File '{file.filename}' uploaded and system updated successfully."}
    except Exception as e:
        logger.error(f"Error uploading file {file.filename}: {e}")
        raise HTTPException(status_code=500, detail=f"Could not upload file: {str(e)}")