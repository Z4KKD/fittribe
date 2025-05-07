# FitTribe - Social Fitness Tracker

**FitTribe** is a fitness tracking platform that integrates gamification elements like XP, streaks, leaderboards, and workout logging. It also provides a fitness blog and scheduled challenges to keep users engaged and motivated. This repository contains a monorepo setup with the following services:

-   **WordPress**: Manages blog content and fitness challenges.
-   **FastAPI**: Handles user authentication, workout logs, and social features.
-   **Go**: Manages gamification logic, streaks, leaderboards, and XP calculation.

## 🚀 Features

-   **User Authentication**: Register, log in, and manage user profiles.
-   **Workout Logging**: Log workouts such as running, cycling, yoga, and weights.
-   **Gamification**: Earn XP, track streaks, and see leaderboard rankings based on workout performance.
-   **Fitness Challenges**: Participate in scheduled fitness challenges managed through WordPress.
-   **Fitness Blog**: Read fitness tips and articles from the WordPress blog.

## 📅 Roadmap

### 🔨 Phase 1: Project Setup & Architecture

1.  **Core Services**:

    -   **WordPress Service**: Handles blog content and fitness challenges.
    -   **FastAPI Service**: Manages user authentication, workout logs, and social features.
    -   **Go Service**: Handles gamification logic, streaks, and leaderboards.
2.  **Folder Structure (Monorepo Example)**:

    ```bash
    fittribe/
    ├── wordpress/             # WordPress instance (Dockerized)
    ├── fastapi-backend/       # Python FastAPI service
    ├── go-gamification/       # Go service for analytics and leaderboards
    ├── frontend/              # Optional: React or Flutter app
    ├── docker-compose.yml     # Service orchestration
    └── README.md              # This file
    ```

    **Tech Stack:**

    -   **WordPress**: WordPress + WP REST API + Custom Post Types
    -   **FastAPI**: FastAPI + PostgreSQL + Redis (optional)
    -   **Go**: Go + native HTTP or gRPC + Cron or Worker
    -   **Docker Compose**: To run all services locally

### 🔒 Phase 2: Authentication & User Management (FastAPI)

-   Register and log in using JWT (JSON Web Tokens).
-   User profiles: name, bio, avatar, and fitness goals stored in PostgreSQL.

### 🏋️ Phase 3: Workout Logging (FastAPI)

-   Log workouts like Running, Cycling, Weights, Yoga, etc.
-   Store logs with details like date, duration, intensity, and notes.
-   Auto-award XP based on workout rules.

### 🧠 Phase 4: Gamification (Go)

-   Calculate XP for each workout.
-   Track streaks and calculate weekly leaderboards.
-   Expose results via FastAPI or through a direct API for the frontend.

### 📰 Phase 5: Content (WordPress)

-   Fitness blog articles and tips.
-   Fitness Challenges: Created using a Custom Post Type and exposed through the WordPress REST API.
-   Create custom plugin for fitness challenge.

## 📦 Requirements

**Backend Services:**

-   Python (3.9 or higher)
-   FastAPI
-   PostgreSQL
-   Uvicorn
-   Passlib
-   Go (for gamification logic and analytics)
-   WordPress (Dockerized instance)
-   Redis (Optional for caching)

**Docker:**

-   Docker Compose for running the services locally.


## 💡 What’s Next:

-   Add more detailed analytics and gamification features.
-   Integrate additional workout types and progress tracking.
-   Enhance the frontend for a more interactive user experience.
