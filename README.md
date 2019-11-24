# ymir

> Ymir Labs Handwriting Recognition

This project is built using Nuxt JS(Vue Framework) as frontend, Python/Flask as backend and MongoDB as database
## Build Setup

### Vue Frontend

``` bash
# install dependencies
$ npm run install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```
For detailed explanation on how things work, checkout [Nuxt.js docs](https://nuxtjs.org).

### Python Backend (v3.6)

``` bash
pip install google-cloud-storage
pip install google-cloud-vision
pip install flask
pip install flask-cors
pip install pymongo
python service.py

```

## Assumptions and Simplification

It is assumed that an image file will be uploaded always, hence file type checking is not implemented. Also assumed an image file with some handwritten texts will be uploaded.

## Screenshots

Screenshots are provided in the "screenshots" folder.