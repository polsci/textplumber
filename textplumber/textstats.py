"""Extract document-level statistics as features."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/40_textstats.ipynb.

# %% auto 0
__all__ = ['TextstatsTransformer']

# %% ../nbs/40_textstats.ipynb 3
from sklearn.base import BaseEstimator, TransformerMixin
from .store import TextFeatureStore

# %% ../nbs/40_textstats.ipynb 4
class TextstatsTransformer(BaseEstimator, TransformerMixin):
	""" Sci-kit Learn pipeline component to extract document-level text statistics based on the textstat library and pre-computed counts. 
		This component should be used after the SpacyPreprocessor component with the same feature store. 
		The statistics currently available are monosyllable count, polysyllable count, token count, sentence count, unique tokens count and average sentence length. """
	def __init__(self, 
			  	feature_store: TextFeatureStore, # the feature store to use
				columns = ['monosyll_count', 'polysyll_count', 'token_count', 'sentence_count', 'unique_tokens_count', 'average_sentence_length']
				#scale: bool = True, # whether to scale the features - not implemented yet
				):
		self.feature_store = feature_store
		#self.scale = scale
		# check that passed columns matches these ...
		possible_columns = ['monosyll_count', 'polysyll_count', 'token_count', 'sentence_count', 'unique_tokens_count', 'average_sentence_length']
		for col in columns:
			if col not in possible_columns:
				raise ValueError(f"Invalid column name: {col}. Possible columns are: {possible_columns}")
		self.columns = columns

	def fit(self, X, y=None):
		""" Fit is implemented but does nothing. """
		#if self.scale:        
		#	self.scaler_ = StandardScaler()
		#	self.scaler_.fit(self.feature_store.get_textstats_from_texts(X, self.columns))
		return self
	
	def transform(self, X):
		""" Transforms the texts to a matrix of text statistics. """
		textstats = self.feature_store.get_textstats_from_texts(X, self.columns)
		#if self.scale:
		#	textstats = self.scaler_.transform(textstats)
		return textstats
	
	def get_feature_names_out(self, input_features=None):
		""" Get the feature names out from the text statistics. """
		return self.columns

