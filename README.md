*# Skillit: Your Personal AI Career Co-pilot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-in%20development-blue)]()

An intelligent, all-in-one platform designed to help students and professionals build their personal brand, identify skill gaps, and navigate the job market with confidence.

---

## 🚀 About The Project

The modern career journey is fragmented. Students use one tool for their resume, another for their portfolio, and countless websites for job searching and interview prep. This process is manual, time-consuming, and often fails to account for the automated screening systems (ATS) used by employers.

**Skillit** solves this by creating a unified, AI-driven ecosystem. By connecting with a user's professional profiles like LinkedIn and GitHub, Skillit automates the most tedious parts of personal branding. It then provides a suite of powerful, integrated tools to empower the user at every step of their career path—from building a portfolio to preparing for an interview.

### Key Features

*   ✅ **Frictionless Onboarding:** One-click signup using LinkedIn and GitHub to automatically import profile data, skills, and projects.
*   🎨 **Interactive Portfolio Builder:** Instantly generates a beautiful, responsive portfolio from user data with live-editing capabilities and multiple templates.
*   📄 **Dynamic Resume Suite:** Build ATS-friendly resumes from your profile, analyze them against real job descriptions, and export them as PDFs.
*   🧭 **Intelligent Career Explorer:** Get personalized career path recommendations based on your skills, discover trending jobs, and find "hidden gem" opportunities.
*   💡 **Skill-Gap Analysis:** For any target job, instantly see the skills you have and the skills you need to acquire, with links to learning resources.

---

## 🛠️ Tech Stack & Architecture

This project is built with a modern, scalable technology stack, chosen for its power in web development and machine learning.

| Layer          | Technology                                                                                                                                                                                                                                                                              |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**   | ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Material-UI](https://img.shields.io/badge/MUI-%230081CB.svg?style=for-the-badge&logo=mui&logoColor=white)                                                               |
| **Backend**    | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)                                                                           |
| **Database**   | ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)                                                                                                                                                                           |
| **ML/NLP**     | ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![spaCy](https://img.shields.io/badge/spaCy-%2309A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white)                                               |
| **Deployment** | ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)                                                               |

### System Architecture

The application follows a standard client-server architecture. The React frontend communicates with the Flask backend via a REST API. The backend handles business logic, user authentication, and interfaces with the MongoDB database and the Python ML scripts for analysis.

*(A more detailed visual diagram will be added here.)*

---

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have the following installed on your machine:

*   [Node.js](https://nodejs.org/) and npm
*   [Python 3.8+](https://www.python.org/) and pip
*   [Git](https://git-scm.com/)
*   [MongoDB Community Server](https://www.mongodb.com/try/download/community) or a MongoDB Atlas account.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Aksh2758/SKILL-IT.git
    cd SKILL-IT
    ```

2.  **Backend Setup:**
    ```sh
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Frontend Setup:**
    ```sh
    cd ../frontend
    npm install
    ```

4.  **Environment Variables:**
    You will need to create a `.env` file in the `backend` directory. This file will store your secret keys and database connection strings. Use the `.env.example` file as a template.
    ```env
    # .env.example
    MONGO_URI="your_mongodb_connection_string"
    SECRET_KEY="your_super_secret_key"

    GITHUB_CLIENT_ID="your_github_oauth_client_id"
    GITHUB_CLIENT_SECRET="your_github_oauth_client_secret"

    LINKEDIN_CLIENT_ID="your_linkedin_oauth_client_id"
    LINKEDIN_CLIENT_SECRET="your_linkedin_oauth_client_secret"
    ```

5.  **Run the Application:**
    *   **Run the Backend Server (from the `backend` directory):**
        ```sh
        flask run
        ```
    *   **Run the Frontend App (from the `frontend` directory in a new terminal):**
        ```sh
        npm start
        ```
    Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

---

## 🗺️ Project Roadmap

*   [x] **Phase 1: Core Functionality**
    *   [x] User Onboarding & Profile Creation via OAuth
    *   [x] Interactive Portfolio Builder with Code Download
    *   [x] Dynamic Resume Builder & Analyzer with PDF Export
    *   [x] Intelligent Career Explorer Dashboard
*   [ ] **Phase 2: Advanced Features**
    *   [ ] One-Click Portfolio Deployment (Netlify/Vercel)
    *   [ ] Mock Interview & Quiz Module
    *   [ ] Integration with Course APIs for Learning Resources

---

## 🤝 Contributing

This project is for our college mini-project. Contributions are managed by the team members.

1.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3.  Push to the Branch (`git push origin feature/AmazingFeature`)
4.  Open a Pull Request for team review.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 👥 Our Team

*   **Akshatha K S** - *The API & Logic Builder* - [GitHub Profile Link](https://github.com/Aksh2758)
*   **Keerthi V** - *The Visual Architect* - [GitHub Profile Link](https://github.com/Keerthi)
*   **Suhana** - *The AI Specialist* - [GitHub Profile Link](https://github.com/Suhana745)
*   **Shilpa Jayanth Naik** - *The Infrastructure Glue* - [GitHub Profile Link](https://github.com/Shilpa)
