# NLP Service

### Description

The NLP Service is meticulously developed to simplify and optimize the text transcription process. It offers support for various document types, including HTML and PDF files, ensuring a versatile and convenient experience for users. In addition to its primary transcription functionality, this microservice stands out for its ability to perform keyword extraction. This means that it not only converts text into a readable format but also identifies and highlights the most relevant and significant terms present in the original document.

### Technologies Used

- FastAPI
- Python
- Boto3
- Anthopic
- Amazon Bedrock

### Model used

- Anthropic Claude_v2

# Getting Started

1. Clone the repository:

```bash
    git clone https://gitlab.com/datalab/nlp_service
```

2. Run the server:

```bash
    docker-compose up --build
```

3. View the document