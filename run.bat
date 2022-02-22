docker stop     "btp-setup-automator"
docker rm -f    "btp-setup-automator"
docker rmi -f   "btp-setup-automator"

docker build -t btp-setup-automator:latest -f .\config\containerdefinitions\btp-setup-automator\Dockerfile .
docker run --rm  -it -d --name btp-setup-automator btp-setup-automator
