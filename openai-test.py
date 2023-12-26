import os
from openai import OpenAI
from dotenv import load_dotenv
import openai
import random

load_dotenv()
# print(os.environ.get("OPENAI_API_KEY")) #key should now be available

import os


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# Function to generate clues about a country
def generate_geography_clues():
    countries = [
 {"name": "Francia", "clues": ["Es conocida por la Torre Eiffel.", "La capital es París.", "Famosa por su cocina."]},
        {"name": "Japón", "clues": ["Está ubicado en Asia Oriental.", "El Monte Fuji es un punto de referencia prominente.", "El sushi es un plato popular."]},
        {"name": "Brasil", "clues": ["Es el país más grande de América del Sur.", "La selva amazónica se encuentra aquí.", "Río de Janeiro es una ciudad famosa."]},
        {"name": "España", "clues": ["Ubicado en la península ibérica.", "El flamenco es una forma de música y baile tradicional.", "Famoso por la Sagrada Familia en Barcelona."]},
        {"name": "México", "clues": ["Es el país más grande de habla hispana.", "La comida incluye tacos, enchiladas y guacamole.", "La Ciudad de México es la capital."]},
        {"name": "Italia", "clues": ["Conocido por su arquitectura renacentista.", "La pizza y la pasta son platos emblemáticos.", "Roma es la capital."]},
        {"name": "Indonesia", "clues": ["Es el país más grande del sudeste asiático.", "Compuesto por miles de islas.", "Tiene una gran diversidad cultural."]},
        {"name": "Uruguay", "clues": ["Pequeño país en América del Sur.", "Famoso por su carne y asados.", "Montevideo es la capital."]},
        {"name": "Argentina", "clues": ["El segundo país más grande de América del Sur.", "Conocido por el tango y el mate.", "Buenos Aires es la capital."]},
        {"name": "Estados Unidos", "clues": ["País ubicado en América del Norte.", "Compuesto por 50 estados.", "Washington D.C. es la capital."]},
        {"name": "Panamá", "clues": ["Conocido por el Canal de Panamá.", "Conecta el océano Atlántico con el Pacífico.", "La Ciudad de Panamá es la capital."]},
        {"name": "Senegal", "clues": ["País en África Occidental.", "Dakar es la capital.", "Famoso por su música y danza."]},
        {"name": "Sudáfrica", "clues": ["Ubicado en el extremo sur de África.", "Ciudad del Cabo y Pretoria son ciudades importantes.", "Conocido por su diversidad étnica."]},
        {"name": "Nicaragua", "clues": ["País en América Central.", "Famoso por los lagos Nicaragua y Managua.", "Managua es la capital."]},
        {"name": "Nigeria", "clues": ["País en África Occidental.", "Abuja es la capital.", "Famoso por su diversidad étnica y cultural."]},
        {"name": "India", "clues": ["El séptimo país más grande del mundo.", "Conocido por el Taj Mahal y el curry.", "Nueva Delhi es la capital."]},
        {"name": "China", "clues": ["País más poblado del mundo.", "Conocido por la Gran Muralla y la Ciudad Prohibida.", "Pekín es la capital."]},
        {"name": "Corea del Norte", "clues": ["País en Asia Oriental.", "Gobierno liderado por Kim Jong-un.", "Pyongyang es la capital."]},
        {"name": "Corea del Sur", "clues": ["País en Asia Oriental.", "Capitalismo y democracia.", "Seúl es la capital."]},
        {"name": "Irlanda", "clues": ["Isla en Europa.", "Conocida por sus paisajes verdes.", "Dublín es la capital."]},
        {"name": "Inglaterra", "clues": ["Parte del Reino Unido.", "Famosa por la familia real y el té.", "Londres es la capital."]},
        {"name": "Australia", "clues": ["Continente-isla en el hemisferio sur.", "Famoso por la Ópera de Sídney y los canguros.", "Canberra es la capital."]},
        {"name": "Nueva Zelanda", "clues": ["País insular en el Pacífico.", "Conocido por su belleza natural y el Señor de los Anillos.", "Wellington es la capital."]},
        {"name": "Filipinas", "clues": ["Archipiélago en el sudeste asiático.", "Compuesto por miles de islas.", "Manila es la capital."]},
        {"name": "Chile", "clues": ["País largo y estrecho en América del Sur.", "Famoso por la cordillera de los Andes y la Patagonia.", "Santiago es la capital."]},
        {"name": "Paraguay", "clues": ["País en América del Sur.", "Sin acceso al mar.", "Asunción es la capital."]},
        {"name": "Canadá", "clues": ["País en América del Norte.", "Segundo país más grande del mundo.", "Ottawa es la capital."]},
        {"name": "Austria", "clues": ["País en Europa Central.", "Famoso por la música clásica y los Alpes.", "Viena es la capital."]},
        {"name": "Portugal", "clues": ["País en la península ibérica.", "Famoso por el vino de Oporto y los azulejos.", "Lisboa es la capital."]},
        
      ]

    # Randomly select a country
    selected_country = random.choice(countries)

    # Return the clues for the selected country
    return selected_country["name"], selected_country["clues"]


# Start the conversation with a system message
conversation = [
    {"role": "system", "content": "Eres un experto en geografía."},
    {"role": "user", "content": "¿Me das una pista para adivinar el país?"}
]

# Make the initial API call to set up the model
initial_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation
)


# Display the model's initial response
print(initial_completion.choices[0].message.content)

# Define the number of turns in the conversation
num_turns = 1

# Game loop
for turn in range(num_turns):
    # Generate clues about a country
    correct_answer, clues = generate_geography_clues()

    # Display clues and prompt user for a guess
    print("Aquí tienes 3 pistas del país:")
    for clue in clues:
        print(clue)
    
    user_guess = input("Adivina: ")

    # Add the user's guess to the conversation
    conversation.append({"role": "user", "content": user_guess})

    # Check if the user's guess is correct
    if user_guess.lower() == correct_answer.lower():
        response = "¡Correcto!"
    else:
        response = f"Lo siento. La respuesta correcta es: {correct_answer}."

    # Print the response
    print(response)

    # Add the model's response to the conversation
    conversation.append({"role": "assistant", "content": response})

    # Make the API call with the updated conversation
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Display the model's response
    print(completion.choices[0].message.content)

# Display a closing message or game summary
print("Thanks for playing!")








# # Continue the conversation with back-and-forth interaction
# for turn in range(num_turns):
#     # Display the model's question and prompt user for a response
#     print(initial_completion.choices[0].message.content)
#     user_response = input("Tu respuesta: ")

#     # Add the user's response to the conversation
#     conversation.append({"role": "user", "content": user_response})

#     # Make the API call with the updated conversation
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=conversation
#     )

#     # Display the model's response
#     print(completion.choices[0].message.content)