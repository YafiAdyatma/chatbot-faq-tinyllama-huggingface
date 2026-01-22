# Chatbot FAQ Internal - TinyLlama 1.1B

**PT Teknologi Maju Bersama - FAQ Assistant**

## ✅ Project Overview

- ✅ **Judul**: Chatbot FAQ Internal Perusahaan Menggunakan TinyLlama 1.1B
- ✅ **Task**: Conversational AI / Question Answering
- ✅ **Model**: TinyLlama-1.1B-Chat-v1.0
- ✅ **Dataset**: 12+ FAQ Internal Perusahaan (Custom)
- ✅ **Output**: Natural language responses (LLM-generated)

---

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone <repository-url>
cd chatbot

# 2. Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run server (first run akan download ~1.1GB)
python app.py

# 5. Open browser
http://localhost:5000
```

---

## ⚠️ System Requirements

**Minimum:**

- Python: 3.8+
- RAM: 4GB (TinyLlama 1.1B)
- Storage: 5GB free space
- Internet: Download ~1.1GB (first run)

**Recommended:**

- RAM: 8GB+
- CPU: 4 cores+
- GPU: Optional (akan lebih cepat)

**Note:** Tidak perlu HuggingFace token untuk TinyLlama!

---

## 🎯 Features

✅ **TinyLlama 1.1B** - Efficient LLM dengan 1.1B parameters  
✅ **Intelligent FAQ matching** - Keyword-based context retrieval  
✅ **Natural language generation** - LLM-generated responses  
✅ **Modern UI/UX** - Clean, responsive interface  
✅ **Real-time chat** - Instant responses  
✅ **Multi-topic support** - Jam kerja, cuti, gaji, benefit, IT support, dll

---

## 📊 Architecture

```
User Question
    ↓
Keyword Matching (FAQ Detection)
    ↓
Context Building (Relevant FAQs)
    ↓
Prompt Engineering
    ↓
TinyLlama 1.1B Generation
    ↓
Post-processing & Cleanup
    ↓
Natural Language Response
```

---

## 🔧 Tech Stack

**Backend:**

- Flask 3.0.0 - Web framework
- PyTorch 2.6.0 - Deep learning
- Transformers 4.46.0 - HuggingFace
- TinyLlama-1.1B-Chat-v1.0 - LLM model

**Frontend:**

- HTML5 + CSS3
- Vanilla JavaScript
- Inter Font (Google Fonts)
- Responsive design

**Data:**

- faq_data.json - 12+ FAQ categories

---

## 💡 How It Works

1. **User asks question** - Via web interface
2. **Keyword matching** - Find relevant FAQs based on keywords
3. **Context building** - Build prompt with relevant FAQ data
4. **LLM generation** - TinyLlama generates natural response
5. **Response delivery** - Clean, formatted answer returned

## 📸 Screenshots

- Modern chat interface with gradient design
- Quick action cards for common questions
- Real-time typing indicator
- Mobile responsive layout

## 🤖 Model Info

- **Model**: TinyLlama-1.1B-Chat-v1.0
- **Type**: Causal Language Model (Chat-tuned)
- **Parameters**: 1.1 Billion
- **Size**: ~1.1GB
- **Source**: HuggingFace (TinyLlama)
- **License**: Apache 2.0

## 📝 FAQ Categories

1. ⏰ Jam Kerja
2. 🏖️ Cuti & Leave
3. 💰 Gaji & Payroll
4. 🎁 Benefit Karyawan
5. 💻 IT Support
6. 🚗 Parkir
7. 📚 Training & Development
8. 🏠 Work From Home

## 🔮 Future Improvements

- [ ] Add conversation history
- [ ] Implement user feedback system
- [ ] Add more FAQ categories
- [ ] GPU acceleration support
- [ ] Multi-language support
- [ ] Export chat history

## 📄 License

MIT License

## 👨‍💻 Author

**Your Name**  
PT Teknologi Maju Bersama
