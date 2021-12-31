FROM python:3.9

# Install our build tools
RUN bash -c "pip install poetry==1.2.0a2 nox"

ENTRYPOINT ["/bin/bash", "-cl"]
