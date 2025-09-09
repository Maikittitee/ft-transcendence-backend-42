# HOW TO RUN 

## Setup env
```
echo "DEBUG=false
NGINX_SERVER_NAME=localhost

# User manage
USER_MANAGE_SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxx

# Match Making
MATCH_MAKING_SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxx


# 42OAuth
OAUTH_UID=u-s4t2ud-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
FT_CLIENT_SECRET=s-s4t2ud-xxxxxxxxxxxxxxxxxxxxxxxxxxx
REDIRECT_URI=https://xxxx:xxxx/xxxx"
OAUTH_URL=https://api.intra.42.fr/oauth/authorize?xxxxxxxxxxxxx

# Database
DB_NAME=db1
DB_USER=root
DB_PASSWORD=root" > .env
```

## Run
```
docker-compose up --build
```
make a small change
