def version_to_module(version: str) -> str:
    return "v" + version.replace(".", "_")
