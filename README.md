# Mergington High School Activities API

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

A FastAPI-based web application for managing high school extracurricular activities. Students can view available activities and sign up for them through a simple web interface.

## 🚀 Features

- **View Activities**: Browse all available extracurricular activities
- **Activity Details**: See descriptions, schedules, and availability
- **Student Signup**: Sign up for activities with email validation
- **Real-time Updates**: See current enrollment and spots available
- **Responsive UI**: Modern, mobile-friendly interface

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Server**: Uvicorn ASGI server
- **Testing**: Pytest
- **Code Quality**: Black, Flake8, isort

## 📦 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/ssahgalnagarro/skills-getting-started-with-github-copilot.git
cd skills-getting-started-with-github-copilot

# Run the setup script
./setup.sh

# Start the development server
source venv/bin/activate
uvicorn src.app:app --reload
```

### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn src.app:app --reload
```

### Option 3: Using Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build and run manually
docker build -t mergington-api .
docker run -p 8000:8000 mergington-api
```

## 🎯 Usage

Once the server is running, you can:

1. **Access the Web Interface**: http://localhost:8000
2. **View API Documentation**: http://localhost:8000/docs
3. **Alternative API Docs**: http://localhost:8000/redoc

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Redirect to web interface |
| `GET` | `/activities` | Get all activities |
| `POST` | `/activities/{activity_name}/signup?email={email}` | Sign up for activity |

## 🧪 Testing

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=src --cov-report=html
```

## 🔧 Development

### VS Code Setup

This project includes VS Code configuration for an optimal development experience:

1. **Open in VS Code**: `code .`
2. **Install Recommended Extensions**: VS Code will prompt you
3. **Use Built-in Tasks**:
   - `Ctrl+Shift+P` → `Tasks: Run Task`
   - Choose from: Start Server, Run Tests, Format Code, etc.

### Available Commands

```bash
# Using Make (recommended)
make help          # Show all available commands
make setup         # Setup virtual environment
make install       # Install dependencies
make run           # Start development server
make test          # Run tests
make format        # Format code
make lint          # Lint code

# Using VS Code Tasks
# Press Ctrl+Shift+P and type "Tasks: Run Task"
```

### Code Quality

The project uses several tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **isort**: Import sorting
- **Pytest**: Testing

## 🏗️ Project Structure

```
skills-getting-started-with-github-copilot/
├── .vscode/                 # VS Code configuration
│   ├── launch.json         # Debug configuration
│   ├── settings.json       # Workspace settings
│   └── tasks.json          # Build tasks
├── src/                    # Application source code
│   ├── app.py             # Main FastAPI application
│   ├── static/            # Static web files
│   │   ├── index.html     # Main web interface
│   │   ├── app.js         # Frontend JavaScript
│   │   └── styles.css     # CSS styles
│   └── README.md          # Technical documentation
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_app.py        # API tests
├── requirements.txt        # Python dependencies
├── requirements-dev.txt    # Development dependencies
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Docker Compose setup
├── Makefile              # Build automation
├── setup.sh              # Setup script
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🌟 Activities Available

The system comes with three pre-configured activities:

1. **Chess Club** - Strategy and tournaments (Fridays 3:30-5:00 PM)
2. **Programming Class** - Software development basics (Tuesdays & Thursdays 3:30-4:30 PM)
3. **Gym Class** - Physical education and sports (Mon/Wed/Fri 2:00-3:00 PM)

## 🔄 Future Enhancements

- [ ] User authentication and authorization
- [ ] Database integration (PostgreSQL)
- [ ] Email notifications for signups
- [ ] Activity capacity management
- [ ] Admin dashboard for activity management
- [ ] Student profiles and history
- [ ] Calendar integration
- [ ] Mobile app

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Styled with modern CSS3
- Tested with [Pytest](https://pytest.org/)
- Developed as part of the GitHub Copilot skills exercise

---

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/ssahgalnagarro/skills-getting-started-with-github-copilot/issues/1)

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

