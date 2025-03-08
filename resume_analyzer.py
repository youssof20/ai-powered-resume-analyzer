import spacy
from transformers import pipeline

# Load spaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Load BERT model for sentiment and semantic analysis
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

def analyze_resume(resume_text):
    # Process resume text with spaCy NLP
    doc = nlp(resume_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]  # Extract entities like skills, company names
    
    # Perform a BERT-based analysis (zero-shot classification)
    job_description = "Analyze if this resume fits an AI job."
    analysis = classifier(resume_text, candidate_labels=["AI", "Data Science", "Software Engineering", "Marketing"])

    return {
        "entities": entities,
        "job_fit": analysis['labels'][0],  # Best job fit
        "score": analysis['scores'][0]     # Confidence score
    }
