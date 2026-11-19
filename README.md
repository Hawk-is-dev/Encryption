# Railway Fernet Key Generator

A minimal one-shot worker that generates a Fernet-compatible encryption key
and prints it to the Railway runtime logs.

## Deploy

1. Create a new GitHub repository and upload these files.
2. Create a Railway project from that repository.
3. Deploy it as a worker (the included `Procfile` runs `python main.py`).
4. Open the deployment's runtime logs and copy the generated key.
5. Set that value as `ENCRYPTION_KEY` in the bot's environment variables.

## Important

- Treat the key like a password. Anyone with access to the Railway project logs
  may be able to read it.
- Copy it once into the bot's environment variables, then delete/stop this
  generator service and avoid sharing its logs.
- Keep using the same key for data encrypted with it. Generating a different
  key later will not decrypt data encrypted with the old key.
- This project only generates a key; it does not connect to or modify your bot.
