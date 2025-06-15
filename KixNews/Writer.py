import json
from GeminiPro import GenAI
from markdown import markdown
import re

def ExtractData(text):
    try:
        pattern = re.compile(r'\[\s*"[^"]*"(?:\s*,\s*"[^"]*")*\s*\]', re.DOTALL)
        match = pattern.search(text)
        if match:
            data = json.loads(match.group())
            return data
        else:
            return []
    except Exception as e:
        print(e)
        return []
    
########## Title Selection ##########

def GenerateTitles(Topic, Context):
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article on "{Topic}".
    Use very Simple words and construct a Catchy, Attractive and Informative, Long Tail Title which is SEO Optimized and Ranks High on Google and also Reader Friendly.
    Title should be Reader friendly and it should be easily understandable by all audience.
    Use the below Context and Give me 5 different Variations. Your response should be an Array of Titles. Format: Each index should be enclosed within Double Quotes and All the Indexes should be collectively enclosed within Square Brackets.
    Context: {Context}
    """

    Titles = GenAI(query)

    try:
        Titles = ExtractData(Titles)
    except Exception as e:
        print(e)

    if isinstance(Titles, list) and Titles:
        return Titles
    else:
       return GenerateTitles(Topic, Context)
    
def SelectTitle(Topic, Titles, Context):
    TitleString = "\n".join(Titles)
    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article on "{Topic}".
    Using the below provided context select the best title out of these (Select One): {TitleString}
    Your response should be enclosed within Double Quotes. Format: "Title".
    Context: {Context}
    """

    Title = GenAI(query)

    try:
        # Title = str(Title.strip("*").strip("#"))
        special_characters = "*#"
        translation_table = str.maketrans('', '', special_characters)
        Title = Title.translate(translation_table)
    except Exception as e:
        print(e)

    if isinstance(Title, str) and Title:
        Title = str(Title.strip("*").strip("#"))
        return Title
    else:
       return SelectTitle(Topic, Titles)

######### Sub Headings ##########

def GenerateSubHeadings(Title, Context):
    # query= f"""
    # Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".
    # Suggest me the list of Sub Headings to include in the article to make it detailed, descriptive, informative and also engaging for users.
    # Use the below Context and Give me minimum 6 Subheadings and maximum any number according to the content. 
    # Sub Headings should be Reader friendly and it should be easily understandable by all audience.
    # Your output should not contain the provided title itself and don't include subheadings for intro and conclusion.
    # Your response should be an Array of Sub Headings. Format: Each index should be enclosed within Double Quotes and All the Indexes should be collectively enclosed within Square Brackets.
    # Context: {Context}
    # """

    # query= f"""
    # Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".
    # Suggest me the list of Sub Headings to include in the article to make it detailed, descriptive, informative and also engaging for users.
    # Use the below Context and Give me minimum 3 Subheadings and maximum any number according to the content. Be straight to the point with Subheadings.
    # Sub Headings should be Reader friendly and it should be easily understandable by all audience.
    # Your output should not contain the provided title itself and don't include subheadings for intro and conclusion.
    # Your response should be an Array of Sub Headings. Format: Each index should be enclosed within Double Quotes and All the Indexes should be collectively enclosed within Square Brackets.
    # """

    query= f"""
    Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".
    Using the below provided compiled context, Suggest me the list of Sub Headings to include in the article to make it detailed, descriptive, informative and also engaging for users.
    Use the below Context and Give me Subheadings to write a detailed article on it.
    Make sure that Sub Headings count is less than 5.
    Sub Headings should be Reader friendly and it should be easily understandable by all audience.
    Your output should not contain the provided title itself and don't include subheadings for intro and conclusion.
    Your response should be an Array of Sub Headings. Format: Each index should be enclosed within Double Quotes and All the Indexes should be collectively enclosed within Square Brackets.
    Context: {Context}
    """

    subheadings = GenAI(query)

    try:
        subheadings = ExtractData(subheadings)
        # subheadings = subheadings.strip("```")
        # subheadings = json.loads(subheadings)
    except Exception as e:
        print(e)

    if isinstance(subheadings, list) and subheadings:
        SubHeadingsFiltered = []
        for heading in subheadings:
            heading = str(heading.strip("*").strip("#"))
            if "intro" not in str(heading).lower() and "conclusion" not in str(heading).lower():
                SubHeadingsFiltered.append(heading)
        return SubHeadingsFiltered
    else:
       return GenerateSubHeadings(Title, Context)

######### Intro #########

def GenerateIntro(Title, Context):
    # query= f"""
    # Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".
    # Write me an Introduction Paragraph for the Article based on the context. Your writing style should be Simple and Engaging. Write to the point and don't ever use jargons. Should not contain any Headings.
    # Your writing should be Reader friendly and it should be easily understandable by all audience.
    # Write the Introduction in one or two Paragraphs according to the Title. 
    # Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    # """

    query = f"""
    Write Intro for the Website Article for the following Title: "{Title}". 
    Use context provided below. Use Very Simple Words and make it Reader Friendly and engaging. 
    Your output should contain multiple paragraphs and each paragraph should be enclosed within double quotes and comma separated. 
    Everything should be collectively enclosed by single square brackets as array format.
    Context: {Context}
    """

    intro = GenAI(query)

    try:
        # intro = intro.strip("```")
        # intro = json.loads(intro)
        intro = ExtractData(intro)
    except Exception as e:
        print(e)

    if isinstance(intro, list) and intro:
        return intro
    else:
       return GenerateIntro(Title, Context) 

