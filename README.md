# Systatum Products API

This project is a simple RESTful API built as part of the
**Systatum Intern Member of Technical Staff Engineering Challenge**.

The application helps retailers record their products by providing an API
to create, retrieve, update, and delete products.


---

## Tech Stack

* **Python 3**
* **Django**
* **Django REST Framework**
* **SQLite** (development database)

This stack was chosen because it is mature, well-documented, and explicitly
recommended in the challenge description for candidates familiar with Django.

---

## Judgement & Design Decisions

### 1. Flexible Product Fields (JSON-based)

All product attributes are stored inside a single JSON field called `fields`.

**Example request body:**

```json
{
  "fields": {
    "name": "Ultramie Goreng",
    "price": 25000
  }
}
```

**Rationale:**

* The challenge explicitly states that product fields can be arbitrary
* JSON storage avoids frequent database schema migrations
* Supports different product types with different attributes
* Reduces coupling between the database schema and business logic

This approach trades strict schema enforcement for flexibility, which is
appropriate for early-stage or rapidly evolving product systems.

---

### 2. RESTful API Design

The application follows standard REST principles.

**Design Choices:**

* Resource-based URLs (e.g. `/products/`)
* Clear mapping of HTTP methods to actions:

  * `POST` → Create
  * `GET` → Retrieve
  * `PUT` / `PATCH` → Update
  * `DELETE` → Remove
* JSON used consistently for requests and responses

**Rationale:**

* REST APIs are widely understood and easy to consume
* Stateless requests allow horizontal scaling
* Clear conventions improve maintainability and developer experience

The API can be tested easily using tools such as Postman or `curl`.

---

### 3. No Front-End

**Rationale:**

* The challenge explicitly states that a front-end is not required
* The objective is to assess backend engineering judgement
* API functionality can be fully validated using HTTP clients

This keeps the solution focused, simple, and aligned with the challenge scope.

---

## API Endpoints

### Create Product

**POST** `/products/`

**Request:**

```json
{
  "fields": {
    "name": "Ultramie Goreng",
    "price": 25000
  }
}
```

**Response:**

```json
{
  "id": 1,
  "fields": {
    "name": "Ultramie Goreng",
    "price": 25000
  }
}
```

---

### Retrieve All Products

**GET** `/products/`

---

### Retrieve Single Product

**GET** `/products/{id}/`

---

### Update Product

**PUT** or **PATCH** `/products/{id}/`

Only the fields included in the request body will be overwritten.

**Example:**

```json
{
  "fields": {
    "price": 30000
  }
}
```

---

### Delete Product

**DELETE** `/products/{id}/`

---

## Running the Project Locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The server will be available at:

```
http://127.0.0.1:8000/
```
The main API endpoints are available at:

```
http://127.0.0.1:8000/products
```
---

## Scalability Considerations

**Rationale:**

* The application is stateless and can scale horizontally behind a load balancer
* SQLite is used for development simplicity and can be replaced with PostgreSQL
* JSON-based product fields allow schema evolution without database migrations
* Django REST Framework provides support for pagination, authentication, and throttling

These decisions ensure the application remains maintainable and scalable
as future requirements grow.

---

## Summary of Judgement
Key judgements include:

* Using a JSON-based data structure to support arbitrary product fields without schema changes
* Choosing Django REST Framework for rapid, readable, and production-ready API development
* Avoiding a front-end to keep focus on backend correctness and design reasoning
* Designing a stateless REST API to enable horizontal scalability


