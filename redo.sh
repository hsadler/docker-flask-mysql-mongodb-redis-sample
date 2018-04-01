
rm -rf mongo/ && rm -rf mysql/ && rm -rf redis/ && \

docker-compose up --build --force-recreate --remove-orphans \
--abort-on-container-exit
