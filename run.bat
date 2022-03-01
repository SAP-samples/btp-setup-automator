docker container stop   "btp-setup-automator"
docker container rm  -f "btp-setup-automator"
docker image     rmi -f "btp-setup-automator"

docker image     build -t btp-setup-automator:latest -f .\config\containerdefinitions\btp-setup-automator\Dockerfile .
docker container run   --rm  -it -d --name btp-setup-automator btp-setup-automator