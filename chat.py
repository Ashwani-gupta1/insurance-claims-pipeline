from src.ai.assistant import AIAssistant


def main():

    assistant = AIAssistant()

    print("=" * 70)
    print("      Insurance Claims AI Assistant")
    print("=" * 70)
    print("Ask questions about your Claims Warehouse.")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        question = input("\nAsk> ").strip()

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        if question == "":
            print("Please enter a question.")
            continue

        try:

            print("\nGenerating SQL and querying warehouse...\n")

            df = assistant.ask(question)

            if df.empty:
                print("No records found.")
                continue

            print("=" * 70)
            print("QUERY RESULT")
            print("=" * 70)
            print(df.to_string(index=False))

            print("\n" + "=" * 70)
            print("AI BUSINESS SUMMARY")
            print("=" * 70)

            summary = assistant.explain(df)

            print(summary)

        except Exception as e:

            print("\nError occurred:")
            print(e)


if __name__ == "__main__":
    main()