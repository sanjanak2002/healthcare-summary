# text_summarization.py

import spacy
from textblob import TextBlob
import itertools

def resolve_coreferences(text):
    # Use spaCy for coreference resolution
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    resolved_text = doc._.coref_resolved if doc._.has_coref else text
    return resolved_text

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    # Extract entities from the text
    entities = [ent.text for ent in doc.ents]
    return entities

def analyze_entity_relationships(entities):
    # Using co-occurrences of entities in the text
    entity_relationships = {}

    for entity_pair in itertools.combinations(entities, 2):
        entity_tuple = tuple(sorted(entity_pair))

        if entity_tuple in entity_relationships:
            entity_relationships[entity_tuple] += 1
        else:
            entity_relationships[entity_tuple] = 1

    return entity_relationships

def analyze_sentiment(text):
    # Use TextBlob for sentiment analysis
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    
    sentiment_result = {
        "score": sentiment_score,
        "label": sentiment_label,
    }
    
    return sentiment_result

def evaluate_context(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    entities = [ent.text for ent in doc.ents]
    
    # Analyze relationships between entities
    entity_relationships = analyze_entity_relationships(entities)
    sentiment = analyze_sentiment(text)
    context_evaluation_result = {
        "entity_relationships": entity_relationships,
        "sentiment": sentiment,
    }
    
    return context_evaluation_result

def summarize_text(text):
    # Use coreference resolution, NER, and context evaluation to generate a summary
    resolved_text = resolve_coreferences(text)
    entities = extract_entities(resolved_text)
    context_evaluation_result = evaluate_context(resolved_text)
    
    # Combine information for summary
    summary = {
        "resolved_text": resolved_text,
        "entities": entities,
        "context_evaluation_result": context_evaluation_result,
    }
    
    return summary
