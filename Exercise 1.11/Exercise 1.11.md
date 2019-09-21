docker build -t backi .
docker run --name backend -p 8000:8000 backi
docker exec -it backend /bin/bash

root@5f7624904ec2:/app# cat logs.txt

(open localhost:8000 a few times)

root@5f7624904ec2:/app# cat logs.txt
7/12/2019, 2:22:00 PM: Connection received in root
7/12/2019, 2:22:00 PM: Connection received in root
7/12/2019, 2:22:01 PM: Connection received in root
7/12/2019, 2:22:01 PM: Connection received in root
7/12/2019, 2:22:01 PM: Connection received in root