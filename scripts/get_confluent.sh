#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR=$SCRIPT_DIR/../
SRC_DIR=$BASE_DIR/sources
mkdir $SRC_DIR 2>/dev/null
echo "Downloading confluent OSS 3.3.0..."
curl --silent -o $SRC_DIR/confluent-oss-3.3.0-2.11.tar.gz http://packages.confluent.io/archive/3.3/confluent-oss-3.3.0-2.11.tar.gz
echo "Downloading mysql jdbc driver..."
curl --silent -o $SRC_DIR/mysql-connector-java-5.1.44.tar.gz https://cdn.mysql.com//Downloads/Connector-J/mysql-connector-java-5.1.44.tar.gz
cd $SRC_DIR
tar xzpf confluent-oss-3.3.0-2.11.tar.gz
tar xzpf mysql-connector-java-5.1.44.tar.gz
cp $SRC_DIR/mysql-connector-java-5.1.44/mysql-connector-java-5.1.44-bin.jar $SRC_DIR/confluent-3.3.0/share/java/kafka-connect-jdbc/
echo "Done. CP Oss 3.3.0 available in $SCRIPT_DIR/sources/confluent-3.3.0"
echo ""
echo "to start : $SRC_DIR/confluent-3.3.0/bin/confluent start"
echo ""
