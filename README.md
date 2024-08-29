# Social Media Manager Assistant

This project implements a social media manager assistant with LLM capabilities. It generates new posts based on previous posts and given topics, maintaining the voice and style of different user profiles.

## Features

- Generate new social media posts using LLM technology
- Maintain different user profiles with unique posting styles
- Store and retrieve previous posts using SQLite and ChromaDB
- Easy-to-use command-line interface
- Open WebUI integration

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/erniefontes/social-media-manager-assistant.git
   cd social-media-assistant
   ```

2. Install the required dependencies (requires [Poetry](https://python-poetry.org/)):
   ```
   poetry install
   ```

3. Set up your environment variables:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```
   or place in `.env` file.

## Project Structure
```
social_media_assistant/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── llm_handler.py
│   ├── database_handler.py
│   ├── profile_manager.py
│   └── post_generator.py
├── data/
│   ├── sqlite_db.sqlite
│   └── chroma_db/
├── tests/
│   ├── __init__.py
│   ├── test_llm_handler.py
│   ├── test_database_handler.py
│   ├── test_profile_manager.py
│   └── test_post_generator.py
├── requirements.txt
├── CHANGELOG.md
├── MILESTONES.md
├── README.md
└── USAGE.md
```

## Core Components
1. `main.py`: This will be the entry point of the application, orchestrating the other components.
2. `llm_handler.py`: This will handle interactions with the LLM, including sending prompts and processing responses.
3. `database_handler.py`: This will manage interactions with both SQLite and Chroma databases.
4. `profile_manager.py`: This will handle loading and managing different user profiles.
5. `post_generator.py`: This will generate new posts based on previous posts and topics.

## Usage

For detailed usage instructions, please refer to the [USAGE.md](USAGE.md) file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Code Quality
- Follow PEP 8 guidelines for Python.
- Write modular and reusable code.
- Include docstrings for all methods and classes.
- Utilize type hints for better code readability.

### Testing
- Implement unit tests for each module.
- Use pytest for testing.
- Achieve at least 85% code coverage.

### Error Handling
- Implement robust error handling with descriptive error messages.
- Log errors using a logging framework (e.g., loguru).

### Security
- Secure API endpoints with authentication (OAuth2, JWT).
- Sanitize inputs to prevent SQL injection and other common vulnerabilities.

### Performance

Optimize database queries.
Use async operations where possible (e.g., FastAPI’s async capabilities).
Documentation

Provide detailed docstrings.
Include a USAGE.md for instructions on how to use the assistant.
Provide a README.md with an overview, setup instructions, and architecture details.
Update CHANGELOG.md to reflect the addition.

## License

This project is licensed under the MIT License.