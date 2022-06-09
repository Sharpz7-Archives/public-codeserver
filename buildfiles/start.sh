#!/bin/sh

# Replace commas with spaces
SHARPDOMAINS=$(echo $SHARPDOMAINS | sed 's/,/ /g')
sudo sed -i "s/XXXXX/$SHARPDOMAINS/g" /sharpnet/nginx.conf

# Check if PORT is set
if [ -z "$PORT" ]; then
    sudo sed -i "s/8080/$PORT/g" /sharpnet/nginx.conf
fi

code-server --auth password