# LangChain Web Search Agent 🌐🤖

A smart conversational agent built using **LangChain**, powered by Google's **Gemini 2.5 Flash** model, and integrated with the **Tavily Search API** for real-time web browsing capabilities.

---

## 📊 System Flow & I/O Diagram

The flowchart below represents how data flows between the user, the LangChain agent, the Gemini model, and the external Tavily Search tool:

```mermaid
graph TD
    %% Styling Definitions
    classDef inputOutput fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1;
    classDef coreAgent fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    classDef toolStyle fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20;
    classDef decisionStyle fill:#F3E5F5,stroke:#6A1B9A,stroke-width:2px,color:#4A148C;

    %% Data Flow Nodes
    subgraph Input [📥 Input Phase]
        UserQuery["🗣️ User Message<br>('Who is cm of west bengal? Born details, etc.')"]:::inputOutput
        EnvVars["🔑 Env Credentials<br>(TAVILY_API_KEY, GOOGLE_API_KEY)"]:::inputOutput
    end

    subgraph Agent [🧠 Agent Execution Flow]
        LoadEnv["⚙️ load_dotenv()"]:::coreAgent
        InitModel["🤖 Gemini 2.5 Flash Model"]:::coreAgent
        InitAgent["🤝 LangChain Agent & Tools Registered"]:::coreAgent
        AgentDecision{"❓ Decision Node:<br>Does answering need web search?"}:::decisionStyle
    end

    subgraph Tools [🔧 External Services & Tools]
        SurfTool["🔍 surfInternet(query) Tool"]:::toolStyle
        TavilyAPI["🚀 Tavily Search API (Cloud)"]:::toolStyle
    end

    subgraph Output [📤 Output Phase]
        ConsoleOutput["🖥️ Console Output<br>(Final Answer Text)"]:::inputOutput
    end

    %% Flow Connections
    EnvVars --> LoadEnv
    LoadEnv --> InitModel
    InitModel --> InitAgent
    
    UserQuery --> InitAgent
    InitAgent --> AgentDecision
    
    %% Decision Routes
    AgentDecision -- "Yes (Current/External Info Needed)" --> SurfTool
    AgentDecision -- "No (Knowledge exists in model)" --> FinalResponse
    
    %% Tool Flow
    SurfTool -->|Sends API Request| TavilyAPI
    TavilyAPI -->|Returns Web Search Results JSON| SurfTool
    SurfTool -->|Yields Raw Results| InitAgent
    InitAgent --> AgentDecision
    
    %% Response
    FinalResponse["📝 Compile response using context"]:::coreAgent
    FinalResponse --> ConsoleOutput
```

---

## 🛠️ Features

- **Real-Time Web Search**: Utilizes Tavily search to fetch the latest online information.
- **State-of-the-Art LLM**: Powered by `gemini-2.5-flash` for fast, accurate response generation.
- **Agentic Workflow**: Automatically determines whether it needs to search the web or answer from the model's native knowledge.
- **Clean Structure**: Secure token management with dotenv support.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Installation
Clone this repository and install the dependencies:
```bash
# Clone the repository
git clone https://github.com/hsachan295-source/langchain-web-search-agent.git
cd langchain-web-search-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install langchain langchain-google-genai tavily-python python-dotenv
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory:
```env
TAVILY_API_KEY=your_tavily_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Running the Agent
Run the main script:
```bash
python main.py
```
