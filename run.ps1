#!/usr/bin/pwsh
Param(
    [Parameter(Mandatory=$False)]
    [bool]$RunReleaseFromRegistry = $False,
    [bool]$RunDevFromRegistry = $False
)

Write-Host "Cleaning up containers and images (if existing)" -ForegroundColor green
docker container stop   "btp-setup-automator"
docker container rm  -f "btp-setup-automator"
docker image     rm  -f "btp-setup-automator"

if ( $RunReleaseFromRegistry -eq $True )
{
    Write-Host "Pulling container image RELEASE from registry ..." -ForegroundColor green
    docker pull ghcr.io/sap-samples/btp-setup-automator:latest 

    Write-Host "Starting the container as 'btp-setup-automator' - Access possible e.g. via VS Code" -ForegroundColor green
    docker container run --rm  -it -d --name "btp-setup-automator" ghcr.io/sap-samples/btp-setup-automator:latest 
}
 
elseif ($RunDevFromRegistry -eq $True) {
    Write-Host "Pulling container image DEV from registry ..." -ForegroundColor green
    docker pull ghcr.io/sap-samples/btp-setup-automator-dev:dev 

    Write-Host "Starting the container as 'btp-setup-automator' - Access possible e.g. via VS Code" -ForegroundColor green
    docker container run --rm  -it -d --name "btp-setup-automator" ghcr.io/sap-samples/btp-setup-automator-dev:dev 
}

else
{
    Write-Host "Building the container image ..." -ForegroundColor green
    docker image build -t btp-setup-automator:latest -f "config/Dockerfile"  .

    Write-Host "Starting the container as 'btp-setup-automator' - Access possible e.g. via VS Code" -ForegroundColor green
    docker container run -e BTPSA_VERSION_GIT="$(git describe --long --tags  --always)" --rm  -it -d --name "btp-setup-automator" "btp-setup-automator" 
}
