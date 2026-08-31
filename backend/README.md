# Rotas para testar


### User - POST / GET 

```
http://localhost:8000/api/user/
```

```
{
  "name": "a"
}
```

### Login - POST

```
http://localhost:8000/api/login/teste/
```

### Room - POST / GET

```
http://localhost:8000/api/room/
```

```
{
  "name": "sala-de-teste",
  "creator": "teste",
  "users": ["a", "b"]
}
```

### Room User List - GET

```
http://localhost:8000/api/room/?creator=teste
```

### Room Add User - POST

```
http://localhost:8000/api/room/sala-de-teste/users/
```

```
{
  "name": "c"
}
```