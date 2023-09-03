# Login-Demo-Flask 🚀

[![GitHub stars](https://img.shields.io/github/stars/Akash-nath29/Login-Demo-Flask?style=social)](https://github.com/Akash-nath29/Login-Demo-Flask/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Akash-nath29/Login-Demo-Flask?style=flat-square)](https://github.com/Akash-nath29/Login-Demo-Flask/network)
[![GitHub issues](https://img.shields.io/github/issues/Akash-nath29/Login-Demo-Flask?style=social)](https://github.com/Akash-nath29/Login-Demo-Flask/issues)
[![GitHub license](https://img.shields.io/github/license/Akash-nath29/Login-Demo-Flask?style=flat-square)](https://github.com/Akash-nath29/Login-Demo-Flask/blob/master/LICENSE)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Akash-nath29/Login-Demo-Flask?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Akash-nath29/Login-Demo-Flask?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/Akash-nath29/Login-Demo-Flask?style=social)
![GitHub language count](https://img.shields.io/github/languages/count/Akash-nath29/Login-Demo-Flask)


A simple and secure login system implemented using Flask. This system allows users to register, log in, and enjoy a seamless authentication experience.

## Features 🌟

- User Registration
- User Login
- Secure Password Storage (bcrypt)
- Session Management
- User Authentication

## Technologies Used 🛠️

- **Flask**: A lightweight web application framework for Python.
- **Flask-Sqlalchemy**: A self-contained, serverless, and zero-configuration database engine.
- **HTML/CSS/JS**: For the frontend design.

## Getting Started 🚀

Follow these steps to get the project up and running on your local machine.

### Prerequisites 📋

- Python (3.6 or higher) installed.
- Pip package manager installed.

### Installation 🔧

1. Clone the repository:

   ```bash
   git clone https://github.com/Akash-nath29/Login-Demo-Flask.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Login-Demo-Flask
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Initialize the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. Start the Flask development server:

   ```bash
   flask run
   ```

8. Open your browser and go to `http://127.0.0.1:80/` to access the application.

## Usage 📝

- Register a new user account.
- Log in with your credentials.
- Enjoy the authenticated features.

## Contributing 🤝

Contributions are welcome! To contribute:

1. Fork the repository and create a new branch for your feature/fix.

2. Make changes, commit them, and push to your forked repository.

3. Create a pull request to the main project repository.

4. Your contribution will be reviewed and merged upon approval.


## License 📄

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Acknowledgments 🙏

- Special thanks to the Flask and Python communities for their awesome support and resources.

Happy Coding! 🚀🔒🐍

---

**Disclaimer:** This project is for educational purposes and should not be used for production without proper security considerations and enhancements.