<h1 align="center">📄 Resume Application Tracking System (ATS) Using Google Gemini</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit"/>
  <img src="https://img.shields.io/badge/Google_Gemini-API-orange?style=flat-square"/>
</p>

---

<h2>📘 Project Overview</h2>

<p>
This project is a **Resume Application Tracking System (ATS)** powered by <strong>Google Gemini LLM</strong>.  
It allows HR professionals and recruiters to upload resumes (PDF) and analyze them against a job description.  
The system evaluates alignment, highlights strengths & weaknesses, calculates ATS compatibility, and provides a match percentage.  
Streamlit provides a responsive interface, while Gemini LLM processes the PDF content intelligently.
</p>

---

<h2>🎯 Key Features</h2>

<ul>
  <li>📄 Upload resumes in PDF format</li>
  <li>⚡ AI-powered evaluation of resume against job description</li>
  <li>📊 Percentage match with job requirements and ATS compatibility</li>
  <li>🧠 Highlights strengths, weaknesses, missing keywords, and final thoughts</li>
  <li>🎨 Interactive Streamlit interface with clear outputs</li>
  <li>🔒 Secure API key management using <code>.env</code></li>
</ul>

---

<h2>🧩 Tech Stack</h2>

<table>
<tr>
  <td><strong>Language</strong></td>
  <td>Python 🐍</td>
</tr>
<tr>
  <td><strong>Frontend</strong></td>
  <td>Streamlit</td>
</tr>
<tr>
  <td><strong>AI Model</strong></td>
  <td>Google Gemini LLM (gemini-2.5-flash)</td>
</tr>
<tr>
  <td><strong>Environment</strong></td>
  <td>.env for API key management</td>
</tr>
<tr>
  <td><strong>PDF Processing</strong></td>
  <td>pdf2image, Pillow (PIL), Poppler for PDF-to-image conversion</td>
</tr>
</table>

---

<h2>🧠 Skills Demonstrated</h2>

<ul>
  <li>Integrating Google Gemini API for resume evaluation</li>
  <li>Processing PDF resumes and converting pages to images for AI analysis</li>
  <li>Building interactive web apps with Streamlit</li>
  <li>Generating structured outputs: ATS match percentage, qualifications, keyword analysis</li>
  <li>Secure handling of API keys and environment variables</li>
</ul>

---

---

<h2 align="center">🖥️ Application Interface</h2>

<p align="center">
  <img src="https://github.com/BIKRANT-RAWAT/GenAI_Project_Using_Google_Gemini/blob/master/Resume%20Application%20Tracking%20System(ATS)%20Using%20Google%20Gemini/images/interface.png" alt="App Interface" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="https://github.com/BIKRANT-RAWAT/GenAI_Project_Using_Google_Gemini/blob/master/Resume%20Application%20Tracking%20System(ATS)%20Using%20Google%20Gemini/images/response.png" alt="Prediction Page" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
</p>

---

<h2>🚀 How to Run the Project</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/Resume-ATS-Gemini.git</code></pre>
  </li>
  <li>Create a virtual environment and activate it:
    <pre><code>python -m venv venv
venv\\Scripts\\activate</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Create a <code>.env</code> file and store your Google API key:
    <pre><code>GOOGLE_API_KEY=your_api_key_here</code></pre>
  </li>
  <li>Install Poppler for PDF-to-image conversion:
    <pre><code>Download from https://github.com/oschwartz10612/poppler-windows/releases/ and set poppler_path</code></pre>
  </li>
  <li>Run the Streamlit app:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

---

<h2>📂 Folder Structure</h2>

<pre>
📁 Resume-ATS-Gemini
│
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── .env                     # Environment file storing API key
└── README.md               # Project documentation
</pre>

---

<h2>🤝 Collaboration</h2>

<p>
Contributions are welcome! Potential enhancements include:
<ul>
  <li>📊 Automatic parsing and structured data extraction from resumes</li>
  <li>🗂️ Multi-page PDF support and batch resume processing</li>
  <li>🌐 Deploy on cloud platforms for enterprise usage</li>
  <li>🔐 User authentication and secure access</li>
</ul>
</p>

<p align="center">
  <a href="https://github.com/yourusername/Resume-ATS-Gemini/fork">
    <img src="https://img.shields.io/badge/Fork-Repository-blue?style=for-the-badge&logo=github"/>
  </a>
</p>

---

<h2>💡 Future Enhancements</h2>

<ul>
  <li>🧾 Extract structured fields automatically: name, skills, experience, education</li>
  <li>📈 Visualization of applicant match metrics</li>
  <li>🌐 Deploy web app for HR teams</li>
  <li>🤖 Integrate multi-language resume evaluation</li>
</ul>

---

<h2>🙏 Acknowledgements</h2>

<ul>
  <li>❤️ <strong>Krish Naik Sir</strong> for mentoring and guiding such beautiful project</li>
  <li>🧠 Google Gemini LLM — for intelligent AI-based resume evaluation</li>
  <li>🚀 Streamlit — for building interactive web applications</li>
  <li>🖼️ pdf2image, Pillow (PIL) — for PDF processing and image conversion</li>
  <li>💡 Open-source community — for guidance on AI & Streamlit integration</li>
</ul>

---

<h3 align="center">⭐ If you find this project helpful, give it a star on GitHub! ⭐</h3>
<p align="center">Made with ❤️ using Streamlit & Google Gemini AI</p>
