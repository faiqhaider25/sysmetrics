# SysMetrics

SysMetrics is a powerful, real-time system monitoring and diagnostics tool built with a **FastAPI** backend and a responsive user interface. It provides comprehensive insights into system performance, making it ideal for developers, system administrators, and DevOps professionals.

## Features

- 📊 **Real-Time Monitoring**: Track system metrics with live updates.
- 💻 **CPU Performance**: Monitor CPU usage and performance metrics.
- 🧠 **Memory Utilization**: View memory usage and availability.
- 💾 **Disk Usage**: Keep tabs on disk space and storage metrics.
- 🌐 **Network Statistics**: Analyze network activity and performance.
- ⚡ **Responsive UI**: Enjoy a fast and intuitive web interface.
- 🔄 **Auto-Refreshing Metrics**: Stay updated with automatic metric refreshes.
- 🐳 **Docker Support**: Easily deploy using Docker and Docker Compose.

---

## Demo Video

[Watch the video on YouTube](https://www.youtube.com/watch?v=XzjtfzKpajM)

## Getting Started

SysMetrics can be run locally using a Python environment or deployed effortlessly with Docker (recommended for production).

### Option 1: Running Locally (Manual Python Setup)

#### Prerequisites

- **Python**: Version 3.8 or higher
- **Git**: For cloning the repository

#### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/faiqhaider25/sysmetrics.git
   cd sysmetrics
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   # On Windows
   python -m venv venv

   # Enable script execution temporarily
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

   # Then
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r src/requirements.txt
   ```

4. **Run the Application**:

   ```bash
   uvicorn syspulse.server:app --host 0.0.0.0 --port 8000
   ```

5. **Access the Dashboard**:
   - **Web Interface**: [http://localhost:8000](http://localhost:8000)
   - **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Option 2: Deployment with Docker (Recommended)

#### Prerequisites

- **Docker Desktop**: Includes Docker and Docker Compose
  - [Windows Installation](https://docs.docker.com/desktop/install/windows-install/)
  - [macOS Installation](https://docs.docker.com/desktop/install/mac-install/)
  - [Linux Installation](https://docs.docker.com/desktop/install/linux-install/)

#### Deployment Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/faiqhaider25/sysmetrics.git
   cd sysmetrics
   ```

2. **Run the Application**:

   - **Using Scripts**:
     - On Windows: Double-click `run.bat` or execute it in PowerShell.
     - On macOS/Linux: Run `./run.sh` in a terminal.
   - **Using Docker Compose**:
     ```bash
     docker-compose up -d
     ```

3. **Access the Dashboard**:

   - **Web Interface**: [http://localhost:8000](http://localhost:8000)
   - **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Prometheus**: [http://localhost:9090](http://localhost:9090)
   - **Grafana**: [http://localhost:3000](http://localhost:3000)

4. **Stop the Application**:
   ```bash
   docker-compose down
   ```

---

## API Endpoints

SysMetrics provides a set of RESTful API endpoints for accessing system metrics:

| Endpoint                  | Description                           |
| ------------------------- | ------------------------------------- |
| `GET /api/health`         | Check the application's health status |
| `GET /api/metrics/cpu`    | Retrieve CPU usage metrics            |
| `GET /api/metrics/memory` | Fetch memory usage statistics         |
| `GET /api/metrics/disk`   | Get disk space information            |

For detailed API specifications, visit [http://localhost:8000/docs](http://localhost:8000/docs) when the application is running.

---

## Development

To contribute to SysMetrics or set up a development environment, follow these steps:

1. **Install Development Dependencies**:

   ```bash
   pip install -r src/requirements-dev.txt
   ```

2. **Run Tests**:

   ```bash
   pytest
   ```

3. **Run Linting**:
   ```bash
   flake8 src/ --exclude=src/frontend,src/__pycache__ --max-line-length=120
   ```

---

## Contributing

We welcome contributions to SysMetrics! To get started:

1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m "Add AmazingFeature"
   ```
4. **Push to Your Branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**: Submit your changes for review.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

---

## Collaborators

- **Saud Ahmed** – _2021576_
- **Usama Sadiq** – _2022609_
- **Hassan Ahmed** – _2022211_
- **Syed Faiq Haider Naqvi** – _2022562_

---

Enjoy monitoring your system with SysMetrics! 🚀
