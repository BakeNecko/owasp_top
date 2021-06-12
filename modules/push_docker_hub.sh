docker build -t bakenecko/owasp1:latest owasp1
docker build -t bakenecko/owasp2:latest owasp2
docker build -t bakenecko/owasp3:latest owasp3
docker build -t bakenecko/owasp4:latest owasp4
docker build -t bakenecko/owasp6:latest owasp6
docker build -t bakenecko/owasp7:latest owasp7

docker push bakenecko/owasp1:latest
docker push bakenecko/owasp2:latest
docker push bakenecko/owasp3:latest
docker push bakenecko/owasp4:latest
docker push bakenecko/owasp6:latest
docker push bakenecko/owasp7:latest
