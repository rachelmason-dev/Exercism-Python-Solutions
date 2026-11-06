#!/usr/bin/env bash

main () {
    word_reverse=""
    word="$1"
    l=${#word}
    for ((i = l-1; i >= 0; i--)); do word_reverse+=${word:i:1}; done
    echo "$word_reverse"
}
main "$@"