from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import json

app = Flask(__name__)
CORS(app)

model = None
tokenizer = None
text_generator = None
faq_data = None

def load_faq_data():
    try:
        with open('faq_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading FAQ: {e}")
        return {"faqs": []}

def initialize_model():
    global model, tokenizer, text_generator, faq_data
    
    print("\n" + "="*70)
    print("🤖 LOADING MODEL")
    print("="*70)
    
    faq_data = load_faq_data()
    print(f"✅ Loaded {len(faq_data.get('faqs', []))} FAQ categories")
    
    try:
        model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        print(f"\n📥 Loading {model_name}...")
        print("First run will download ~1.1GB")
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            resume_download=True,
            force_download=False
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            low_cpu_mem_usage=True,
            torch_dtype=torch.float32,
            resume_download=True,
            force_download=False
        )
        
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            model.config.pad_token_id = model.config.eos_token_id
        
        text_generator = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=150,
            do_sample=False,
            repetition_penalty=1.1
        )
        
        print("✅ TinyLlama loaded!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nCoba:")
        print("1. Cek koneksi internet")
        print("2. Pake mirror: set HF_ENDPOINT=https://hf-mirror.com")
        print("3. Download manual dari huggingface.co")
        return False

def build_faq_context():
    context = ""
    for faq in faq_data.get('faqs', []):
        context += f"Q: {faq['question']}\nA: {faq['answer']}\n\n"
    return context

def generate_response(question):
    if text_generator is None:
        return "Model belum ter-load."
    
    try:
        q_lower = question.lower().strip()
        
        # Handle greetings and small talk
        greetings = ['halo', 'hai', 'hi', 'hello', 'hey', 'test', 'tes', 'ping']
        if q_lower in greetings or len(q_lower) < 3:
            return "Halo! Ada yang bisa saya bantu? Silakan tanya tentang jam kerja, cuti, gaji, benefit, IT support, parkir, atau training."
        
        # Simple keyword matching for relevant FAQs
        relevant_faqs = []
        for faq in faq_data.get('faqs', []):
            if any(kw in q_lower for kw in faq.get('keywords', [])):
                relevant_faqs.append(faq)
                if len(relevant_faqs) >= 2:  # Max 2 FAQs
                    break
        
        # If no keyword match, return helpful message
        if not relevant_faqs:
            return "Maaf, saya tidak menemukan informasi yang sesuai. Coba tanyakan tentang: jam kerja, cuti, gaji, benefit, IT support, parkir, atau training."
        
        # Build context
        faq_context = ""
        if relevant_faqs:
            for faq in relevant_faqs:
                faq_context += f"Pertanyaan: {faq['question']}\nJawaban: {faq['answer']}\n\n"
        
        # Simpler prompt format without special tokens
        prompt = f"""Kamu adalah asisten FAQ perusahaan. Jawab pertanyaan berikut berdasarkan informasi FAQ.

{faq_context}
Pertanyaan: {question}
Jawaban:"""
        
        print(f"🤖 LLM Generating: '{question}'")
        print(f"📝 Prompt length: {len(prompt)} chars")
        
        response = text_generator(
            prompt,
            pad_token_id=tokenizer.pad_token_id,
            max_new_tokens=100,
            return_full_text=False  # Only return generated text
        )
        
        answer = response[0]['generated_text'].strip()
        
        # Clean up response
        if "Pertanyaan:" in answer:
            answer = answer.split("Pertanyaan:")[0].strip()
        
        # Take first complete sentence or paragraph
        if "\n\n" in answer:
            answer = answer.split("\n\n")[0].strip()
        
        # Limit length
        if len(answer) > 200:
            sentences = answer.split(". ")
            answer = sentences[0] + "." if sentences else answer[:200]
        
        print(f"✅ Done: {answer[:80]}...")
        return answer if answer else "Maaf, informasi tidak ditemukan."
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return "Maaf, terjadi error."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        question = data.get('message', '').strip()
        
        if not question:
            return jsonify({'error': 'Message required'}), 400
        
        response = generate_response(question)
        
        return jsonify({
            'response': response,
            'status': 'success',
            'model': 'TinyLlama-1.1B-Chat'
        })
        
    except Exception as e:
        print(f"❌ API error: {e}")
        return jsonify({'error': str(e), 'status': 'error'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'model': 'TinyLlama-1.1B-Chat',
        'model_loaded': text_generator is not None
    })

if __name__ == '__main__':
    print("="*70)
    print("🤖 CHATBOT FAQ - TinyLlama 1.1B Chat")
    print("="*70)
    
    success = initialize_model()
    
    if not success:
        print("⚠️  Model failed to load!")
    
    print("\n🌐 Server: http://localhost:5000")
    print("="*70 + "\n")
    
    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)
