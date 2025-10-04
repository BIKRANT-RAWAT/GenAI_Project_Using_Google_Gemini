<h1 align="center">🥗 Gemini Health Management App</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit"/>
  <img src="https://img.shields.io/badge/Google_Gemini-API-orange?style=flat-square"/>
</p>

---

<h2>📘 Project Overview</h2>

<p>
The **Gemini Health Management App** is an AI-powered application that helps users analyze food items from images and calculate total calorie intake.  
Using the <strong>Google Gemini Pro Vision API</strong>, the app provides detailed nutritional information for each item in the image.  
The app is built with <strong>Streamlit</strong> for a responsive and interactive user experience.
</p>

---

<h2>🎯 Key Features</h2>

<ul>
  <li>🖼️ Upload food images in JPG, JPEG, or PNG formats</li>
  <li>⚡ AI-powered analysis of food items using Gemini LLM</li>
  <li>🥗 Calculates total calories and provides a detailed breakdown for each food item</li>
  <li>🎨 Interactive Streamlit interface with live image preview</li>
  <li>🔒 Secure API key management using <code>.env</code> files</li>
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
  <td><strong>Image Processing</strong></td>
  <td>Pillow (PIL)</td>
</tr>
</table>

---

<h2>🧠 Skills Demonstrated</h2>

<ul>
  <li>Integrating Google Gemini API for image-based nutritional analysis</li>
  <li>Building interactive web apps using Streamlit</li>
  <li>Handling uploaded images and processing for AI analysis</li>
  <li>Generating structured outputs like total calories and item-wise breakdown</li>
  <li>Secure handling of API keys using environment variables</li>
</ul>

---
---

<h2 align="center">🖥️ Application Interface</h2>

<p align="center">
  <img src="https://github.com/BIKRANT-RAWAT/GenAI_Project_Using_Google_Gemini/blob/master/Nutritionist%20Generative%20AI%20Doctor%20Using%20Google%20Gemini/images/interface.png" alt="App Interface" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="https://github.com/BIKRANT-RAWAT/GenAI_Project_Using_Google_Gemini/blob/master/Nutritionist%20Generative%20AI%20Doctor%20Using%20Google%20Gemini/images/input.png" alt="Prediction Page" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="https://github.com/BIKRANT-RAWAT/GenAI_Project_Using_Google_Gemini/blob/master/Nutritionist%20Generative%20AI%20Doctor%20Using%20Google%20Gemini/images/res1.png" alt="Prediction Page" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="https://github.com/BIKRANT-RAWAT/GenAI_Project_Using_Google_Gemini/blob/master/Nutritionist%20Generative%20AI%20Doctor%20Using%20Google%20Gemini/images/res2.png" alt="Prediction Page" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
</p>

---

<h2>🚀 How to Run the Project</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/Gemini-Health-App.git</code></pre>
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
  <li>Run the Streamlit app:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

---

<h2>📂 Folder Structure</h2>

<pre>
📁 Gemini-Health-App
│
├── health.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── .env                     # Environment file storing API key
└── README.md               # Project documentation
</pre>

---

<h2>🤝 Collaboration</h2>

<p>
Contributions are welcome! You can enhance the project by adding features such as:
<ul>
  <li>📊 Automatic recognition of more food items</li>
  <li>🌐 Support for multi-language nutrition labels</li>
  <li>📈 Visualization of daily or weekly calorie intake</li>
  <li>🔐 User authentication for personalized health tracking</li>
</ul>
</p>

<p align="center">
  <a href="https://github.com/yourusername/Gemini-Health-App/fork">
    <img src="https://img.shields.io/badge/Fork-Repository-blue?style=for-the-badge&logo=github"/>
  </a>
</p>

---

<h2>💡 Future Enhancements</h2>

<ul>
  <li>🧾 Detailed nutrient breakdown (protein, carbs, fats)</li>
  <li>🌐 Multi-user support with health tracking dashboard</li>
  <li>📊 Visual analytics of diet over time</li>
  <li>🌱 Recommendations for healthy food choices</li>
</ul>

---

<h2>🙏 Acknowledgements</h2>

<ul>
  <li>❤️ <strong>Krish Naik Sir</strong> for mentoring and guiding such beautiful project</li>
  <li>🧠 Google Gemini LLM — for AI-powered image and nutrition analysis</li>
  <li>🚀 Streamlit — for creating interactive web apps</li>
  <li>🖼️ Pillow (PIL) — for handling uploaded food images</li>
  <li>💡 Open-source community — for guidance on AI & Streamlit integration</li>
</ul>

---

<h3 align="center">⭐ If you find this project helpful, give it a star on GitHub! ⭐</h3>
<p align="center">Made with ❤️ using Streamlit & Google Gemini AI</p>
