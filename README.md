<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NewsSense Lite - README</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 900px; margin: auto; background: #f9f9f9; color: #333; }
    h1, h2, h3 { color: #2c3e50; }
    code, pre { background: #eee; padding: 4px 8px; border-radius: 4px; font-family: monospace; }
    pre { overflow-x: auto; padding: 10px; }
    section { margin-bottom: 30px; }
    hr { border: none; border-top: 1px solid #ddd; margin: 30px 0; }
</style>
</head>
<body>

<h1>🧭 NewsSense Lite</h1>
<p><strong>NewsSense Lite</strong> is a lightweight, open-source Streamlit app that reads online news articles and lets you ask AI-powered questions about them — fast, clean, and privacy-friendly.</p>

<hr>

<section>
<h2>✨ Features</h2>
<ul>
    <li>Add up to <strong>3 article URLs</strong> at once</li>
    <li>Automatically <strong>extracts, cleans, and processes</strong> article text</li>
    <li>Creates <strong>semantic embeddings</strong> using FAISS for retrieval</li>
    <li>Answers your questions using <strong>Hugging Face’s <code>flan-t5-base</code></strong> model</li>
    <li>Simple, elegant interface built with <strong>Streamlit</strong></li>
</ul>
</section>

<hr>

<section>
<h2>🚀 Getting Started</h2>

<h3>1️⃣ Clone the repository</h3>
<pre><code>git clone https://github.com/&lt;your-username&gt;/news-sense-lite.git
cd news-sense-lite</code></pre>

<h3>2️⃣ Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3️⃣ Set up environment variables</h3>
<p>Create a <code>.env</code> file in the project root (copy from <code>.env.example</code>) and add your tokens:</p>
<pre><code>HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
NGROK_AUTHTOKEN=your_ngrok_token</code></pre>

<h3>4️⃣ Run the app</h3>
<pre><code>streamlit run app.py</code></pre>
<p>Once it starts, open the URL shown in your terminal:</p>
<pre><code>Local URL: http://localhost:8501
Public URL: https://&lt;random&gt;.ngrok-free.dev</code></pre>
</section>

<hr>

<section>
<h2>🧩 Example Usage</h2>
<ol>
    <li>Paste up to 3 article URLs in the sidebar.</li>
    <li>Click <strong>"🚀 Process Articles"</strong> to load and index them.</li>
    <li>Type a question such as:</li>
</ol>
<pre><code>What are the main findings of these articles?</code></pre>
<p>The app will generate an AI-based summary and list the sources it used.</p>
</section>

<hr>

<section>
<h2>⚙️ Technologies Used</h2>
<ul>
    <li>🐍 Python 3.10+</li>
    <li>🎨 Streamlit — interactive web UI</li>
    <li>🧠 LangChain — LLM orchestration</li>
    <li>🤗 Hugging Face Transformers — model hosting</li>
    <li>🗂 FAISS — vector similarity search</li>
    <li>🌐 Ngrok — secure public tunnel</li>
    <li>📄 Unstructured — article text extraction</li>
</ul>
</section>

<hr>

<section>
<h2>🧠 Default Model</h2>
<pre><code>google/flan-t5-base</code></pre>
<p>You can change this in <code>.env</code> by setting:</p>
<pre><code>NEWS_MODEL_NAME=your_custom_model_name</code></pre>
</section>

<hr>

<section>
<h2>🪪 License</h2>
<p>This project is licensed under the MIT License — see the LICENSE file for details.</p>
</section>

<hr>

<section>
<h2>💬 About</h2>
<p>Made with ❤️ using Streamlit and LangChain.<br>
Built for learning, research, and fun exploration of AI-driven news understanding.</p>
</section>

</body>
</html>
