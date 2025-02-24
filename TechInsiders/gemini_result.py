import google.generativeai as genai
import PIL.Image

def detect_objects(image_path, api_key):
    """
    Detect and identify objects in an image using Gemini Vision AI
    
    Args:
        image_path (str): Path to the image file
        api_key (str): Google AI API key
    
    Returns:
        str: Description of detected objects
    """
    # Configure the Gemini API
    genai.configure(api_key=api_key)

    # Load the model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Load and prepare the image
    image = PIL.Image.open(image_path)
    
    # Prompt for object detection
    prompt = """
    Please analyze this image and list all the main objects you can detect. 
    Format the response as a clear, detailed list of what you see.
    Give resource links to learn about the main object.
    """

    # Generate response
    response = model.generate_content([prompt, image])
    
    return response.text

def generate_quiz_questions(objects_text, api_key):
    """
    Generate quiz questions based on detected objects
    
    Args:
        objects_text (str): Text containing detected objects
        api_key (str): Google AI API key
    
    Returns:
        str: Generated quiz questions
    """
    # Configure the Gemini API
    genai.configure(api_key=api_key)

    # Load the model for text generation
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prompt for quiz generation
    prompt = f"""
    Based on these detected objects from an image:
    {objects_text}
    
    Generate 10 quiz questions about these objects. The questions should:
    1. Be a mix of multiple choice and short answer questions
    2. Test knowledge about the objects' functions, characteristics, and relationships
    3. Include the correct answers after each question
    4. Range from easy to challenging difficulty
    
    Format each question with a number, the question, and the answer on the next line.
    """

    # Generate response
    response = model.generate_content(prompt)
    
    return response.text

# Example usage
if __name__ == "__main__":
    # Replace with your API key
    API_KEY = "AIzaSyAI78rv14nGO2CG6vBuDQYunEzwvGa_8zk"
    
    # Replace with your image path
    IMAGE_PATH = "arduino.png"
    
    try:
        # Detect objects
        print("=== Object Detection Results ===")
        objects = detect_objects(IMAGE_PATH, API_KEY)
        print(objects)
        
        print("\n=== Generated Quiz Questions ===")
        quiz = generate_quiz_questions(objects, API_KEY)
        print(quiz)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
