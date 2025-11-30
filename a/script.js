// Cần có file này trong thư mục static/

// ĐÃ SỬA LỖI: Trỏ đúng tới endpoint /ask
const API_URL = 'http://127.0.0.1:8000/ask';
const chatBox = document.getElementById('chat-box');
const questionInput = document.getElementById('question-input');

function createMessageElement(content, type) {
    const messageDiv = document.createElement('div');

    // FIX: Sử dụng spread operator (...) để thêm nhiều class (khắc phục InvalidCharacterError)
    const classes = type.split(' ');
    messageDiv.classList.add(...classes);

    messageDiv.innerHTML = content;
    return messageDiv;
}

function showLoading() {
    // Gọi với chuỗi classes có khoảng trắng: "ai-message loading"
    const loadingDiv = createMessageElement('<span>... Đang tìm kiếm và tạo câu trả lời...</span>', 'ai-message loading');
    loadingDiv.id = 'loading-indicator';
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function hideLoading() {
    const loadingDiv = document.getElementById('loading-indicator');
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

async function askQuestion() {
    const question = questionInput.value.trim();
    if (question === "") return;

    chatBox.appendChild(createMessageElement(question, 'user-message'));
    questionInput.value = '';
    questionInput.disabled = true;

    showLoading();
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question }),
        });

        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const data = await response.json();
        const answer = data.answer;

        const aiMessage = createMessageElement(answer, 'ai-message');
        hideLoading();
        chatBox.appendChild(aiMessage);

    } catch (error) {
        console.error('Lỗi khi gọi API:', error);
        hideLoading();
        const errorMessage = createMessageElement(`❌ **Lỗi kết nối:** Không thể xử lý yêu cầu. Chi tiết: ${error.message}`, 'ai-message error');
        errorMessage.style.color = '#800020';
        chatBox.appendChild(errorMessage);
    } finally {
        questionInput.disabled = false;
        questionInput.focus();
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}