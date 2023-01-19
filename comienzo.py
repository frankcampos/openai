
import openai

openai.api_key = "none"

# List of countries that speak Spanish
countries_in_spanish = ["Argentina", "Bolivia", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", 
                       "Ecuador", "El Salvador", "Equatorial Guinea", "Guatemala", "Honduras", "Mexico", 
                       "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Spain", "Uruguay", "Venezuela"]

# Create a list of prompts
prompts = ["What is the capital of " + country + "?" for country in countries_in_spanish]

# Initialize an empty list to store the answers
answers = []

# Iterate through the list of prompts
for p in prompts:
    # Use the OpenAI API to generate a text completion for each prompt
    completions = openai.Completion.create(engine="text-davinci-002", prompt=p, max_tokens=1024)
    # Append the answer to the list of answers
    answers.append(completions.choices[0].text)

# Print the list of answers
print(answers)






