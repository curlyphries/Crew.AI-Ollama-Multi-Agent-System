# Ollama-Powered AI System with Crew.ai Extensions

# File Structure Overview

Below is the refined file structure for the project, designed to enhance modularity, ensure maintainability and support scalability as the system evolves.

```plaintext
crew-ai/
├── src/                     # Application code
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── memory.py
│   ├── utils.py
│   ├── main.py              # CLI entry point
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── ollama_agent.py
│   │   ├── search_agent.py
│   │   └── base_agent.py
│   ├── integrations/
│   │   ├── __init__.py
│   │   └── browserbase_client.py
│   └── settings/
│       ├── config.yaml
│       ├── secrets.env
│       └── logging.yaml
├── scripts/                 # Helper scripts
│   ├── init_db.py
│   ├── pull_models.sh
│   └── start_service.sh
├── tests/                   # Tests for application
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                    # Documentation
│   ├── installation.md
│   ├── api_reference.md
│   └── usage_tutorials/
│       ├── basic_usage.md
│       └── advanced_workflows.md
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker setup for application
├── CHANGELOG.md             # Project history
├── LICENSE                  # License information
├── README.md                # Project documentation
└── .gitignore               # Git exclusions
```

## 🤖 **Introduction**

Welcome to a system designed to bring the power of **local AI** to your hardware, powered by **Ollama** and enhanced by extensions like **Crew.ai**. At its core, this system uses Ollama to run advanced language models such as **Llama 2**, enabling privacy-first, cutting-edge AI functionality on your local machine.

Crew.ai serves as a flexible framework to organize and coordinate specialized agents, but the heart of the system is Ollama’s powerful local LLM capabilities.

With this project, you can:
- Leverage **Ollama** for hosting and querying state-of-the-art AI models.
- Extend functionality with customizable multi-agent systems like Crew.ai.
- Ensure your data remains private and secure with everything running locally.

This project is for anyone looking to explore local AI systems, whether you're new to AI or eager to dive deeper into multi-agent orchestration.

---

## **Why Ollama First?**

Ollama provides:

1. **Privacy-First AI**: All computations and data handling happen locally—no reliance on the cloud.
2. **Ease of Use**: Set up and run advanced language models with minimal configuration.
3. **Flexibility**: Supports integration with tools like Crew.ai for creating multi-agent workflows.
4. **Efficiency**: Optimized to run even on consumer-grade hardware, making it accessible for many.

Crew.ai adds optional structure to organize tasks, but the foundational capability of AI queries and responses comes from Ollama’s robust LLM functionality.

---

## 📚 **Table of Contents**

