# AI Multi-Agent Research System

A modular multi-agent system that generates structured reports from a high-level goal using a **Planner → Executor → Critic → Refine** workflow.

---

## Overview

This project implements a simple but extensible architecture for building AI agent systems.
Given a user-defined goal (e.g., *"Write a report on the future of AI in healthcare"*), the system:

1. Breaks the goal into actionable steps (Planner)
2. Executes each step sequentially (Executor)
3. Evaluates the final output (Critic)
4. Refines the output if needed (Refinement loop)

The result is a structured, coherent report generated through controlled coordination between agents.

---

## Features

* Multi-agent architecture (Planner, Executor, Critic)
* Iterative refinement loop
* Structured JSON outputs for reliability
* Modular design (easy to extend)
* Streamlit-based UI (optional)
* Clean separation of concerns

---

## Project Structure

```
/app
  /system
    planner.py
    executor.py
    critic.py
    workflow.py            -> core workflow file

  /ai_agents               -> agents with prompts
    planner_agent.py
    executor_agent.py
    critic_agent.py

  /utils
    helpers.py

  streamlit_app.py
  requirements.txt
  .env
```

---

## How It Works

### 1. Planner Agent

* Converts a high-level goal into structured steps
* Outputs JSON task list

### 2. Executor Agent

* Executes each step independently
* Produces structured intermediate outputs

### 3. Critic Agent

* Evaluates final output based on:

  * Accuracy
  * Completeness
  * Clarity
  * Consistency
* Returns score and improvement suggestions

### 4. Refinement Loop

* If score is below threshold, output is improved using feedback

---

## Installation

```bash
python -m venv .venv
Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Environment Variables

In `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Project

### Streamlit UI

```bash
streamlit run app_streamlit.py
```
---

## Example Usage

**Input:**

```
Write a report on the future of AI in healthcare
```

**Output:**

* Executive summary
* Structured sections
* Coherent multi-step generated report
* Critic-evaluated and refined content

---

## Current Limitations

* No persistent database 
* Limited error handling for edge cases
* Basic evaluation (can be improved with stronger metrics)
* No authentication or multi-user support

---

## Future Improvements

* Add database for report storage
* Improve retrieval (RAG + citations)
* Add user authentication
* Build production-ready API layer
* Enhance UI for better usability
* Add observability and logging dashboard

---

## Key Learnings

This project demonstrates:

* Agent orchestration patterns
* Prompt engineering with role separation
* Iterative refinement loops
* System design for AI applications

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---


## Author

Built as part of a rapid AI engineering project cycle focused on real-world system design and deployment.
