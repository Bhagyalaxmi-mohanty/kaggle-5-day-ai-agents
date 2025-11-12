import time

class DummyAgent:
    def __init__(self, name):
        self.name = name

    def run(self, task):
        print(f"🤖 {self.name} processing task: {task}")
        time.sleep(0.8)
        return f"{self.name} completed: {task}"


def negotiation_architecture():
    print("\n🔹 Negotiation-Based Agent Architecture:")
    print("----------------------------------------")

    buyer = DummyAgent("Buyer Agent")
    seller = DummyAgent("Seller Agent")

    proposal = buyer.run("Requesting AI dataset at low cost")
    counter = seller.run("Offering same dataset at higher price")
    agreement = buyer.run(f"Negotiating: {proposal} <-> {counter}")

    print("✅ Agreement Achieved:", agreement)
