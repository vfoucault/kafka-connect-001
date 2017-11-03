#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
docker run -d -p 127.0.0.1:9200:9200 --rm --name=test-elasticsearch elasticsearch:latest
echo "Done."

