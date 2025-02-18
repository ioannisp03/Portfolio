# Portfolio Project

This is a personal portfolio project built with Vue.js for the frontend, Flask for the backend, and MongoDB for the database. The application is designed to showcase projects, skills, and gather user feedback.

## Tech Stack

- **Frontend**: Vue.js, Bootstrap
- **Backend**: Flask
- **Database**: MongoDB
- **Deployment**: DigitalOcean

## Project Setup

### Prerequisites

Ensure you have the following installed on your system:
- Node.js
- Python 3.x
- MongoDB (local or cloud instance)

### Frontend Setup

1. Navigate to the `portfolio-front-end` directory:
    ```sh
    cd portfolio-front-end
    ```

2. Install dependencies:
    ```sh
    npm install
    ```

3. Compile and Hot-Reload for Development:
    ```sh
    npm run dev
    ```

4. Compile and Minify for Production:
    ```sh
    npm run build
    ```

5. Run End-to-End Tests with Playwright:
    ```sh
    npx playwright install
    npm run build
    npm run test:e2e
    ```

6. Lint with ESLint:
    ```sh
    npm run lint
    ```

### Backend Setup

1. Navigate to the [Backend](http://_vscodecontentref_/0) directory:
    ```sh
    cd Backend
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Flask server:
    ```sh
    python main.py
    ```

## Routes

### Frontend Routes

- `/`: Home page
- `/login`: Login page
- `/register`: Register page
- `/admin-panel`: Admin panel (protected route)

### Backend Routes

- **Auth**
  - `POST /register`: Register a new user
  - `POST /login`: Login a user
  - `POST /logout`: Logout a user (JWT required)
  - `GET /protected`: Protected route (JWT required)
  - `GET /api/user`: Get user info (JWT required)

- **Projects**
  - `GET /projects`: Get all projects
  - `GET /projects/<projectId>`: Get project by ID
  - `POST /projects`: Add a new project
  - `PUT /project/<projectId>`: Update a project by ID
  - `DELETE /project/<project_id>`: Delete a project by ID

- **Testimonials**
  - `GET /testimonials`: Get all testimonials
  - `POST /testimonials`: Add a new testimonial
  - `PUT /testimonial/<testimonial_id>`: Update a testimonial by ID
  - `DELETE /testimonial/<testimonial_id>`: Delete a testimonial by ID

- **Email**
  - `POST /send-email`: Send an email

- **CV Download**
  - `GET /download-pdf`: Download CV PDF

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/)



## Deployment

The application is deployed on DigitalOcean. You can access it [here](https://starfish-app-bipd7.ondigitalocean.app/).
