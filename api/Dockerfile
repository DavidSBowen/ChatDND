# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the container
COPY . /app

ENV OPENAI_API_KEY=$OPENAI_API_KEY
EXPOSE 8000

# Set the entrypoint command to run the application
CMD ["poetry", "run", "python", "api/main.py"]
