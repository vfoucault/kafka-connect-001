#!/bin/bash
echo "Inserting 10K records"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
docker run -it -v $DIR/../scripts_sql:/tmp/scripts_sql --link test-mysql:test-mysql --rm mysql sh -c 'exec mysql -h"test-mysql" -P"3306" -uroot -p"abcd1234" < /tmp/scripts_sql/insert_records.sql'
echo "Done."

