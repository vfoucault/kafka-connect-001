#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
docker run -it --link test-mysql:test-mysql --rm mysql sh -c 'exec mysql -h"test-mysql" -P"3306" -uroot -p"abcd1234"'

