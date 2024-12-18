import openai
import pandas as pd
import numpy as np

# OpenAI API Configuration
openai.api_key = 'your-api-key-here'  # Replace with your actual API key

# Example Data: Simulated with a simple dictionary for demonstration purposes
students_data = {
    "student_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "learning_history": ["Math A, Science B", "Math B, Science A", "Math A, Science A"],
    "preferred_style": ["visual", "auditory", "kinesthetic"],
    "progress_levels": [75, 84, 67]  # Simulated progress measures
}

# Convert example data to DataFrame
students_df = pd.DataFrame(students_data)

def generate_personalized_content(student_info):
    """Uses GPT to generate a learning plan for the student based on their personal data."""
    prompt = f"""
    Student Name: {student_info['name']}
    Learning Style: {student_info['preferred_style']}
    Current Performance: {student_info['learning_history']}
    Progress Level: {student_info['progress_levels']}%
    
    Based on this information, provide a personalized learning plan focusing on areas of improvement,
    interactive resources, and suggested activities that suit the student's learning style.
    """
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def personalize_learning():
    """Iterates through each student and generates learning content."""
    for _, student_info in students_df.iterrows():
        print(f"---\nGenerating content for: {student_info['name']}")
        content = generate_personalized_content(student_info)
        print(f"Learning Plan:\n{content}\n")

if __name__ == "__main__":
    personalize_learning()
