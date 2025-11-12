import time

class DummyAgent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        print(f"🤖 {self.name} processing task: {task}")
        time.sleep(0.8)
        return f"{self.name} completed: {task}"


def sequential_architecture():
    print("\n🔹 Sequential Agent Architecture:")
    print("---------------------------------")

    agent1 = DummyAgent("Data Collector")
    agent2 = DummyAgent("Analyzer")
    agent3 = DummyAgent("Reporter")

    data = agent1.run("Gathering market trend data")
    analysis = agent2.run(f"Analyzing results from '{data}'")
    report = agent3.run(f"Creating summary for '{analysis}'")

    print("✅ Final Output:", report)
