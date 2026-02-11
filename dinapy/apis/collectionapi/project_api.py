"""Class that extracts common functionality for Project entity"""

from .collectionapi import CollectionModuleApi

class ProjectAPI(CollectionModuleApi):

	def __init__(self, config_path: str = None, base_url: str = None, provided_token: str = None) -> None:
		super().__init__(config_path, base_url, provided_token)
		self.base_url += "collecting-event"
