# Development

This document explains how to set up a development environment to contributing to *predlp*.

## Setting up a virtual environment
Install project dependencies
```
poetry install
```

Activate environment:
```
poetry shell
```

Add local *predlp* package for testing:
```
poetry install
```
## Testing

Run all test files directly using poetry run:
```
poetry run pytest
```
Run a specific file or test:
```
poetry run pytest -k <filename>
```

## Managing Dependencies

To add a development dependency:
```
poetry add --group dev <package_name>
```
To add a runtime dependency:
```
poetry add <package_name>
```
Ensure pyproject.toml and poetry.lock are updated:
```
poetry lock
```

## Packaging and releasing
The release process is automated using GitHub Actions. 
### Steps to Trigger a Release
1. Create a tag for the desired release. Ensure the tag matches the SemVer format and is applied to the correct commit.
    ```
    git tag <MAJOR.MINOR.PATCH>
    ```

2. Push the tag to the remote repository:
    ```
    git push origin --tags
    ```

This process automatically starts the release workflow.

