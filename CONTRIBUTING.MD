# How to Contribute to SKILL-IT

Thank you for contributing! To keep the project organized and efficient, please follow these guidelines.

## Git Workflow

We use a feature-branch workflow. **NEVER push directly to the `develop` or `main` branches.**

1.  **Sync your `develop` branch:** Before starting any new work, make sure your local `develop` branch is up-to-date.
    ```bash
    git checkout develop
    git pull origin develop
    ```

2.  **Create a new branch:** Create a new branch *from* `develop` for the feature you are working on. Name it clearly.
    - Good branch names: `feature/user-login-api`, `bugfix/cors-error`
    - Bad branch names: `my-branch`, `test`, `dev`
    ```bash
    git checkout -b feature/name-of-your-feature
    ```

3.  **Do your work:** Write your code. Make small, logical commits.
    - Good commit message: `feat: Add register user API endpoint`
    - Bad commit message: `updated files`
    ```bash
    git add .
    git commit -m "feat: Describe your change clearly"
    ```

4.  **Push your branch to GitHub:**
    ```bash
    git push -u origin feature/name-of-your-feature
    ```

5.  **Create a Pull Request (PR):**
    - Go to the GitHub repository.
    - Click the "Compare & pull request" button for your new branch.
    - Set the base branch to `develop`.
    - Write a clear title and description for your PR, explaining what you did.
    - Assign a reviewer (the team lead).

## Code Style

- **Backend (Python):** We follow the PEP 8 style guide.
- **Frontend (JavaScript/React):** We will use Prettier for automatic code formatting.

---