# nlp_comparison.py

import spacy
from scispacy.ner import SciSpacyNer

def evaluate_ner_performance(gold_standard_entities, predicted_entities):
    """
    Evaluate NER performance by comparing predicted entities to the gold standard.
    """

    true_positives = len(set(gold_standard_entities) & set(predicted_entities))
    false_positives = len(set(predicted_entities) - set(gold_standard_entities))
    false_negatives = len(set(gold_standard_entities) - set(predicted_entities))

    # Calculate Precision
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0.0

    # Calculate Recall
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0.0

    # Calculate F1-score
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    return precision, recall, f1_score

def analyze_text_with_spacy(text, gold_standard_entities):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    predicted_entities = [ent.text for ent in doc.ents]

    # Evaluate NER performance
    precision, recall, f1_score = evaluate_ner_performance(gold_standard_entities, predicted_entities)

    print(f"SpaCy NER Performance:")
    print(f"Precision: {precision}, Recall: {recall}, F1-score: {f1_score}")

    return predicted_entities

def analyze_text_with_scispaCy(text, gold_standard_entities):
    ner = SciSpacyNer()
    doc = ner(text)
    
    predicted_entities = [ent.text for ent in doc.ents]

    # Evaluate NER performance
    precision, recall, f1_score = evaluate_ner_performance(gold_standard_entities, predicted_entities)

    print(f"SciSpacy NER Performance:")
    print(f"Precision: {precision}, Recall: {recall}, F1-score: {f1_score}")

    return predicted_entities
