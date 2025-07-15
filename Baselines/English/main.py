import json
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import evaluate
import numpy as np
import os

# --- 1. Setup ---
# Ensure you have the required libraries installed:
# pip install transformers torch datasets evaluate sacrebleu sentencepiece bert_score

# --- 2. Data Loading ---
def load_data(file_path):
    """Loads the summarization data from a JSON file."""
    if not os.path.exists(file_path):
        print(f"Error: Data file not found at {file_path}")
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get("Instances", [])

# --- 3. Model and Metric Loading ---
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

def load_model_and_tokenizer(model_name):
    """Loads a pre-trained model and tokenizer."""
    print(f"Loading model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
    print("Model loaded.")
    return tokenizer, model

# Load metrics
print("Loading evaluation metrics...")
rouge = evaluate.load('rouge')
bertscore = evaluate.load('bertscore')
bleu = evaluate.load('bleu')
print("Metrics loaded.")

# --- 4. Generation and Evaluation Functions ---
def generate_summary(tokenizer, model, text, model_name):
    """Generates a summary for a given text using the specified model."""
    if "t5" in model_name:
        text = "summarize: " + text

    inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True).to(device)
    summary_ids = model.generate(inputs.input_ids, num_beams=4, max_length=150, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def compute_scores(predictions, references):
    """Computes ROUGE, BERT, and BLEU scores."""
    rouge_scores = rouge.compute(predictions=predictions, references=references, use_stemmer=True)
    bert_scores = bertscore.compute(predictions=predictions, references=references, lang="en")
    bleu_score = bleu.compute(predictions=predictions, references=references)

    return {
        "ROUGE-1 F1": rouge_scores['rouge1'],
        "ROUGE-2 F1": rouge_scores['rouge2'],
        "ROUGE-L F1": rouge_scores['rougeL'],
        "BERT Score F1": np.mean(bert_scores['f1']),
        "BLEU Score": bleu_score['bleu']
    }

# --- 5. Main Evaluation Loop ---
def evaluate_models_on_datasets():
    """Main function to run the evaluation."""
    # Define your datasets here. The script will look for these files.
    datasets = {"XSUM": "task1290_xsum_summarization_first250.json", "XLSUM": "task1357_xlsum_summary_generation_first250.json"}

    models = {
        "BART": "facebook/bart-large",
        "T5": "google-t5/t5-large"
    }

    all_results = {}

    for model_alias, model_name in models.items():
        tokenizer, model = load_model_and_tokenizer(model_name)

        for dataset_name, data_path in datasets.items():
            print(f"\n--- Evaluating {model_alias} on {dataset_name} dataset ---")
            dataset = load_data(data_path)

            if dataset is None:
                continue

            instance_results = []
            all_predictions = []
            all_references = []

            for i, instance in enumerate(dataset):
                print(f"Processing instance {i+1}/{len(dataset)}...")
                input_text = instance['input']
                reference_summary = instance['output'][0]

                # Generate summary
                generated_summary = generate_summary(tokenizer, model, input_text, model_name)

                # Compute individual scores
                scores = compute_scores(predictions=[generated_summary], references=[reference_summary])

                # Store results for this instance
                instance_results.append({
                    "id": instance.get('id', f'instance_{i}'),
                    "generated_summary": generated_summary,
                    "reference_summary": reference_summary,
                    "scores": scores
                })

                all_predictions.append(generated_summary)
                all_references.append(reference_summary)

            # Compute average scores for the dataset
            avg_scores = compute_scores(predictions=all_predictions, references=all_references)

            # Store all results
            if dataset_name not in all_results:
                all_results[dataset_name] = {}
            all_results[dataset_name][model_alias] = {
                "average_scores": avg_scores,
                "instance_details": instance_results
            }

            print(f"\nAverage Scores for {model_alias} on {dataset_name}:")
            for metric, score in avg_scores.items():
                print(f"  {metric}: {score:.4f}")

    # Save all results to a single JSON file
    with open("evaluation_results.json", "w", encoding='utf-8') as f:
        json.dump(all_results, f, indent=4, ensure_ascii=False)
    print("\n✅ Detailed results saved to evaluation_results.json")

if __name__ == "__main__":
    evaluate_models_on_datasets()