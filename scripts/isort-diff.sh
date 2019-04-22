#!/bin/bash
# Check if isort show difference.

ISORT_OUTPUT=$(isort -rc . --diff)
IS_ISORT_DIFF=$(echo ${ISORT_OUTPUT} | grep '+')

if [ -z "$IS_ISORT_DIFF" ]
then
    exit 0
else
    echo "${ISORT_OUTPUT}"
    exit 1
fi
