# Change log

## [0.0.9] - pre-release, in-progress, not released to Pypi

### Added

- CHANGELOG.md added!
- VADER feature extraction and estimator, with examples
- Character ngram feature extraction, with examples
- save_results function to log experiment results
- added confusion matrix grid plot
- added experimental document sentiment profile feature extraction

### Changed

- improved lexicon count performance
- updated Model2Vec transform to use batch_size
- improved example documentation
- skipping example runs in release tests
- checks for dataset parsing in report functions
- improved layout and responsiveness of doc site
- revised CI workflow to install language model for tests
- removed auto-install of SpaCy en_core_web_sm model and added documentation on how to install models

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
