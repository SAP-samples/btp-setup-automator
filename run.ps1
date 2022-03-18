#!/usr/bin/pwsh

Write-Host "Cleaning up containers and images (if existing)" -ForegroundColor green
docker container stop   "btp-setup-automator"
docker container rm  -f "btp-setup-automator"
docker image     rmi -f "btp-setup-automator"

Write-Host "Building the container image ..." -ForegroundColor green
docker image build -t btp-setup-automator:latest -f "config/containerdefinitions/btp-setup-automator/Dockerfile"  .

Write-Host "Start the container as 'btp-setup-automator' - Access possible e.g. via VSCode" -ForegroundColor green
docker container run -e BTPSA_VERSION_GIT="$(git describe --long --tags  --always)" --rm  -it -d --name "btp-setup-automator" "btp-setup-automator" 