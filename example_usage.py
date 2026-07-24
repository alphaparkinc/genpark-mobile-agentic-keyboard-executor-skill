from client import MobileAgenticKeyboardExecutorClient

def main():
    client = MobileAgenticKeyboardExecutorClient()
    res = client.execute_from_keyboard("Schedule lunch with Sarah tomorrow at 12pm", "messaging")
    print(f"Confidence: {res['intent_confidence']}")
    print(f"Action: {res['executed_action']}")

if __name__ == "__main__":
    main()
