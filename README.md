### Updated README with Swagger Documentation

---

# Plot Generator API

The **Plot Generator API** is a creative tool designed to help users generate random characters, quotes, settings, and entire plots for storytelling. With this API, you can explore various genres and create fun, dynamic story ideas programmatically.

---

## Features

- Generate random characters, quotes, settings, and plots.
- Create, update, and retrieve details of characters, quotes, and settings.
- Integrated Swagger documentation for seamless exploration of API endpoints.

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework
- drf-yasg (for Swagger)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/georgeminyillahmensah/mashup_api.git
   cd mashup_api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

| Endpoint                          | Method  | Description                                   |
|-----------------------------------|---------|-----------------------------------------------|
| `/api/characters/random/`         | `GET`   | Fetch a random character.                    |
| `/api/characters/<int:pk>/`       | `PUT`   | Update an existing character by ID.          |
| `/api/quotes/random/`             | `GET`   | Fetch a random quote.                        |
| `/api/quotes/<int:pk>/`           | `PUT`   | Update an existing quote by ID.              |
| `/api/settings/random/`           | `GET`   | Fetch a random setting.                      |
| `/api/settings/<int:pk>/`         | `PUT`   | Update an existing setting by ID.            |
| `/api/plots/random/`              | `GET`   | Generate a random plot.                      |
| `/api/plots/`                     | `POST`  | Create a new plot (optional).                |
| `/swagger/`                       | `GET`   | Access the Swagger documentation.            |

---

## Using the API

### Random Character Example
**GET** `/api/characters/random/`
```json
{
    "id": 1,
    "name": "John Doe",
    "description": "A brave explorer with a mysterious past."
}
```

### Update Character Example
**PUT** `/api/characters/1/`
```json
{
    "name": "Jane Doe",
    "description": "A curious scientist exploring new worlds."
}
```

---

## Swagger Documentation

This API includes **Swagger Documentation** for easy testing and exploration of endpoints.  
To access it:

1. Start the development server.
2. Navigate to: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

Swagger provides an interactive UI to test endpoints and review request/response formats.

---

## Project Structure

```
plot-generator-api/
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── plot_generator/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt
```

---

## Future Enhancements

- Add user authentication to secure endpoints.
- Allow users to save and retrieve their favorite plots.
- Introduce advanced filtering options for characters, quotes, and settings.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contribution

Contributions are welcome! Please fork this repository, create a feature branch, and submit a pull request for review.

Happy storytelling! 🎉