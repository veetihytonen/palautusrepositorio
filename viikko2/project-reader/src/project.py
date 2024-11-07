class Project:
    def __init__(self, name, description, proj_license, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = proj_license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        formatted = [f"- {dep}" for dep in dependencies]
        
        return "\n".join(formatted) if len(formatted) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nDependencies:\n{self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}\n"
        )