######### Outro #########

def GenerateOutro(Title, Context):
    # query= f"""
    # Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".
    # Write me an Outro or Conclusion Paragraph for the Article based on the context. Your writing style should be Simple and Engaging. Write to the point and don't ever use jargons. Should not contain any Headings.
    # Your writing should be Reader friendly and it should be easily understandable by all audience.
    # Write the Introduction in one or two Paragraphs according to the Title. 
    # Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    # """
    query = f"""
    Write Outro for the Website Article for the following Title: "{Title}". 
    Use context provided below. Use Very Simple Words and make it Reader Friendly and engaging. 
    Your output should contain multiple paragraphs and each paragraph should be enclosed within double quotes and comma separated. 
    Everything should be collectively enclosed by single square brackets as array format.
    Context: {Context}
    """

    outro = GenAI(query)

    try:
        # outro = outro.strip("```")
        # outro = json.loads(outro)
        outro = ExtractData(outro)
    except Exception as e:
        print(e)

    if isinstance(outro, list) and outro:
        return outro
    else:
       return GenerateOutro(Title, Context)

######### Content #########

def GenerateContent(Title, SubHeading, Context):
    # query= f"""
    # Consider yourself as an experienced blogger. I'm going to write an article titled: "{Title}".\n
    # Write me article content for the Sub Heading using Context as supplement information: "{SubHeading}".\n 
    # Use very Simple words while you write, make sure that it is Reader friendly. Your writing should be Engaging. Also include engaging hooks and transitions. Write to the point and don't ever use jargons.
    # Also make sure that, output you provide is Search Engine Optimized.
    # Write the Content as much as possible relavant for the Subheading. Make sure that your content is split into paragraphs. Each paragraph should be three lines maximum. 
    # Your output should not contain any Headings or Subheadings strictly.
    # Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    # Context: {Context}
    # """

    query= f"""
    Consider yourself as an experienced blogger. I am going to write an article on Title: "{Title}".
    Write me article content for the Sub Heading using Context as supplement information: "{SubHeading}".\n 
    Use very Simple words while you write, make sure that it is Reader friendly. Your writing should be Engaging. Also include engaging hooks and transitions. Write to the point and don't ever use jargons.
    Also make sure that, output you provide is Search Engine Optimized.
    Write the Content as much as possible relavant for the Subheading. Make sure that your content is split into paragraphs. Each paragraph should be three lines maximum. 
    Your output should not contain any Headings or Subheadings strictly. Make sure that even 10 year old kid understands your english writing.
    Your response should be an Array of Paragraphs. Format: Each index should be enclosed within Double Quotes and all the Indexes should be Comma Seperated and collectively enclosed within Square Brackets. Example Format: ["Paragraph", "Paragraph", "Paragraph"].
    Context: {Context}
    """

    Content = GenAI(query)

    try:
        # Content = Content.strip("```")
        # Content = json.loads(Content)
        Content = ExtractData(Content)
    except Exception as e:
        print(e)

    if isinstance(Content, list) and Content:
        FinalContent = []
        for Paragraph in Content:
            if str(Title.strip("*").strip("#")) != str(Paragraph.strip("*").strip("#")):
                FinalContent.append(Paragraph)
        return FinalContent
    else:
       return GenerateContent(Title, SubHeading, Context)

######### Compile to MD #########

def CompileToMD(Intro, Outro, SubHeadings, Contents):
    Final = ""

    for a in Intro:
        Final = Final + a + "\n"

    for i in range(len(SubHeadings)):
        Final = Final + "## " + SubHeadings[i] + " ##" + "\n"
        for a in Contents[i]:
            Final = Final + a + "\n"

        Final = Final + "\n"

    for a in Outro:
        Final = Final + a + "\n"

    return Final

######### Compile to HTML #########

def CompileToHTML(Intro, Outro, SubHeadings, Contents):
    Final = ""

    for a in Intro:
        Final = Final + a + "\n"

    for i in range(len(SubHeadings)):
        Final = Final + "## " + SubHeadings[i] + " ##" + "\n"
        for a in Contents[i]:
            Final = Final + a + "\n"

        Final = Final + "\n"

    for a in Outro:
        Final = Final + a + "\n"

    Final = markdown(Final)

    return Final

######### Main #########

def Writer(Topic, Context):
    Titles = GenerateTitles(Topic, Context)
    Title = SelectTitle(Topic, Titles, Context)
    print("Titles Generated")
    print("-------")

    SubHeadings = GenerateSubHeadings(Title, Context)
    print(f"{len(SubHeadings)} SubHeadings Generated")
    print("-------")

    Intro = GenerateIntro(Title, Context)
    print("Intro Generated")
    print("-------")

    Outro = GenerateOutro(Title, Context)
    print("Outro Generated")
    print("-------")

    Contents = []
    count = 0
    for SubHeading in SubHeadings:
        Content = GenerateContent(Title, SubHeading, Context)
        Contents.append(Content)
        count = count+1
        print(f"SubHeading {count} Content Generated")
    print("-------")
    
    # MD = CompileToMD(Intro, Outro, SubHeadings, Contents)

    HTML = CompileToHTML(Intro, Outro, SubHeadings, Contents)
    return Title, HTML