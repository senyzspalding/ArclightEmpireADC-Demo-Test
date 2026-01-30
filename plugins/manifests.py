from description_harvester.plugins import Plugin
from description_harvester.iiif_utils import fetch_manifest, enrich_dao_from_manifest
from urllib.parse import urlparse, urlunparse
import requests
import yaml

class ManifestsPlugin(Plugin):
    """Plugin for reading digital object data from IIIF manifests.
    
    This is a local implementation example showing how to fetch and parse
    IIIF manifests to enrich digital object metadata. It handles both IIIF
    manifests and institution-specific web archive formats.
    """
    plugin_name = "manifests"

    def __init__(self):
        print(f"Set up {self.plugin_name} plugin for reading digital object data from IIIF manifests.")

    def update_dao(self, dao):
        """
        Reads and processes IIIF manifest data, extracting relevant information such as:
            - The manifest version (V2 or V3)
            - Thumbnail image URL
            - Textual content from renderings or canvas annotations
            - Rights statements
            - Metadata
        and updates the dao DadoCM fields

        Args:
            dao: The inital digital object record.

        Returns:
            dao: The updated digital object record with additions from the manifest.
        """

        # Initialize metadata if it's None
        if dao.metadata is None:
            dao.metadata = {}

        # Handle IIIF manifests

        # Start by checking if the identifier is a manifest URL
        domain = "cdm16694.contentdm.oclc.org"
        parsed = urlparse(dao.identifier)
        path = parsed.path
        if not parsed.hostname == domain or not path.startswith("/cdm/ref/collection/"):
            dao.action = "link"
        else:
            # If its a contentdm link, find the manifest
            new_identifier = path.replace(
                "/cdm/ref/collection/", ""
            ).replace(
                "/id/", ":"
            )
            dao.identifier = f"https://{parsed.hostname}/iiif/2/{new_identifier}/manifest.json"

            # Use iiif_utils to enrich the DAO with manifest data
            if enrich_dao_from_manifest(dao, manifest_url=dao.identifier):
                dao.action = "embed"
            else:
                print(f"Failed to fetch manifest, linking instead of embedding.")
                dao.action = "link"

        # Return the updated dao object
        return dao



