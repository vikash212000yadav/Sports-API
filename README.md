# Sports Data API

- Provides API to receive data from external providers and update our system with the latest data about events in real time.

- Provides access to support team to allow to see the most recent data for each event and to query data.

### API Features:

1. Listing all the match stored in the system.

2. Filtering of listed items based on query parameters like `name`, `sport`, `ordering`.

3. Detailed view of a particular match using its `id`.

4. Uses nested serializers for detailed view of baby elements.

5. Retrieve football matches ordered by start_time.

6. Retrieve matches filtered by name.

### Steps to Run on Local Machine:

- `$python3 -m venv <env_name>`
- `$source <env_name>/bin/activate`
- `$pip install -r requirements.txt`
- `$python manage.py makemigrations`
- `$python manage.py migrate`
- `$python manage.py createsuperuser`
- `$python manage.py runserver`