Public Code Servers - An implementation of [Code Server](https://github.com/coder/code-server)
=================

Access a version of VS Code on the web with a bunch of extra features and integrations.

![](https://files.mcaq.me/5052j.png)

Uses [Code Server](https://github.com/coder/code-server) while also providing:

- One-click install using [SharpCD](https://github.com/Sharpz7/sharpcd)
- Automatic HTTPS using [Sharpnet](https://github.com/Sharpz7/sharpnet)
- Automatic Google Auth using [Vouch](https://github.com/vouch/vouch-proxy)


Current Included Features
=================
- ZSH and Oh-My-ZSH
- SharpCD and Sharpdev
- Neofetch
- Everything in /home/coder stored in a docker volume
- Docker and docker-compose installed
- Fira Code font installed

Current Languages
=================
- Golang
- Python
- Julia
- PHP
- Typescript
- Rust
- Elixir


Installation
=================

- Make sure [SharpCD](https://github.com/Sharpz7/sharpcd) havs been installed.


**Installing Dependencies**

- Ensure the enviromental variables have been set in an enviromental variable file:

```env
OAUTH_PROVIDER=google
# Set by google
OAUTH_CALLBACK_URLS=${CALLBACK_URL}
OAUTH_CLIENT_ID=${VOUCHID}
OAUTH_CLIENT_SECRET=${VOUCHSECRET}

ADMIN_EMAIL=mygmail@gmail.com
# domain vouch proxy will be hosted on
DOMAINS=mydomain.com

#====================

# sharpnet ports
HTTP_PORT=80
HTTPS_PORT=443

# Sharpnet gmail login credentials
# for sending errors
MAILPASS=email_password
SENDER_EMAIL=email

# Email that problems will be sent to
RECEIVER_EMAIL=email@domain1.com

# Domain for certificates
DOMAIN=domain2.com

# For Devs only
DEV=FALSE
NETWORK=sharpnet
```

**(Note that VOUCH OAuth could be changed to another provider, please see [Vouch Proxy](https://github.com/vouch/vouch-proxy))**

- Run the following command to install the dependencies:

```bash
sharpcd --remotefile https://raw.githubusercontent.com/Sharpz7/vouch/main/.sharpcd/dependencies.sharpcd.yml
```

**Installing a Codeserver**

- Ensure the enviromental variables have been set in an enviromental variable file:

- Use the $VERSION variable to set the version of Code Server you want to install.

```env
CODESERVER_PASS=<password>
VERSION=<version>
```

- Run the following command to install Code Server:

```bash
sharpcd --remotefile https://raw.githubusercontent.com/Sharpz7/vouch/main/.sharpcd/sharpcd.yml
```