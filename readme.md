# Django Elasticsearch Example

Simple project to test Elasticsearch with Django, build on docker.

###### WARNING! This project is only for local testing, it's not prepared for deployment into remote server.

## Prerequisites

* Docker
* Docker-compose

## Getting Started

Steps to build, load data from fixtures and run project:

1. `cd` to root of project
2. `docker-compose build`
3. `docker-compose run --service-ports --rm django python manage.py bootstrap`
4. `docker-compose up`

To test Elasticsearch in shell run these commands:
1. `docker-compose up`
2. `docker-compose exec django python manage.py shell`

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

- http://localhost:8000/cars/?search=description|is - search and display cars, which contain the word ‘is’ in the description.
- http://localhost:8000/cars/?id__gte=7 - filter and get only the cars which have ‘id’ greater or equal than 7.
- http://localhost:8000/cars/suggest/?name_suggest__completion=cor - get suggestions for the word ‘cor’.

## Links

Check out article to this project:
https://sunscrapers.com/blog/how-to-use-elasticsearch-with-django/

## Troubleshooting

- max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
  https://github.com/elastic/elasticsearch/issues/21523
