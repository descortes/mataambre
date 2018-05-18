Mataambre
=========


Ejecutar mataambre con gunicorn

```
./start.sh 8000
```

---
### Test


```
curl localhost:8000/ping
curl localhost:8000/sleep/{seg}
curl localhost:8000/fibo/{num}
```


---
#### Links
* [gunicorn](http://docs.gunicorn.org/en/stable/index.html)
* [flask](flask.pocoo.org)
* [nginx](https://docs.nginx.com/nginx/admin-guide/)
