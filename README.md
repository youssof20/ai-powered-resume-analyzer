# AI-Powered Resume Analyzer 🚀

An AI-driven resume analysis tool that evaluates resumes based on industry-specific AI job requirements. It uses **spaCy** for natural language processing (NLP) and **Transformers (BERT)** for enhanced analysis. The tool provides feedback on the suitability of a resume for AI-related jobs, highlighting key skills, experience, and more.

### Features:
- 📄 **Resume Parsing**: Extracts skills, experience, education, and other relevant information.
- 🤖 **AI Job Matching**: Analyzes resume content based on AI job descriptions using pre-trained BERT models.
- 🔍 **Feedback**: Provides valuable feedback to improve resume relevance for AI-related roles.
- 🌐 **Streamlit UI**: Simple and interactive web UI to upload and analyze resumes.

---

## Tech Stack 🛠️

- **Python 3.8+**
- **spaCy** (NLP)
- **Transformers (BERT)** (Text classification)
- **Flask** (Backend API)
- **Streamlit** (Frontend UI)

---

## Prerequisites 📦

Before you get started, make sure you have the following installed:

- **Anaconda** (or Miniconda)
  - [Download Anaconda](https://www.anaconda.com/products/individual) for managing environments and dependencies.
- **Python 3.8+**
- **Git** (for version control)

---

## Getting Started 🚀

### 1. Clone the Repository or Download the Project 🔽

Clone the repository or download the files to your local machine:

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

### 2. Create a Conda Environment 🧑‍💻

Create a new environment to manage dependencies:

```bash
conda create -n resume-analyzer python=3.8
conda activate resume-analyzer
```

### 3. Install Required Dependencies 📥

Install all required libraries using `conda` and `pip`:

```bash
conda install -c conda-forge spacy
conda install -c conda-forge transformers
pip install flask streamlit
```

Download the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

### 4. Set Up the Project Files 📂

Ensure your project structure looks like this:

```
resume-analyzer/
│
├── app.py                # Flask app backend
├── resume_analyzer.py    # Resume analysis logic (NLP & matching)
├── requirements.txt      # Project dependencies
├── ui.py                 # Streamlit UI
└── README.md             # This file!
```

---

## Running the Project 💻

### 1. Start the Flask Backend 🏃‍♂️

In one terminal window, run the Flask backend:

```bash
python app.py
```

The Flask API will be running at `http://127.0.0.1:5000/`.

### 2. Start the Streamlit UI 🌐

In another terminal window, run the Streamlit frontend:

```bash
streamlit run ui.py
```

This will launch the interactive UI at `http://localhost:8501/` where you can upload resumes for analysis.

---

## How to Use 📝

1. **Open the Streamlit UI** by navigating to `http://localhost:8501/` in your browser.
2. **Upload your resume** (in .txt, .pdf, or .docx format).
3. **Click "Analyze"** to see the AI job-matching results, including:
   - Extracted skills and experience.
   - Evaluation based on AI job descriptions.
   - Suggestions for resume improvement.

---

## Contributing 🤝

Feel free to contribute by:
- 🐛 **Reporting bugs** or issues.
- 🧑‍💻 **Submitting pull requests** to improve features or fix bugs.
- ✍️ **Suggesting improvements** to the project.

### Steps to contribute:
1. Fork the repo.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -m "Added feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

---

## Deployment 🌍

If you want to deploy this project, you can use platforms like [Heroku](https://www.heroku.com/) or [Render](https://render.com/) for hosting the app.

### Deployment Steps (for Heroku):

1. Create a **Procfile**:

   ```txt
   web: python app.py
   ```

2. Login to Heroku:

   ```bash
   heroku login
   ```

3. Push the app to Heroku:

   ```bash
   git push heroku master
   ```

4. Open the app in your browser:

   ```bash
   heroku open
   ```

---

## License 📜

This project is licensed under the MIT License

---

## Acknowledgements 🙏

- **spaCy** for NLP and resume parsing.
- **Transformers (BERT)** for enhanced text analysis.
- **Streamlit** for creating the web interface.
- **Flask** for handling backend requests.
- And everyone who contributed to open-source projects!

---

## Common Issues⚠️

If you encounter any issues during setup, try the following:

1. **Ensure your environment is activated**: `conda activate resume-analyzer`.
2. **Check if spaCy model is installed**: `python -m spacy download en_core_web_sm`.
3. **Ensure all dependencies are installed**: Run `conda list` to confirm the installation of required libraries.

If problems persist, feel free to open an issue or reach out for help! 😊

---

### Thanks for using the AI-Powered Resume Analyzer! ✨

Good luck improving those resumes and landing your dream job! 👩‍💻👨‍💻🚀
