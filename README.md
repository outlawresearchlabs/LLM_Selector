# LLM_Selector
# Auto Select the Best LLM for Your Use Case or Queries
Check out the youtube video
https://youtu.be/zCKwnfHB99k

Clone this Repo on your local drive and then get started.

This code selects the best model for your specific question.

# FLOW +>

Step 1: User Asks a Question

Step 2: A Local LLM runs checks to find the best model to run for the particular user input

Step 3: The user query is sent to the chosen one

Step 4: The chosen LLM runs giving the output


# CODE EXPLANATION

main.py +> Basic Implementation of Langchain for Ollama

main_working.py +> Gives your Terminal Experience (This is the full code your can run on your terminal using "python main_working.py")
    This is where we have primarily developed.  Currently it is a dynamic list of models, next steps is exception handling if the model is not already pulled, it will pull the model.

main_stream.py +> Give a Web UI experience using Streamlit (To run this code, type "streamlit run main_stream.py" on your terminal)

requirements.txt +> Run these requirements before running any codes above ("pip install -r requirements.txt" on your terminal)


# REQUIREMENTS:

1. You need to have Ollama Running on your System
   Check out these videos on Ollama:
   Ollama Videos:
https://youtu.be/lhQ8ixnYO2Y
https://youtu.be/ridRXgAmqoQ
https://youtu.be/oguOlJz7RIY



# To Do (may change)

1. Pull Model if not present
2. Autogen
3. MemGPT
4. More to come
