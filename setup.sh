#!/bin/bash

function pyfile {
	echo '#!/usr/bin/python3' > $1
	chmod +x "$1"
	vi "$1"
}
