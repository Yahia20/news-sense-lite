# 🧭 NewsSense Lite

**NewsSense Lite** is a lightweight, open-source Streamlit app that reads online news articles and lets you ask AI-powered questions about them — fast, clean, and privacy-friendly.

---

## ✨ Features
- Add up to **3 article URLs** at once  
- Automatically **extracts, cleans, and processes** article text  
- Creates **semantic embeddings** using FAISS for retrieval  
- Answers your questions using **Hugging Face’s `flan-t5-base`** model  
- Simple, elegant interface built with **Streamlit**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Yahia20/news-sense-lite.git
cd news-sense-lite
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables
Create a `.env` file in the project root (copy from `.env.example`) and add your tokens:

```bash
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
NGROK_AUTHTOKEN=your_ngrok_token
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

Once it starts, open the URL shown in your terminal:

- **Local URL:** `http://localhost:8501`  
- **Public URL:** `https://<random>.ngrok-free.dev`

---

## 🧩 Example Usage
1. Paste up to 3 article URLs in the sidebar.  
2. Click **"🚀 Process Articles"** to load and index them.  
3. Type a question such as:  
   ```
   What are the main findings of these articles?
   ```
4. The app will generate an AI-based summary and list the sources it used.

---

## ⚙️ Technologies Used
- 🐍 Python 3.10+  
- 🎨 Streamlit — interactive web UI  
- 🧠 LangChain — LLM orchestration  
- 🤗 Hugging Face Transformers — model hosting  
- 🗂 FAISS — vector similarity search  
- 🌐 Ngrok — secure public tunnel  
- 📄 Unstructured — article text extraction  

---

## 🧠 Default Model
By default, the app uses:
```
google/flan-t5-base
```
You can change this in `.env` by setting:
```
NEWS_MODEL_NAME=your_custom_model_name
```

---

## 🪪 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

## 💬 About
Made with ❤️ using Streamlit and LangChain.  
Built for learning, research, and fun exploration of AI-driven news understanding.
