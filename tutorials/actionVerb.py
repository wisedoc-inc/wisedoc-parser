#!pip install https://huggingface.co/spacy/en_core_web_trf/resolve/main/en_core_web_trf-any-py3-none-any.whl


# import sys module
import spacy
import en_core_web_trf
from wisedoc_parser.actionVerbsExtractor import ActionVerbExtractor
import sys
# tell interpreter where to look
sys.path.insert(0, "..")


nlp = spacy.load("en_core_web_trf")


# Importing as module.
nlp = en_core_web_trf.load()

# fname = '/kaggle/input/aresume/AmaanResume.pdf'
# doc = fitz.open(fname)

# get input from request
text = """
Responsibilities:
• Collect and understand the requirements of feature from the Product Managers.
• Design an architecture from the requirements.
• Design Database schema and develop APIs related to the feature.
• Mentoring juniors on the product or the feature.
Achievements:
• Increased the efficiency of the report API by reducing the number of API calls made on each request from 6 to 1 and adding the response to the Redis cache.
• Developed a background job which helps in scheduling the Workflows at a given time. We acquired a $1 contract because to this feature.
• Developed a background job using to regenerate the reports with the latest data which are about to expire.
• Created an API to calculate all the licenses utilization details so that users could act on any licenses that were not being utilized or were being used inefficiently.
"""
# for page in doc:
#     text = text + str(page.get_text())

doc = nlp(text)

actionVerbs = ActionVerbExtractor(doc, nlp)


ACTION_VERB_PROCESSED = actionVerbs.prepare()

av_text_lemmed = actionVerbs.extractActionVerb(text)

matched = actionVerbs.getMatchedActionVerbs(
    av_text_lemmed, ACTION_VERB_PROCESSED)


print(matched)
