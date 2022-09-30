@echo off
setlocal
call :setESC

echo %ESC%[32mCleaning up containers and images (if existing)%ESC%[0m
docker container stop   "btp-setup-automator"
docker container rm  -f "btp-setup-automator"
docker image     rm  -f "btp-setup-automator"


if not "%1" == "RunFromRegistry" (
  
  echo %ESC%[32mBuilding the container image ...%ESC%[0m
  docker image     build -t btp-setup-automator:latest -f .\config\Dockerfile .

  echo %ESC%[32mStart the container as 'btp-setup-automator' - Access possible e.g. via VSCode%ESC%[0m
  docker container run -e BTPSA_VERSION_GIT="$(git describe --long --tags  --always)" --rm  -it -d --name btp-setup-automator btp-setup-automator

) else (

  echo %ESC%[32mPulling container image from registry ...%ESC%[0m
  docker pull ghcr.io/sap-samples/btp-setup-automator:main

  echo %ESC%[32mStart the container as 'btp-setup-automator' - Access possible e.g. via VSCode%ESC%[0m
  docker container run --rm  -it -d --name btp-setup-automator ghcr.io/sap-samples/btp-setup-automator:main

)

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0
