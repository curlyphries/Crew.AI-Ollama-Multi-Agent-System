```markdown
# Crew.ai Ollama Multi-Agent System

## 🤖 **Introduction**

Welcome to **Crew.ai**, a personal journey into building **local AI systems** that are private, powerful, and customizable. This project is designed to run entirely on **your own hardware**, using the **Ollama framework** to host cutting-edge language models like Llama2. 

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
7. [Customization](#-customization)
8. [Why Local AI Matters](#-why-local-ai-matters)
9. [Future Plans](#-future-plans)
10. [Contributions](#-contributions)
11. [License](#-license)

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
  - Minimum: 4-core CPU, 16 GB RAM, 50 GB storage
  - Recommended: GPU with at least 12 GB VRAM for faster model inference
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
- Enable Docker to start on boot:
  ```bash
  sudo systemctl enable docker
  sudo systemctl start docker
  ```
- Verify installation:
  ```bash
  docker --version
  ```

### 2. **Pull the Ollama Image**
Download the official **Ollama Docker image**:
```bash
docker pull ollama/ollama
```

### 3. **Run the Ollama Service**
Start the Ollama service using Docker:
```bash
docker run --name ollama -d -p 11434:11434 ollama/ollama
```

- This starts the Ollama service on port `11434`.

### 4. **Verify Ollama is Running**
Test if the Ollama service is up by running:
```bash
curl http://localhost:11434/api/status
```
- If successful, you’ll see a JSON response confirming the service status.

### 5. **Optional: Install Specific Models**
Pull a specific LLM, such as **Llama2**:
```bash
docker exec -it ollama ollama pull llama2
```

---

## 🛠️ **Installation**

After installing Ollama, set up the Crew.ai project:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/curlyphries/crew-ai.git
   cd crew-ai
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the System**
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

4. **Test the System**
   Send your first query:
   ```bash
   curl -X POST http://localhost:8000/agent -H "Content-Type: application/json" \
       -d '{"query": "What’s the weather today?"}'
   ```

---

## 🧠 **How It Works**

1. **User Input**: You send a query or request.
2. **Orchestrator**: The system decides which agents can best handle the task.
3. **Agents**: Specialized modules (e.g., search, analysis, file I/O) process the request.
4. **Memory**: Relevant context from past interactions is retrieved to enhance responses.
5. **Response**: The final answer is returned, with all processing done locally.

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

---

## 🤝 **Contributions**

While this is a personal project, I’d love to hear your thoughts, suggestions, or improvements. If you try this out and build something cool, let me know!

---

## 📝 **License**

This project is licensed under the **MIT License**. Feel free to use, modify, and build on it, but please provide attribution. See the [LICENSE](LICENSE) file for details.

---

Take control of your AI future. Let’s build something amazing—together.
```
