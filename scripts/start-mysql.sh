#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
docker run -d -e MYSQL_ROOT_PASSWORD=abcd1234 -p 127.0.0.1:3306:3306 --rm --name=test-mysql mysql 
docker run -it --link test-mysql:test-mysql --rm mysql sh -c 'while ! mysqladmin ping -h"test-mysql" --silent
do
 sleep 1
done'
docker run -it -v $DIR/../scripts_sql:/tmp/scripts_sql --link test-mysql:test-mysql --rm mysql sh -c 'exec mysql -h"test-mysql" -P"3306" -uroot -p"abcd1234" < /tmp/scripts_sql/create_db.sql'
docker run -it -v $DIR/../scripts_sql:/tmp/scripts_sql --link test-mysql:test-mysql --rm mysql sh -c 'exec mysql -h"test-mysql" -P"3306" -uroot -p"abcd1234" < /tmp/scripts_sql/create_proc.sql'
docker run -it -v $DIR/../scripts_sql:/tmp/scripts_sql --link test-mysql:test-mysql --rm mysql sh -c 'exec mysql -h"test-mysql" -P"3306" -uroot -p"abcd1234" < /tmp/scripts_sql/insert_records.sql'
echo "Done."

