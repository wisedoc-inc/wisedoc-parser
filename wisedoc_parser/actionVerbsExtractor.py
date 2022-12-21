import json


class ActionVerbExtractor:
    """Main class to Extract Action Verbs from a text.
    """

    def __init__(
        self,
        nlp,
        phraseMatcher,
        tranlsator_func=False
    ):
        """Constructor of the class.

        Parameters
        ----------
        nlp : [type]
            NLP object loaded from spacy.
        phraseMatcher : [type]
            A phrasematcher loaded from spacy.
        tranlsator_func :Callable
            A fucntion to translate text from source language to english def tranlsator_func(text_input: str) -> text_input:str
        """

        # params
        self.tranlsator_func = tranlsator_func
        self.nlp = nlp
        self.phraseMatcher = phraseMatcher

        return

    def extractActionVerb(self, text):
        """
         Parameters
        ----------
        nlp : [type]
            NLP object loaded from spacy.
        """
        doc = self.nlp(text)
        av_text_lemmed = []
        for token in doc:
            if token.pos_ == 'VERB':
                av_text_lemmed.append(token.lemma_)
                # print(token.text, token.lemma_, token.pos_)
        return av_text_lemmed

    def prepare(self):
        with open('buckets/actionVerbDB.json') as json_file:
            ACTION_VERB_DB = json.load(json_file)
        av_string = ' '.join(ACTION_VERB_DB)
        av_doc = self.nlp(av_string)
        av_lemmed = []
        for token in av_doc:
            av_lemmed.append(token.lemma_)
            print(token.text, token.lemma_, token.pos_)
        return av_lemmed

    def getMatchedActionVerbs(self, input_action_verbs, action_verbs_db):
        matched = set(input_action_verbs) & set(action_verbs_db)
        return list(matched)
