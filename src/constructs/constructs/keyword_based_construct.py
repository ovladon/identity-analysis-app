from .base_construct import BaseConstruct

class KeywordBasedConstruct(BaseConstruct):
    def __init__(self, name, keywords, phrases=None):
        super().__init__(name)
        self.keywords = [kw.lower() for kw in keywords]
        self.phrases = [ph.lower() for ph in phrases] if phrases else []

    def analyze_text(self, text):
        try:
            text_lower = text.lower()
            words = text_lower.split()
            total_words = len(words)
            total_elements = total_words + len(self.phrases) if self.phrases else total_words

            keyword_count = sum(1 for word in words if word in self.keywords)
            phrase_count = sum(text_lower.count(phrase) for phrase in self.phrases)

            total_count = keyword_count + phrase_count
            score = (total_count / total_elements) * 100 if total_elements > 0 else 0.0
            return {self.name: {'score': score, 'error': False}}
        except Exception as e:
            return {self.name: {'score': 0.0, 'error': True, 'error_message': str(e)}}

