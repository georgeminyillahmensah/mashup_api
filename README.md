Here’s the updated README, incorporating the new changes and reflecting the use of Django REST Framework (DRF) generic views:

---

# Plot Generator API

The **Plot Generator API** is a creative tool designed to help users generate random characters, quotes, settings, and entire plots for storytelling. With this API, you can explore various genres and create fun, dynamic story ideas programmatically. The API now uses Django REST Framework (DRF) generic views for simplicity and maintainability, along with Swagger documentation for a seamless developer experience.

---

## Features

- Generate random characters, quotes, settings, and plots.
- Perform CRUD operations for characters, quotes, settings, and genres.
- Easily explore and test endpoints with integrated Swagger documentation.
- Simplified implementation using DRF generic views.

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework
- drf-yasg (for Swagger)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/georgeminyillahmensah/mashup_api.git
   cd mashup_api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

| **Endpoint**                     | **Method**  | **Description**                                   |
|-----------------------------------|-------------|---------------------------------------------------|
| `/api/characters/`               | `GET`, `POST` | List all characters or create a new character.    |
| `/api/characters/<int:pk>/`      | `GET`, `PUT`, `PATCH`, `DELETE` | Retrieve, update, or delete a character. |
| `/api/quotes/`                   | `GET`, `POST` | List all quotes or create a new quote.            |
| `/api/quotes/<int:pk>/`          | `GET`, `PUT`, `PATCH`, `DELETE` | Retrieve, update, or delete a quote.  |
| `/api/settings/`                 | `GET`, `POST` | List all settings or create a new setting.        |
| `/api/settings/<int:pk>/`        | `GET`, `PUT`, `PATCH`, `DELETE` | Retrieve, update, or delete a setting. |
| `/api/genres/`                   | `GET`, `POST` | List all genres or create a new genre.            |
| `/api/genres/<int:pk>/`          | `GET`, `PUT`, `PATCH`, `DELETE` | Retrieve, update, or delete a genre.  |
| `/api/plots/random/`             | `GET`       | Generate a random plot based on existing data.    |
| `/swagger/`                      | `GET`       | Access the Swagger documentation.                |

---

## Using the API

### Random Plot Example
**GET** `/api/plots/random/`
```json
{
    "plot": "In a Mystery story, John Doe finds themselves in a haunted mansion."
}
```

### Create a New Character
**POST** `/api/characters/`
```json
{
    "name": "Alice",
    "description": "A curious adventurer with a knack for exploring magical worlds."
}
```

Response:
```json
{
    "id": 1,
    "name": "Alice",
    "description": "A curious adventurer with a knack for exploring magical worlds."
}
```

### Update a Character
**PUT** `/api/characters/1/`
```json
{
    "name": "Alice",
    "description": "A brave explorer of enchanted lands."
}
```

---

## Swagger Documentation

The **Swagger Documentation** provides an interactive interface to explore and test all API endpoints.  
To access it:

1. Start the development server.
2. Open: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

Swagger offers a user-friendly way to understand request/response formats and test the API.

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

- **Authentication**: Add token-based authentication to secure endpoints.
- **Favorites**: Allow users to save and retrieve favorite plots, characters, and settings.
- **Advanced Filters**: Enable filtering by specific attributes for all models.
- **Pagination**: Implement pagination for endpoints returning large datasets.

---

## Contribution

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy storytelling! 🎉