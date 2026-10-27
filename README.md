
Егер тексергіңіз келсе, мына командаларды орындаңыз.

## 1. team2-site (сайт)

```
docker run -d -p 8080:80 --name team2-site ayaulymw/team2-site:1.0
```
Браузерде: http://localhost:8080

## 2. team2-db-data (деректер базасы)

```
docker run -d -p 5433:5432 --name team2-db-data ayaulymw/team2-db-data:1.0
docker exec -it team2-db-data psql -U postgres -c "SELECT * FROM students;"
```

## 3. team2-timer (веб-қолданба)

```
docker run -d -p 8081:5000 --name team2-timer ayaulymw/team2-timer:1.0
```
Браузерде: http://localhost:8081

## Тексеріп болған соң тазалау

```
docker rm -f team2-site team2-db-data team2-timer
```
=======
# team2-docker

