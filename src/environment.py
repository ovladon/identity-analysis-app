# environment.py

import os
import nltk

def setup_environment():
    # Set environment variables if needed
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'

    # Ensure NLTK resources are downloaded
    required_nltk_packages = ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']
    for package in required_nltk_packages:
        try:
            nltk.data.find(f'tokenizers/{package}')
        except LookupError:
            nltk.download(package, quiet=True)
        except:
            try:
                nltk.data.find(package)
            except LookupError:
                nltk.download(package, quiet=True)

