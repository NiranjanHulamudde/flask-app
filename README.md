# 🚀 Automated Flask Metadata Dashboard (DevOps Showcase)

A production-ready DevOps portfolio project demonstrating **Continuous Integration (CI)** and **Infrastructure as Code (IaC)**. This repository packages a lightweight Python web application, automates unit testing, builds a secure container image, and pushes it to Docker Hub via a Jenkins pipeline, while defining all cloud infrastructure in Terraform.

---

## 🏗️ Project Architecture

```text
[ Developer Push ] ──► [ GitHub Repo ] ──► [ Jenkins CI Pipeline ]
                                                 │
                                                 ├──► 1. Lint & Code Checkout
                                                 ├──► 2. Run PyTest Unit Tests
                                                 ├──► 3. Secure Docker Build
                                                 └──► 4. Push to Docker Hub 📦
```

---

## 🛠️ Tech Stack & Components

*   **Application:** Python 3.11 & Flask (Metadata tracking utility)
*   **Testing:** PyTest (HTTP status code and text token assertions)
*   **Containerization:** Docker (Alpine Linux base image, non-root user execution)
*   **CI/CD Automation:** Jenkins (Declarative Pipeline as Code)
*   **Infrastructure as Code:** Terraform (AWS Provider)

---

## 📦 What the Application Does
The Flask web application functions as a **dynamic infrastructure validation dashboard**. It reads system metrics to output:
1.  **Hostname / Container ID:** Validates network routing into isolated container namespaces.
2.  **Environment Flag (`APP_ENV`):** Proves runtime configuration injection works seamlessly without code rewrites.

---

## 🚀 Implemented Pipeline (CI)
The project utilizes a declarative `Jenkinsfile` that automatically executes the following phases upon trigger:

1.  **Code Checking:** Pulls the latest commits from the GitHub repository tracking branch.
2.  **Run Tests:** Dynamically creates a virtual environment, installs dependencies, and runs `pytest` to stop broken code before it is packaged.
3.  **Building the Image:** Compiles a production-ready container image tagged under the user namespace.
4.  **Pushing to Docker Hub:** Leverages secure Jenkins credential helper structures to authenticate and push the final image (`latest`) to the remote public registry.

---

## ☁️ Infrastructure Blueprint (IaC)
The `terraform/` directory contains complete architecture definitions to provision an enterprise-ready sandbox environment on AWS:

*   `providers.tf`: Sets up version constraints and registers the AWS cloud provider block.
*   `main.tf`: Configures the networking layout and server details:
    *   **Custom VPC & Subnets:** Isolated public networks.
    *   **Route Tables & Internet Gateway:** Attaches external routing properties safely.
    *   **Security Groups:** Open to `port 22` (SSH admin access) and `port 5000` (Flask application routing).
    *   **EC2 Instance Engine:** Configured to bootstrap with an automatic shell initialization script (`user_data`) that auto-installs Docker and spins up the app container on startup.
*   `outputs.tf`: Prints out the public EC2 runtime IP address dynamically upon infrastructure convergence.

---

## ⚙️ Local Development & Quickstart

To run and test the application environment locally on your workstation:

```bash
# 1. Clone the project
git clone https://github.com
cd flask-app

# 2. Build the Docker Image
docker build -t flask-devops-app .

# 3. Run the container locally
docker run -p 5000:5000 -e APP_ENV="Local-Dev" flask-devops-app
```
Open `http://localhost:5000` in your browser to verify it runs successfully.
