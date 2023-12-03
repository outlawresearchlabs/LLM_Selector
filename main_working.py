## Working case 
##Your LLM chooses the best LLM for your Specific Query
# Autoselect the best LLM for your specific Query | Ollama Implementation

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def fetch_content(url):
    """
    Fetch content from a single URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_available_models():
    url = 'https://ollama.ai/library'
    models_dict = {}

    content = fetch_content(url)
    if content:
        soup = BeautifulSoup(content, 'lxml')
        model_names = soup.find_all('h2', class_='mb-3 truncate text-lg font-medium underline-offset-2 group-hover:underline md:text-2xl')
        model_descriptions = soup.find_all('p', class_='mb-4 max-w-md')

        for name, desc in zip(model_names, model_descriptions):
            model_key = name.get_text(strip=True).lower().replace(' ', '-')
            model_value = desc.get_text(strip=True)
            models_dict[model_key] = model_value

    return models_dict


models_dict = get_available_models()


def select_best_model(user_input, models_dict):
    llm = Ollama(model="neural-chat") #Selector Model

    # Construct the prompt for the LLM
    prompt = f"Given the user question: '{user_input}', evaluate which of the following models is most suitable: Strictly respond in 1 word only."
    for model, description in models_dict.items():
        prompt += f"\n- {model}: {description}"
    # print('prompt:', prompt)
    
    # Send the prompt to the LLM
    llm_response = llm(prompt)

    # print("llm_response: ", llm_response)

    # Parse the response to find the best model
    # This part depends on how your LLM formats its response. You might need to adjust the parsing logic.
    best_model = parse_llm_response(llm_response, models_dict=models_dict)

    return best_model

def parse_llm_response(response, models_dict):
    # Convert response to lower case for case-insensitive matching
    response_lower = response.lower()

    # Initialize a dictionary to store the occurrence count of each model in the response
    model_occurrences = {model: response_lower.count(model) for model in models_dict}

    # Find the model with the highest occurrence count
    best_model = max(model_occurrences, key=model_occurrences.get)

    # If no model is mentioned or there is a tie, you might need additional logic to handle these cases
    if model_occurrences[best_model] == 0:
        return "neural-chat"  # Or some default model

    return best_model

while True:
    user_input = input("\nEnter the task you need assistance with or type /exit to quit  => ")

    if user_input.strip().lower() == "/exit":
        print("Exiting the program.")
        break
    
    best_model = select_best_model(user_input, models_dict)

    print("Selected model:", best_model)

    llm = Ollama(model=best_model, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

    response = llm(user_input)
