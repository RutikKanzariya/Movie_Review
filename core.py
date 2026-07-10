from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(model = 'mistral-small-2506')

# prompt = ChatPromptTemplate.from_messages([

#     ("system",
#      """
#     You are a Professional Movie Information Extractor Assistant.

#     Your Task:
#     Extract useful structured information from a movie paragraph and present is it in a structured format. The information you need to extract includes:
#     Rules:
#     - Do not include add explanations or extra information in your output.
#     - Do not add extra commentry
#     - Follow the exact format provided in the output schema.
#     - If information is missing, leave it as null or empty.
#     - Keep summary concise and to the point, highlighting the main plot points and themes of the movie.
#     - Do not guess unknown facts.

#     Output schema:
#     Movie Title:
#     Release Year:
#     Genre:
#     Director:
#     main Cast:
#     Setting/location:
#     Plot:
#     Themes:
#     Rating:
#     Notable Features:

#     Short Summary:

# """),

# ('human',"""Extract movie information from the paragraph: {paragraph}"""),
# ])




# para = input("Give your paragraph : ")

# final_prompt = prompt.invoke(

#     {
#         "paragraph": para
#     }
# )

# response = model.invoke(final_prompt)

# print(response.content)


'''
Interstellar is a 2014 science fiction movie directed by Christopher Nolan. It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain and Michael Caine. The story follows astronauts searching for a new home for humanity after Earth becomes uninhabitable. The movie won the Academy Award for Best Visual Effects.
'''

# Now we are moved on the Structured Output part. We will use Pydantic to define the output schema and parse the model's response into a structured format.
# But comapny want dont want text.
# They went data they can store,search,filter,recommend,analyze, sends to APIs. that called the structured op.
# Structured Output is a way to represent the information extracted from the movie paragraph in a structured format, such as JSON or a database schema. This allows for easy storage, searching, filtering, recommending, analyzing, and sending to APIs.
# The AI response fixed machine-readable format instead of the natural language.


# pydantic model for Structured Output
# Step 1 --> Define Schema 
class Movie(BaseModel):
    Movie_Title: Optional[str]
    Release_Year: Optional[int]
    Genre: List[str]
    Director: Optional[str]
    main_Cast: Optional[List[str]]
    Setting_location: Optional[str]
    Plot: Optional[str]
    Themes: Optional[List[str]]
    Rating: Optional[float]
    Notable_Features: Optional[List[str]]
    Short_Summary: Optional[str]

# Define Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# So we dont need need define prompt template.

prompt = ChatPromptTemplate.from_messages([
    ('system',"""
    Extract Movie Inforamtion from the Paragraph
     {format_instructions}
    """),
    ("human","{paragraph}")
])  

para = input("Enter Paragraph Here : ")
final_prompt = prompt.invoke(
    {
        "paragraph":para,
        'format_instructions':parser.get_format_instructions()
     },
    )

response = model.invoke(final_prompt)
print(response.content)