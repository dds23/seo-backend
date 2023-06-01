#!/bin/bash

case $1 in

"" | "production" | "prod")
    echo "production"
    (
    set -a && . deployment/environments/production.ini && set +a
    uvicorn app.server:api --port 8080 --reload
    )
    ;;

*)
  echo "unknown: $1"
  ;;
esac
