# WIP: Rapid Rift API


# For Developers

To run unittests (available in `/tests/`), install the dependencies required for testing,

    conda create -n test_env python=3.9
    conda activate test_env
    pip install .[test]
    # Run unittests using pytest
    pytest -v tests/

Before pushing the code, format it using `black` and `isort`, otherwise the CI pipeline will fail.

    # Format it
    black src/ tests/
    isort --profile src/ tests/

The CI/CD pipeline is implemented using Azure DevOps. Pipeline can be modified through YAML file in `/devops/azure.yaml`.
