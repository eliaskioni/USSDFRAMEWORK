#!/usr/bin/env bash


celery -A ussd_airflow worker -E -n ussdframework-worker \
--concurrency=3 \
--loglevel=info
