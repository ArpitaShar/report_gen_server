# 📄 ReportGeneratorServer

A modular FastAPI application powered by CrewAI agents to generate intelligent, multi-agent reports using data from databases, analysis tools, and LLMs.

---

## 📁 Project Structure

```
report-generator/
├── README.md                   <- Overview of the project, setup instructions, usage.
├── requirements.txt            <- Python dependencies (FastAPI, CrewAI, etc.).
├── .env.example                <- Example environment variables (DB URIs, API keys).

├── app/                        <- Application code package.
│   ├── main.py                 <- FastAPI app initialization and server startup.
│   ├── api/
│   │   └── routes.py           <- Defines API endpoint(s) like /generate-report.
│   ├── agents/                 <- CrewAI agent definitions and their prompt logic.
│   │   ├── data_agent.py       <- Fetches data from Postgres/Mongo using tools.
│   │   ├── analysis_agent.py   <- Performs data analysis and visualizations.
│   │   └── report_agent.py     <- Composes final report text using results.
│   ├── tools/                  <- Custom tool implementations used by agents.
│   │   ├── db_tools.py         <- @tool functions for SQL/Mongo queries.
│   │   └── other_tools.py      <- Placeholder for future tools.
│   ├── services/               <- Workflow orchestration & business logic.
│   │   ├── report_service.py   <- Runs CrewAI workflow: prepares agents, tasks, execution.
│   │   ├── pdf_service.py      <- Converts report content into downloadable PDF.
│   │   └── data_service.py     <- (Optional) Data preprocessing/postprocessing helpers.
│   ├── models/                 <- (Optional) ML models or LLM loader utilities.
│   │   └── llm_loader.py       <- Initializes LLMs (if not directly in agents).
│   └── utils/                  
│       ├── config.py           <- Reads env vars and sets up DB connections.
│       ├── logger.py           <- Logger configuration.
│       └── security.py         <- Input validation and basic security utilities.

├── servers/                    <- (Optional) MCP tool servers.
│   └── tool_server.py          <- Server exposing tools via MCP protocol.

├── data/                       <- (Optional) Example datasets or SQL files.
│   └── example_dataset.sql

├── tests/                      <- Unit and integration test suite.
│   ├── test_tools.py           <- Unit tests for custom DB tools.
│   ├── test_agents.py          <- Agent output testing.
│   ├── test_api.py             <- FastAPI endpoint integration tests.
│   └── test_full_pipeline.py   <- End-to-end pipeline validation including PDF output.

└── crew.yaml or crew.py        <- (Optional) Declarative configuration for CrewAI.
```

---

## 🛠️ Setup Instructions

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn app.main:app --reload
```

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🔐 Environment Variables

Create a `.env` file based on the example below:

```env
POSTGRES_URI=postgresql://user:pass@host:port/dbname
MONGO_URI=mongodb://user:pass@host:port/dbname
OPENAI_API_KEY=your-api-key-here
```

---