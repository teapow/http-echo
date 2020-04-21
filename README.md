# http-echo

A simple, HTTP server (written with [Flask](https://flask.palletsprojects.com/)) that returns a response based on the value of the ECHO_MESSAGE environment variable.

Includes a Dockerfile to "containerise" the application.


## Building the image

To build the image, run the following command from the root of this repository:

```shell script
docker build . --tags=http-echo:latest
```

## Running the image

After building the image, it can be run locally with:

```shell script
docker run --rm --publish 8080:8080 --env ECHO_MESSAGE="Hello, world!" http-echo:latest 
```

You should be able to access the application by visiting http://localhost:8080/ in your browser.


## Supported environment variables

The behaviour of the application can be modified via the following environment variables:

| Name           | Default value                    | Description                                         |
|----------------|----------------------------------|-----------------------------------------------------|
| `ECHO_MESSAGE` | `"This is the default message."` | Controls the message returned in the HTTP response. |
| `SERVER_HOST`  | `"127.0.0.1"`                    | The hostname to listen on.                          |
| `SERVER_PORT`  | `8080`                           | The port of the webserver.                          |
| `SERVER_DEBUG` | `False`                          | Controls whether the webserver runs in debug mode.  |
