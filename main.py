import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def detect_text_in_image(image_path):
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = rekognition_client.detect_text(Image={'Bytes': image_bytes})

    detected_text = []
    for item in response['TextDetections']:
        detected_text.append(item['DetectedText'])

    return detected_text

if __name__ == "__main__":
    # Use environment variables from .env for AWS credentials
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    # Initialize the Amazon Rekognition client securely
    rekognition_client = boto3.client('rekognition', region_name='us-east-1',
                                      aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key)

    image_path = "/home/alif/amazon-rekog/lorem_ipsum.png"
    extracted_text = detect_text_in_image(image_path)
    print("Extracted Text:")
    print(extracted_text)
    for text in extracted_text:
        print(text)
