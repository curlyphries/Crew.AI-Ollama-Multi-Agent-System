# Crew.ai Ollama Multi-Agent System

## 🤖 **Introduction**

Welcome to **Crew.ai**, my personal project that brings the power of **AI assistants** to **your own hardware**. This system is designed to run entirely **locally**, giving you complete control over your data while exploring the exciting potential of **multi-agent AI networks**.

With Crew.ai, you get:
- A **privacy-first AI assistant** that works without relying on the cloud.
- A **multi-agent system** where specialized agents collaborate to handle tasks like searching, summarizing, and managing files.
- The freedom to **customize, grow, and evolve** your system over time.

This project is perfect for those who value **security**, **control**, and **learning by doing**. Whether you're an AI enthusiast or just curious about creating your own assistant, Crew.ai is designed to help you explore the possibilities.

---

## 📚 **Table of Contents**

1. [Project Highlights](#-project-highlights)
2. [Features](#-features)
3. [Requirements](#️-requirements)
4. [Installing Ollama on Linux](#-installing-ollama-on-linux)
5. [Project Installation](#️-installation)
6. [How It Works](#-how-it-works)
    - [Handling Clarifications and Additional Information](#-handling-clarifications-and-additional-information)
7. [Customization](#-customization)
8. [Why Local AI Matters](#-why-local-ai-matters)
9. [Future Plans](#-future-plans)
10. [Contributions](#-contributions)
11. [License](#-license)
12. [Troubleshooting](#-troubleshooting)

---

## 🚀 **Project Highlights**

- **Privacy First**: Your data stays on your machine—no external servers, no tracking.
- **Local AI Models**: Powered by **Ollama**, running Llama2 or other compatible models entirely on your hardware.
- **Multi-Agent Collaboration**: Specialized agents for tasks like searching, summarizing, and managing files.
- **Memory & Recall**: Short-term conversation context and long-term memory for smarter responses.
- **Modular & Evolvable**: Add or upgrade agents, customize workflows, and adapt the system to your needs.

---

## 🌟 **Features**

- **Local AI Hosting**: Leverage Ollama to run cutting-edge AI models like Llama2 or Mistral locally, ensuring privacy and fast responses.
- **Multi-Agent Orchestration**: A central orchestrator coordinates multiple agents to handle tasks intelligently.
  - **Search Agent**: Retrieve and summarize information from local or external sources.
  - **File Agent**: Read from or write to local files for data processing.
  - **Data Analysis Agent**: Analyze and summarize structured/unstructured data.
- **Advanced Capabilities**:
  - **Self-Reflection**: Agents evaluate their own responses for continuous improvement.
  - **Parallel Collaboration**: Agents work together simultaneously to solve complex problems faster.
  - **Isolation & Security**: Each agent runs independently to prevent system-wide issues.

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
```

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

After installing Ollama, proceed to set up the Crew.ai project:

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

- **Explanation**:
  - **orchestration.multi_agent**: Enables multi-agent mode.
  - **memory_store**: Specifies the memory backend (e.g., `vector_db` can be FAISS, Weaviate).

---

## 🧠 **How It Works**

1. **User Input**: You send a query or request via the API.
2. **Orchestrator**: The system decides which agents can best handle the task based on the query content.
3. **Agents**: Specialized modules (e.g., search, analysis, file I/O) process the request.
4. **Memory**: Relevant context from past interactions is retrieved to enhance responses.
5. **Response**: The final answer is returned, with all processing done locally.

### 🔄 **Handling Clarifications and Additional Information**

Sometimes, your queries might be ambiguous or incomplete. To provide the most accurate and helpful responses, Crew.ai's agents are designed to request additional information or clarification when needed. Here's how this works:

#### **How It Works**

1. **Initial Query**: You send a query to Crew.ai via the API.
2. **Agent Evaluation**: The Orchestrator routes the query to the appropriate agent.
3. **Determining Completeness**:
    - **Sufficient Information**: If the agent can handle the query with the provided information, it processes and returns the response.
    - **Insufficient Information**: If the agent requires more details, it returns a clarification request.
4. **User Provides Clarification**: You respond with the necessary information.
5. **Agent Responds Accurately**: With the additional data, the agent provides a more accurate and detailed response.

#### **Example Scenario**

- **User Query**: "Schedule a meeting."
- **Agent Response**: "Sure, I can help with that. Could you please provide the date and time for the meeting?"
- **User Clarification**: "Schedule the meeting for tomorrow at 10 AM."
- **Agent Final Response**: "Meeting scheduled for tomorrow at 10 AM."

#### **Implementing Clarifications in Agents**

To enable agents to request clarification, each agent should implement logic to determine if the query has sufficient information. If not, the agent should return a prompt asking for the missing details.

##### **Example: Enhanced Task Management Agent**

```python
from datetime import datetime

class TaskManagementAgent:
    def __init__(self):
        self.tasks = []

    def can_handle(self, query: str) -> bool:
        return "task" in query.lower() or "reminder" in query.lower()

    def handle_query(self, query: str, session: dict) -> (str, dict):
        if "add task" in query.lower():
            task_details = query.lower().replace("add task", "").strip()
            if not task_details:
                return "Sure, I can help add a task. Could you please provide the task details?", session
            self.tasks.append({"task": task_details, "created_at": datetime.now()})
            return f"Task added: {task_details}", session
        elif "list tasks" in query.lower():
            if not self.tasks:
                return "No tasks available.", session
            task_list = "\n".join([f"{idx+1}. {task['task']} (Added on {task['created_at'].strftime('%Y-%m-%d %H:%M')})" for idx, task in enumerate(self.tasks)])
            return f"Your Tasks:\n{task_list}", session
        else:
            return "Task Management Agent can add or list your tasks.", session
```

---

## 🔧 **Customization**

Crew.ai is designed to grow with you:

- **Add New Agents**: Easily create custom agents for specific tasks (e.g., OCR, email management).
- **Upgrade Memory**: Switch between different memory backends, like FAISS or Weaviate.
- **Tweak Workflows**: Modify the Orchestrator to change how agents collaborate.

Explore the `src/agents/` folder to start building your own features.

---

## 🛡️ **Why Local AI Matters**

- **Privacy**: Keep your data secure—no external servers involved.
- **Independence**: No subscriptions, no downtime, no limits.
- **Control**: Customize and evolve the system to fit your unique needs.

---

## 💡 **Future Plans**

- Add support for **multi-user environments**.
- Enhance the **self-reflection capabilities** of agents.
- Explore **fine-tuned local models** for specific tasks like creative writing or technical analysis.
- Implement **advanced security measures** and **isolation techniques**.
- Integrate **continuous integration (CI)** for automated testing and deployment.
- Develop a **user-friendly interface** for easier interaction with Crew.ai.

---

## 🤝 **Contributions**

While this is a personal project, I’d love to hear your thoughts, suggestions, or improvements. If you try this out and build something cool, let me know!

Feel free to open an issue or submit a pull request. Your contributions can help make Crew.ai even better!

---

## 📝 **License**

This project is licensed under the **MIT License**. Feel free to use, modify, and build on it, but please provide attribution. See the [LICENSE](LICENSE) file for details.
