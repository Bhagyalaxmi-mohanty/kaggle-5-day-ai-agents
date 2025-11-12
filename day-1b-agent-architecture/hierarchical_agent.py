import time

class DummyAgent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        print(f"🤖 {self.name} processing task: {task}")
        time.sleep(0.8)
        return f"{self.name} completed: {task}"


def hierarchical_architecture():
    print("\n🔹 Hierarchical Agent Architecture:")
    print("----------------------------------")

    manager = DummyAgent("Manager Agent")
    sub_agents = [
        DummyAgent("Sub-Agent A"),
        DummyAgent("Sub-Agent B"),
        DummyAgent("Sub-Agent C"),
    ]

    goal = "Plan and execute an AI research project"
    manager.run(f"Breaking down goal: {goal}")

    results = []
    for i, agent in enumerate(sub_agents, start=1):
        task = f"Task {i} for research step"
        results.append(agent.run(task))

    final_summary = manager.run(f"Combining all sub-results: {results}")
    print("✅ Hierarchical Result:", final_summary)
