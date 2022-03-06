Launch the docker with

```
$ make launch_docker
```

By default, ports 8000 and 8888 are forwarded to the host. This make target also supports adding in custom run-flags to
`docker run` by specifying the `DOCKER_ARGS` environment variable. For example, if I wanted to provide an additional
filemount from `~/foobar` in the host to `/foobar` in the container, I could do:

```
$ make launch_docker DOCKER_ARGS="-v ~/foobar:/foobar"
```
