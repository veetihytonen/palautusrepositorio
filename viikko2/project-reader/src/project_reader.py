from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        deserialized = tomli.loads(content)
        project_data = deserialized["tool"]["poetry"]
        
        dependencies = list(project_data["dependencies"].keys())
        dev_dependencies = list(project_data["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project_data["name"], project_data["description"], project_data["license"], dependencies, dev_dependencies)
