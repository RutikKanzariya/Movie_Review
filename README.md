# 🎬 CineSage – AI Movie Information Extractor

CineSage is a Generative AI application that extracts structured movie information from natural language descriptions using the **Mistral AI API**. The project demonstrates modern GenAI concepts such as reusable prompt templates, structured JSON outputs, Pydantic validation, and clean Python project architecture.

---

## 🚀 Features

- 🎥 Extract movie information from plain text
- 🤖 Powered by the Mistral AI API
- 📝 Reusable Prompt Templates
- 📦 Structured JSON Output
- ✅ Pydantic Data Validation
- 🔒 Environment Variable Support using `.env`
- 🏗️ Clean and Modular Project Structure
- 📚 Beginner-Friendly GenAI Project

---

## 🛠️ Tech Stack

- Python 3.11+
- Mistral AI API
- LangChain (Prompt Templates)
- Pydantic
- python-dotenv
- UV (Package Manager)

---

## 📂 Project Structure

```text
cinesage/
│
├── .venv/
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
├── README.md
├── app.py
│
├── prompts/
│   └── movie_prompt.py
│
├── models/
│   └── movie_schema.py
│
├── services/
│   └── mistral_service.py
│
├── utils/
│   └── parser.py
│
└── data/
```

---

## 📥 Installation

### Clone the Repository

```bash
git clone https://github.com/RutikKanzariya/Movie_Review.git
```

```bash
cd cinesage
```

---

### Create Virtual Environment

```bash
uv venv
```

Activate the environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
uv sync
```

or

```bash
uv add mistralai langchain pydantic python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```

> Never upload your `.env` file to GitHub.

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💡 Example Input

```text
Interstellar is a 2014 science fiction film directed by Christopher Nolan.

It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain and Michael Caine.

The story follows astronauts searching for a new home for humanity after Earth becomes uninhabitable.
```

---

## 📤 Example Output

```json
{
  "title": "Interstellar",
  "year": 2014,
  "genre": "Science Fiction",
  "director": "Christopher Nolan",
  "cast": [
    "Matthew McConaughey",
    "Anne Hathaway",
    "Jessica Chastain",
    "Michael Caine"
  ],
  "summary": "A team of astronauts travels through a wormhole to find a new home for humanity."
}
```

---

## 🧠 GenAI Concepts Demonstrated

- Prompt Engineering
- Prompt Templates
- Structured Output Generation
- JSON Parsing
- Pydantic Validation
- Environment Variables
- API Integration
- Modular Project Architecture

---

## 🔮 Future Improvements

- FastAPI Backend
- Streamlit Web Interface
- SQLite/PostgreSQL Database
- Movie Recommendation System
- LangChain Output Parsers
- Docker Support
- Deployment on Render/Railway
- RAG-based Movie Knowledge Assistant

---

## 📸 Screenshots



---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rutik Kanzariya**

- GitHub: https://github.com/RutikKanzariya
- LinkedIn: https://www.linkedin.com/in/rutik-kanzariya-81a7a82bb/

---

⭐ If you found this project helpful, consider giving it a Star on GitHub!