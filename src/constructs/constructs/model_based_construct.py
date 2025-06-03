from .base_construct import BaseConstruct
import torch

class ModelBasedConstruct(BaseConstruct):
    def __init__(self, name):
        super().__init__(name)

    def analyze_text(self, text, tokenizer, model):
        if tokenizer is None or model is None:
            return {self.name: {'score': 0.0, 'error': True, 'error_message': 'Model not loaded'}}

        try:
            inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt', max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=1)
            # Assume label 1 corresponds to the construct
            score = probabilities[0][1].item() * 100
            return {self.name: {'score': score, 'error': False}}
        except Exception as e:
            return {self.name: {'score': 0.0, 'error': True, 'error_message': str(e)}}

