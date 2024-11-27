# Shorten URL
* Allows shortening URLs in your local environment
* Redirects the shortened URLs to the desired URL

## API
* Create Short URL
Endpoint: `POST /api/shorten`
Request Body:
`{
  "url": "https://example.com/very/long/url"
}`

Response:
`{
"short_url": "http://localhost:5000/abc123",
"short_code": "abc123"
}`

* Redirect to Original URL
Endpoint: `GET /{short_code}`
Response: 302 Redirect to original URL

## Prerequisites
The following should be installed:
* Python3
* PostgreSQL
* Node.js + npm CLI

There should be a Postgres server running with the following configurations: (Which could and should be moved to the environment later)
* Port: 5433
* Database Name: shortenurl
* Database User: shorten_user
* Database Password: shorten_password

## Setup Environment
In BE directory:
```
  source .venv/bin/activate
  python3 app.py
```

In FE directory:
```
  npm run dev
```
