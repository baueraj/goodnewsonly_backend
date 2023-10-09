# Good News Only Backend

## Requirements

### Heroku Stack
- **Heroku (Stack 20)**
  - `requirements.txt`
    - Generate using: `poetry export -f requirements.txt --output requirements.txt`
  - `runtime.txt`

## Python Version and Heroku Stack

- **Python Version**: 3.9.9
- **Heroku Stack**: 20

## API Documentation and Testing

- API Docs: [Swagger UI](https://good-news-only-a0460683d0b8.herokuapp.com/docs)

## Curl Command for Testing

```bash
curl -X 'POST' 'https://good-news-only-a0460683d0b8.herokuapp.com/analyze' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"url": "https://www.bbc.com/news"}'
