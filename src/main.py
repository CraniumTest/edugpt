from qa_system import QASystem
from virtual_ta import VirtualTeachingAssistant

def main():
    qa_system = QASystem()
    teaching_assistant = VirtualTeachingAssistant()

    while True:
        user_input = input("Enter your question or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            break
        
        if user_input.startswith("explain"):
            topic = user_input[len("explain "):].strip()
            explanation = teaching_assistant.explain_topic(topic)
            print(explanation)
        else:
            answer = qa_system.answer_question(user_input)
            print(answer)

if __name__ == "__main__":
    main()
