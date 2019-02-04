# docker-compose-pyflask-with-nginx
Use the doecker-compose(version 3) to build the simple application of a flask with nginx.

## Outline
1. Use docker-compose to build the python falsk(runnung on uwsgi) with nginx.
2. Include to install flask, uwsgi and nginx setting.
3. implement a simple middleware by python decorator(for all json response).
4. It's a simple practice by docker-compose.

## Command
```shell
# Build
docker-compose up --build
# Run
docker-compose up
# Remove
docker-compose down -v
# If you need to prune all danlging data(network, images, containers)
docker system prune (-f)
```