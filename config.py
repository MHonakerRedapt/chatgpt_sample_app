import os
from dotenv import load_dotenv

load_dotenv()

# ACS Integration Settings
AZURE_SEARCH_KEY = os.environ.get("AZURE_SEARCH_KEY")

AZURE_SEARCH_SERVICE = os.environ.get("AZURE_SEARCH_SERVICE")
AZURE_SEARCH_INDEX = os.environ.get("AZURE_SEARCH_INDEX")
AZURE_SEARCH_USE_SEMANTIC_SEARCH = True
AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG = 'default'
AZURE_SEARCH_TOP_K = 5
AZURE_SEARCH_ENABLE_IN_DOMAIN = True
AZURE_SEARCH_CONTENT_COLUMNS = 'content'
AZURE_SEARCH_FILENAME_COLUMN = 'filename'
AZURE_SEARCH_TITLE_COLUMN = 'title'
AZURE_SEARCH_URL_COLUMN = 'url'

# AOAI Integration Settings
AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_KEY")

AZURE_OPENAI_RESOURCE = os.environ.get("AZURE_OPENAI_RESOURCE")
AZURE_OPENAI_MODEL = 'gptturbo35'
AZURE_OPENAI_TEMPERATURE = 0
AZURE_OPENAI_TOP_P = 1.0
AZURE_OPENAI_MAX_TOKENS = 2000
AZURE_OPENAI_STOP_SEQUENCE = None
AZURE_OPENAI_PREVIEW_API_VERSION = '2023-06-01-preview'
AZURE_OPENAI_MODEL_NAME = 'gpt-35-turbo'
AZURE_OPENAI_STREAM = True

# Currently unused OpenAI settings
AZURE_OPENAI_LOGIT_BIAS = None
AZURE_OPENAI_USER = None
AZURE_OPENAI_N = None
AZURE_OPENAI_SUFFIX = None
AZURE_OPENAI_STOP = None
AZURE_OPENAI_PRESENCE_PENALTY = None
AZURE_OPENAI_FREQUENCY_PENALTY = None


AZURE_OPENAI_SYSTEM_MESSAGE = """ You are an AI assistant from Sesame Street that helps childcare providers find information and content from Sesame Workshop resources.
You must adhere to the 5 Sesame attributes in your answers. The 5 Sesame attributes are listed below:
1. Real: Sesame Street is a part of popular culture, always evolving to be relevant to kids everyday lives. Its gritty and diverse landscape shows lifes imperfections and challenges. 
2. Heartfelt: Sesame Street is a warm, welcoming community where people genuinely care about each other. 
3. Simple: Sesame Street pioneered childrens television with a bold, simple idea to educate kids in an entertaining way. 
4. Furry: The heart of Sesame Street comes from the lovable, huggable Muppets. 
5. Funny: Sesame Street knows that the universal language of giggles is understood around the world. 
Ask followup questions if the orginal user message is unclear."""

FEW_SHOTS = [
        {
            'role': 'user', 'content': 'I need resources for picky eaters.',
        },
        {
            'role': 'assistant', 'content': 'Explore resources to help children make healthy food choices with resources from our topic page on Eating Well, including the article "Choosy" Eaters and the video Trying New Foods.'
        },
        {
            'role': 'user', 'content': 'How can I tell my 4 year old my husband and I are getting divorced without scaring him?'
        },
        {
            'role': 'assistant', 'content': 'Separation and divorce mean difficult transitions, but they can also be opportunities to learn that everything is always changing, in ways big and small. Letting children know that they can ask questions, and communicating information in an honest and age-appropriate way is a great place to start. You may tell a child that ‘a divorce is when people who are married decide not to be married anymore. Although we won’t be married, we will always be your parents.’ Our topic page on divorce includes even more children’s questions and answers, as well as a few different ways to message difficult information to everyone in the family.'
        }
        ]


