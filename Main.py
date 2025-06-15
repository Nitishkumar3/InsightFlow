import json
import google.generativeai as genai
from markdown import markdown

def GenAI(query):
    try:
        genai.configure(api_key="AIzaSyDTZzFzmpgNeZhy-YSRiPqjx9tzwLpmE0I")
        safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"}, {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}]
        model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config={"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}, safety_settings = safety_settings)
        convo = model.start_chat(history=[])
        convo.send_message(query)
        return convo.last.text.strip()
    except Exception as e:
        return str(e)

########## Start ##########

Topic = "DoT warns against picking up WhatsApp calls with foreign numbers +92"

########## Title ##########

def GenerateTitle(Topic):
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article titled "{Topic}".
    Construct a Catchy, Attractive and Informative Long Tail Title which is SEO Optimized and Ranks High on Google and also Reader Friendly.
    Your response should be enclosed within Double Quotes.
    """

    Title = GenAI(query)

    try:
        Title = str(Title.strip('"'))
    except Exception as e:
        print("Error in Title:", e)

    if isinstance(Title, str):
        return Title
    else:
       return GenerateTitle(Topic)

######### Sub Headings ##########

def GenerateSubHeadings(Title):
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article titled "{Title}".
    Suggest me the list of Sub Headings to include in the article to make it detailed, descriptive, informative and also engaging for users.
    Your response should be an Array of Sub Headings. Format: Each index should be enclosed within Double Quotes and All the Indexes should be collectively enclosed within Square Brackets.
    """

    subheadings = GenAI(query)

    try:
        subheadings = subheadings.strip("```")
        subheadings = json.loads(subheadings)
    except Exception as e:
        print("")

    if isinstance(subheadings, list):
        SubHeadingsFiltered = []
        for heading in subheadings:
            if "intro" not in heading.lower() and "conclusion" not in heading.lower():
                SubHeadingsFiltered.append(heading)
        return SubHeadingsFiltered
    else:
       return GenerateSubHeadings(Title)

######### Intro #########

def GenerateIntro(Title):
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article titled "{Title}".
    Write me an Introduction for the Article. Your writing style should be Simple and Engaging. Also include engaging hooks and transitions. Write to the point and don't ever use jargons. Should not contain any Headings.
    A paragraph should be strictly 3-4 lines maximum. Write in 1-3 Paragraphs according to the Title.
    Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    """

    intro = GenAI(query)

    try:
        intro = intro.strip("```")
        intro = json.loads(intro)
    except Exception as e:
        print("")

    if isinstance(intro, list):
        return intro
    else:
       return GenerateIntro(Title) 

######### Outro #########

def GenerateOutro(Title):
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article titled "{Title}".
    Write me an Outro for the Article. Your writing style should be Simple and Engaging. Also include engaging hooks and transitions. Write to the point and don't ever use jargons. Should not contain any Headings.
    A paragraph should be strictly 3-4 lines maximum. Write in 1-3 Paragraphs according to the title.
    Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    """

    outro = GenAI(query)

    try:
        outro = outro.strip("```")
        outro = json.loads(outro)
    except Exception as e:
        print("")

    if isinstance(outro, list):
        return outro
    else:
       return GenerateOutro(Title)

######### Content #########

def GenerateContent(Title, SubHeading):
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".
    Write me an article content for the Sub Heading: "{SubHeading}".
    Your writing style should be Simple and Engaging. Also include engaging hooks and transitions. Write to the point and don't ever use jargons. Should not contain any Headings.
    A paragraph should be strictly 3-4 lines maximum.
    Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    """

    Content = GenAI(query)

    try:
        Content = Content.strip("```")
        Content = json.loads(Content)
    except Exception as e:
        print("")

    if isinstance(Content, list):
        return Content
    else:
       return GenerateContent(Title, SubHeading)

######### Compile to HTML #########

def CompileToHTML(Intro, Outro, SubHeadings, Contents):
    Final = ""

    for a in Intro:
        Final = Final + a + "\n"

    for i in range(len(SubHeadings)):
        Final = Final + "# " + SubHeadings[i] + " #" + "\n"
        for a in Contents[i]:
            Final = Final + a + "\n"

        Final = Final + "\n"

    for a in Outro:
        Final = Final + a + "\n"

    Final = markdown(Final)

    return Final

######### Main #########

from time import time
s = time()

Title = GenerateTitle(Topic)
print(Title)
print(type(Title))
print()

SubHeadings = GenerateSubHeadings(Title)
print(SubHeadings)
print(type(SubHeadings))
print()

Intro = GenerateIntro(Title)
print(Intro)
print(type(Intro))
print()

Outro = GenerateOutro(Title)
print(Outro)
print(type(Outro))
print()

Contents = []
for SubHeading in SubHeadings:
    Contents.append(GenerateContent(Title, SubHeading))

print(Contents)
print(type(Contents))
print(len(Contents))


HTML = CompileToHTML(Intro, Outro, SubHeadings, Contents)

with open("file.html", 'w', encoding='utf-8') as file:
    file.write(HTML)
    
e = time()
print(e-s)