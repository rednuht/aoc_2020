#!/usr/bin/env bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

curl -s https://adventofcode.com/2020/day/$1/input \
  -H "cookie: session=$(cat ~/.aoc_session_cookie)" >"$DIR/day$1/input.txt"
