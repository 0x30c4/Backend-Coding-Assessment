#!/usr/bin/env bash

export SECRET_KEY="django-insecure-a1ah*vm=+dmbg85)6v_*z!e97@49w!goe2f%msng6b-#2(ny@)"
export DEBUG=1

# DB CRED's
export POSTGRES_DB=fintech
export POSTGRES_USERNAME=root
export POSTGRES_PASSWORD=1234
export POSTGRES_HOST=192.168.0.100
export POSTGRES_PORT=1111

export PROD_HOST_DOMAIN="biniyogfintech.0x30c4.dev"

export DEBUG=0

if [[ $# > 0 ]]
then
	./manage.py runserver
else
	bash
fi