1. [Project Highlights](#project-highlights)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installing Ollama on Linux](#installing-ollama-on-linux)
5. [Project Installation](#project-installation)
6. [How It Works](#how-it-works)
    - [Handling Clarifications and Additional Information](#handling-clarifications-and-additional-information)
7. [Customization](#customization)
8. [Why Local AI Matters](#why-local-ai-matters)
9. [Benefits Over Alternatives](#benefits-over-alternatives)
10. [Future Plans](#future-plans)
11. [Contributions](#contributions)
12. [License](#license)
13. [Troubleshooting](#troubleshooting)

---

## 🚀 **Project Highlights**

- **Ollama as the Foundation**: Host advanced language models like **Llama 2** entirely on your machine.
- **Privacy First**: Your data stays local—no external servers, no tracking.
- **Extendable with Crew.ai**: Add specialized agents to organize tasks, enhance workflows, and manage interactions.
- **Modular & Evolvable**: Build and adapt the system over time to fit your needs.
- **User Control**: Complete freedom to enable or disable extensions.

---

## 🌟 **Features**

### **Powered by Ollama**
- Host and interact with **Llama 2** or other compatible models locally.
- Fast and secure, with all computations handled on your hardware.

### **Optional Multi-Agent System** (Crew.ai Extensions)
- Organize specialized agents for tasks such as:
  - **Search**: Retrieve and summarize information.
  - **File Management**: Read and write local files.
  - **Data Analysis**: Process structured or unstructured data.
  - **Task Coordination**: Collaborate between agents for complex workflows.

### **Advanced Capabilities**
- **Parallel Collaboration**: Agents work together to solve complex problems.
- **Custom Memory Options**: Short-term and long-term context retention.
- **Self-Reflection**: Agents evaluate their responses for continual improvement.
### Browserbase Integration
This project now includes optional integration with [Browserbase](https://www.browserbase.com), allowing agents to browse web pages using an AI-friendly remote browser. Use `BrowserbaseClient` in `src/integrations` to fetch content and `SearchAgent` to generate conservative, liberal, and neutral perspectives.


---

## 🖥️ **Requirements**

- **Operating System**: Ubuntu 20.04+ (or a compatible Linux distribution)
- **Python**: Version 3.9 or higher
- **Hardware**:
  - **Minimum**: 4-core CPU, 16 GB RAM, 50 GB storage
  - **Recommended**: GPU with at least 12 GB VRAM for faster model inference
- **Ollama**: Installed and running on your system ([Ollama Installation Guide](https://www.ollama.ai))

---

## 🔧 **Installing Ollama on Linux**

Follow these steps to install **Ollama** on Linux (Ubuntu 20.04+):

### 1. **Install Docker**

Ollama uses Docker to run local LLMs. Install Docker if it's not already installed:

```bash
sudo apt update
sudo apt install -y docker.io


- **Enable Docker to start on boot**:
  ```bash
  sudo systemctl enable docker
  sudo systemctl start docker
  ```

- **Verify Docker installation**:
  ```bash
  docker --version
  ```
  You should see Docker’s version information, e.g., `Docker version 20.10.7, build f0df350`.

### 2. **Pull the Ollama Docker Image**

Download the official **Ollama Docker image**:

```bash
docker pull ollama/ollama
```

### 3. **Run the Ollama Service**

Start the Ollama service using Docker:

```bash
docker run --name ollama -d -p 11434:11434 ollama/ollama
```

- This command:
  - Names the container `ollama`.
  - Runs it in detached mode (`-d`).
  - Maps port `11434` of your machine to port `11434` in the container.

### 4. **Verify Ollama is Running**

Check if Ollama is up and running:

```bash
curl http://localhost:11434/api/status
```

- You should receive a JSON response confirming the service status, e.g.:
  ```json
  {
    "status": "running",
    "version": "1.0.0"
  }
  ```

### 5. **Pull a Language Model (e.g., Llama2)**

Download a specific model, such as **Llama2**:

```bash
docker exec -it ollama ollama pull llama2
```

- **Explanation**:
  - `docker exec -it ollama`: Executes a command inside the running `ollama` container.
  - `ollama pull llama2`: Pulls the Llama2 model into Ollama.

Verify the model is downloaded:

```bash
curl http://localhost:11434/api/status
```

Look for the model status in the JSON response.

---

## 🛠️ **Project Installation**

After installing Ollama, proceed to set up the Crew.ai extensions:

### 1. **Clone the Repository**

Pull the project from your GitHub repository:

```bash
git clone https://github.com/curlyphries/crew-ai.git
cd crew-ai
```

### 2. **Install Python Dependencies**

Install the required Python packages:

```bash
pip install -r requirements.txt
```

- **`requirements.txt`** example:
  ```
  fastapi==0.95.2
  uvicorn==0.21.1
  requests==2.31.0
  pyyaml==6.0
  python-dotenv==0.21.0
  transformers==4.30.0
  ```

### 3. **Create Configuration Files**

Create a configuration file for agents and orchestrator settings.

#### **File**: `src/config/multi_agent_config.yaml`

```yaml
orchestration:
  multi_agent: true
  memory_store: vector_db

agents:
  - name: ollama_agent
    enabled: true
  - name: search_agent
    enabled: true
  - name: file_agent
    enabled: true
  - name: data_analysis_agent
    enabled: true
  - name: task_management_agent
    enabled: true
  - name: email_management_agent
    enabled: true
```

---

## 🧠 **How It Works**

1. **User Input**: You send a query or request via the API.
2. **Ollama as the Foundation**: The query is processed by Ollama’s language model.
3. **Optional Extensions**: If enabled, Crew.ai orchestrates specialized agents to handle tasks beyond text generation.
4. **Response**: The final answer is returned, with all processing done locally.

---

## 🔧 **Customization**

Crew.ai is designed to grow with you:

- **Add New Agents**: Easily create custom agents for specific tasks.
- **Upgrade Memory**: Switch between different memory backends, like FAISS or Weaviate.
- **Tweak Workflows**: Modify the Orchestrator to change how agents collaborate.

---

## 🛡️ **Why Local AI Matters**

- **Privacy**: Keep your data secure—no external servers involved.
- **Independence**: No subscriptions, no downtime, no limits.
- **Control**: Customize and evolve the system to fit your unique needs.

---

## 💡 **Benefits Over Alternatives**

Compared to other AI implementation methods, this project offers unique advantages:

1. **Full Local Control**:
   - Unlike systems that require partial or full cloud integration, Ollama ensures that all operations occur on your local machine. Your data never leaves your hardware.

2. **Integration Simplicity**:
   - Setting up Ollama with Docker is straightforward, and Crew.ai provides optional extensions for added modularity without complex dependencies.

3. **Enhanced Privacy**:
   - Many alternatives require external API keys or cloud services. With this system, you have zero reliance on external services for queries, ensuring maximum data security.

4. **Customizable Framework**:
   - Crew.ai extensions allow you to tailor the AI to fit your specific needs by enabling or disabling agents, tweaking memory systems, and more.

5. **Efficiency on Local Hardware**:
   - Ollama is optimized to run on consumer-grade hardware, making it accessible without requiring expensive cloud GPUs or enterprise infrastructure.

6. **Multi-Agent Flexibility**:
   - Crew.ai’s orchestrator offers a structured way to handle complex workflows by enabling collaboration among specialized agents—something missing in most LLM-only setups.

7. **Scalability and Modularity**:
   - You can scale by adding new agents or fine-tuning local models. The system evolves with your needs.

8. **Offline Availability**:
   - Operate entirely offline—no need for continuous internet access, making it ideal for sensitive environments or locations with limited connectivity.

---

## 💡 **Future Plans**

- Enhance Ollama’s integration with Crew.ai agents.
- Explore **fine-tuned local models** for specific tasks.
- Add multi-user support and advanced security measures.

---

## 🤝 **Contributions**

Your thoughts, suggestions, or improvements are always welcome! Feel free to open an issue or submit a pull request to enhance the system.

---

## 📝 **License**

This project is licensed under the **MIT License**. Feel free to use, modify, and build on it, but please provide attribution. See the [LICENSE](LICENSE) file for details.

