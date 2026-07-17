# AI_Code_Reviewer_Groq

An intelligent **AI-powered Code Reviewer** that analyzes source code, detects potential issues, suggests improvements, and provides best practices using the **Groq API** and Large Language Models (LLMs).

This project helps developers improve code quality by automating code reviews and generating meaningful feedback in seconds.

---

## 🚀 Features

* ✅ Review code using AI-powered analysis
* ✅ Detect syntax errors and potential bugs
* ✅ Suggest code optimizations and improvements
* ✅ Identify security vulnerabilities and bad practices
* ✅ Provide explanations for suggested changes
* ✅ Support for multiple programming languages
* ✅ Fast responses powered by **Groq LLMs**
* ✅ User-friendly interface with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Groq API**
* **LLMs (Llama Models)**
* **HTML/CSS (for UI customization)**

---

## 📂 Project Structure

```text
AI_Code_Reviewer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
├── utils/
│   └── reviewer.py        # Code review logic
├── assets/
│   └── screenshots/       # Application screenshots
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Code_Reviewer.git
cd AI_Code_Reviewer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

#### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Get Your Groq API Key

1. Create an account on Groq.
2. Generate an API key from the dashboard.
3. Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## 💻 How It Works

1. Paste or upload your source code.
2. Select the programming language (optional).
3. Click **Review Code**.
4. The AI analyzes the code and provides:

   * Bugs and issues
   * Code quality improvements
   * Security recommendations
   * Performance optimizations
   * Best practices

---

## 📸 Application Workflow

```text
Input Code → Send to Groq API → AI Analysis → Review Report → Suggestions
```

---

## Example Review

### Input

```python
def divide(a, b):
    return a / b
```

### AI Suggestions

* Add exception handling for division by zero.
* Include function documentation.
* Validate input parameters.

Improved Code:

```python
def divide(a, b):
    """
    Divides two numbers safely.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
```

---

## 📦 Requirements

```text
streamlit
groq
python-dotenv
```

Install manually:

```bash
pip install streamlit groq python-dotenv
```

---

## 🎯 Future Enhancements

* Support file uploads (.py, .java, .cpp, .js)
* Download review reports as PDF
* Code complexity analysis
* GitHub repository integration
* Multi-file project reviews
* AI-generated unit tests

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---
