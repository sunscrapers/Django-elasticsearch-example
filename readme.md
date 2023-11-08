# Django Elasticsearch Example

Simple project to test Elasticsearch with Django, build on docker.

###### WARNING! This project is only for local testing, it's not prepared for deployment into remote server.

## Prerequisites

- Docker
- Docker-compose

## Getting Started

Steps to build, load data from fixtures and run project:

1. Enter into root of the project
2. `make up`
3. `make bootstrap`

To test Elasticsearch in shell run these commands:

1. `make up`
2. `make shell` or `make bash`

## Examples of usage

```
cars = CarDocument.search().query('match', color='black')
for car in cars:
    print(car.color)

cars = CarDocument.search().extra(size=0)
cars.aggs.bucket('points_count', 'terms', field='points')
result = cars.execute()
for point in result.aggregations.points_count:
    print(point)
```

- http://localhost:8000/cars/?query=is - search and display cars, which contain the word ‘is’ in at least one of those fields: `name`, `color`, `description`

## Links

Check out article to this project:
https://sunscrapers.com/blog/how-to-use-elasticsearch-with-django/
