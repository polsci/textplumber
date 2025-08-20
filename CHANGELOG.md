# Change log

## [0.0.10] - 2025-08-21

### Added

- functionality to aide interpretation of VADER scores for individual/multiple texts

### Changed

- document VaderSentimentProfileExtractor output options and experiments
- plot_sentiment_structure method of VaderSentimentProfileExtractor now using transform
- plot_sentiment_structure method - documented and added example 

### Fixed

- ensure the preview of texts in example notebook is filtered by selected label names

## [0.0.9] - 2025-08-07 - VADER estimator and feature extractor, NLTK preprocessor, stemming and lemmatization

### Added

- CHANGELOG.md added!
- VADER feature extraction and estimator, with examples
- Character ngram feature extraction, with examples
- save_results function to log experiment results
- added confusion matrix grid plot
- added experimental document sentiment profile feature extraction
- added experimental POS ngram sentiment feature extraction
- added method to SpacyPreprocessor and TextCleaner to identify they receive and return text for reporting functionality
- development team and acknowledgements
- improve doc home page and README with links to various functionality
- added NLTKPreprocessor
- added automatic reprocessing when preprocessor, embedder or important settings change
- added stemming and lemmatization via NLTK to TokensVectorizer

### Changed

- improved lexicon count performance
- updated Model2Vec transform to use batch_size
- improved example documentation
- skipping example runs in release tests
- checks for dataset parsing in report functions
- improved layout and responsiveness of doc site
- revised CI workflow to install language model for tests
- removed auto-install of SpaCy en_core_web_sm model and added documentation on how to install models
- revamped preview of dataset and features in pipeline
- improved report docs and examples
- moved token normalization (lowercasing, filtering punctuation/numbers/short words) from TextFeatureStore to TokensVectorizer

### Fixed

- fixed issue with documentation generation on embeddings/chars/vader, standardized layout

## [0.0.8] - 2025-04-24

### Added

- examples of feature plot  
- clarifications about package status to README etc  

### Changed

- report function documentation and examples  
- stop word function to output SpaCy-consistent tokens  

### Fixed

- issue with sparse array handling in decision tree plot  

## [0.0.7] - 2025-04-24

### Added

- documented report functionality with examples  

### Changed

- major changes to report functions for compatibility with complex pipelines, including depreciating some functions
- changed to SVG plots and improved labels  
- notebook tweaks to improve documentation rendering  

## [0.0.6] - 2025-04-23

### Fixed

- fixed missing fastcore dependency  

## [0.0.5] - 2025-04-23

### Changed

- amending min Python to 3.9  
- notebook changes to improve documentation readability
- streamlined nbdev test workflows by preventing execution of long-running training examples  

## [0.0.4] - 2025-04-22

### Changed

- min Python set to 3.8

## [0.0.3] - 2025-04-22

### Added

- caching of lexicons and stop words
- added example data loader and datasets requirement
- added annotation compatibility to earlier Python versions via __future
- added examples to demonstrate pipeline components
- added POS tagset support (for Spacy 'simple' UPOS and 'detailed' Penn Treebank POS tags)

### Changed

- changed introduction example to use example dataset
- changed notebook structure to use fastcore.basics patch for better documentation rendering with nbdev

## [0.0.2] - 2025-04-12

### Changed

- simplified README and to improve rendering of pypi project page

## [0.0.1] - 2025-04-12

Initial release of Textplumber
