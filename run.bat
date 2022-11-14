@echo off
setlocal
call :setESC

echo %ESC%[32mCleaning up containers and images (if existing)%ESC%[0m
docker container stop   "btp-setup-automator"
docker container rm  -f "btp-setup-automator"
docker image     rm  -f "btp-setup-automator"


if "%1" == "RunReleaseFromRegistry" goto release
if "%1" == "RunDevFromRegistry" goto dev

echo %ESC%[32mBuilding the container image ...%ESC%[0m
docker image     build -t btp-setup-automator:latest -f .\config\Dockerfile .
echo %ESC%[32mStarting the container as 'btp-setup-automator' - Access possible e.g. via VS Code%ESC%[0m
docker container run -e BTPSA_VERSION_GIT="$(git describe --long --tags  --always)" --rm  -it -d --name btp-setup-automator btp-setup-automator
goto end

:release
echo %ESC%[32mPulling container image RELEASE from registry ...%ESC%[0m
docker pull ghcr.io/sap-samples/btp-setup-automator:latest
echo %ESC%[32mStarting the container as 'btp-setup-automator' - Access possible e.g. via VS Code%ESC%[0m
docker container run --rm  -it -d --name btp-setup-automator ghcr.io/sap-samples/btp-setup-automator:latest
goto end

:dev
echo %ESC%[32mPulling container image DEV from registry ...%ESC%[0m
docker pull ghcr.io/sap-samples/btp-setup-automator-dev:dev
echo %ESC%[32mStarting the container as 'btp-setup-automator' - Access possible e.g. via VS Code%ESC%[0m
docker container run --rm  -it -d --name btp-setup-automator ghcr.io/sap-samples/btp-setup-automator-dev:dev
goto end

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)

:end
exit /B 0
