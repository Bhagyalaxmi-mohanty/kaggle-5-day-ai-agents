import time

class DummyAgent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        print(f"🤖 {self.name} processing task: {task}")
        time.sleep(0.8)
        return f"{self.name} completed: {task}"


def parallel_architecture():
    print("\n🔹 Parallel Agent Architecture:")
    print("-------------------------------")

    agents = [
        DummyAgent("Vision Agent"),
        DummyAgent("Language Agent"),
        DummyAgent("Reasoning Agent"),
    ]

    tasks = [
        "Processing image inputs",
        "Understanding text instructions",
        "Drawing logical conclusions",
    ]

    outputs = []
    for agent, task in zip(agents, tasks):
        outputs.append(agent.run(task))

    print("\n✅ Combined Parallel Outputs:")
    for output in outputs:
        print("   ", output)
