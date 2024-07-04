# FastAPI-LINE-notify

It's sample code of [Lotify](https://github.com/louis70109/lotify) by FastAPI.

# LINE Notify singup

Set the Callback URL to `http://YOUR_DOMAIN/callback`, and for local testing, use `http://localhost:8000/callback`


# Local testing

```sh
cp .env.sample .env
uvicorn main:app --host=0.0.0.0 --port=8000
```

or

```dockerfile
cp .env.sample .env
docker-compose up
```

> Choose one of the two methods.

# Step

### [LINE Notify](https://notify-bot.line.me/) Basic settings
![](https://i.imgur.com/gOiuuM7.png)

---

### Initial page

After opening the browser and entering `http://localhost:8000` , you will see an input button.

![](https://i.imgur.com/L6bBRKq.png)

---

### Bind notifications - Select`1-on-1 chat reception(1對1聊天接收)`
![](https://i.imgur.com/TApZVFt.png)

---

### Integration complete
At this point, LINE Notify will send a notification indicating that the binding was successful.

![](https://i.imgur.com/pXP6DIS.png)

---

### Web example
At the same time, the browser will be redirected to `/notify/check` with the code and state information included.
![](https://i.imgur.com/hO6tfU0.png)

---

### Test content

![](https://i.imgur.com/9yxI3zq.png)
---

# Route

- GET /
  - User clicks on the binding screen.
- GET /callback
  - The callback route after LINE Notify settings and authentication completion.
- Route for sending push notifications (due to[CORS issues](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS), an API is needed to forward the requests).
    - POST /notify/send
    - POST /notify/send_sticker
    - POST /notify/send_url
    - POST /notify/send_path
    - POST /notify/revoke

# License

[MIT](https://github.com/divazone/fastapi-line-notify/blob/master/LICENSE)
