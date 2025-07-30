from transformers import pipeline

# Initialize Hugging Face NER pipeline
nlp = pipeline("ner", model="dslim/bert-base-NER", tokenizer="dslim/bert-base-NER")

def extract_skills(text):
    # Basic skill extraction (to be refined with dataset)
    entities = nlp(text)
    skills = [entity['word'] for entity in entities if entity['entity'].startswith('B-') or entity['entity'].startswith('I-')]
    return list(set(skills))  # Remove duplicates