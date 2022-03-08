##################################################################################################################################################
# LICENSE
# This Dockerfile is provided under the LICENSE defined in the Github repository
# at https://github.com/SAP-samples/btp-setup-automator
##################################################################################################################################################
# STARTING WITH ALL THE SAP TOOLS FIRST
##################################################################################################################################################
FROM alpine:3 AS base

ENV ARCH=linux-amd64
ENV TOOLS_URL=tools.hana.ondemand.com
ENV CPCLI_URL=cpcli.cf.eu10.hana.ondemand.com

## Install necessary packages to donwload and install tools
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk upgrade \
    && apk add --no-cache curl jq \
    && update-ca-certificates

##########################################################################################
# Retrieve the CloudFoundry CLI (version 7.4.0)
##########################################################################################
FROM base AS cf_cli
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
WORKDIR /tmp/tools
RUN CF_CLI_VERSION="7.4.0" \
    && wget --quiet -O download.tgz "https://packages.cloudfoundry.org/stable?release=linux64-binary&version=$CF_CLI_VERSION&source=github-rel" \
    && tar -xzf download.tgz -C .

##########################################################################################
## Retrieve the BTP CLI
## Latest is always at https://tools.hana.ondemand.com/additional/btp-cli-linux-amd64-latest.tar.gz
## Currently we look at https://cpcli.cf.eu10.hana.ondemand.com/actuator/info to find out what the
## latest supported version on the server side is and use that, specifically.
##########################################################################################
FROM base AS btp_cli
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
WORKDIR /tmp/tools
#RUN BTP_CLI_VERSION="$(curl --silent --url "https://$CPCLI_URL/actuator/info" | jq --raw-output '.app.version')" \
RUN BTP_CLI_VERSION="2.18.0" \
  && curl --fail --silent --location --cookie eula_3_1_agreed="$TOOLS_URL/developer-license-3_1.txt" \
    --url "https://$TOOLS_URL/additional/btp-cli-$ARCH-$BTP_CLI_VERSION.tar.gz" \
    | tar -xzf - --strip-components 1 "$ARCH/btp"

########################################################################################
# Retrieve the MTA build tool
########################################################################################
FROM base AS mta_build_tool
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
WORKDIR /tmp/tools
RUN MBT_VERSION="1.2.8" \
  && curl --fail --silent --location --url "https://github.com/SAP/cloud-mta-build-tool/releases/download/v${MBT_VERSION}/cloud-mta-build-tool_${MBT_VERSION}_Linux_amd64.tar.gz" \
    | tar -xzf - mbt

########################################################################################
# Retrieve the CF plugin MTA (needed for Apple machines with M1 chip)
# The necessary plugin will be built from the sources and copied over to the final
# image.
########################################################################################
FROM golang:alpine as cf_plugin_multiapps
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
WORKDIR /tmp/tools
RUN apk update upgrade \
&& apk add --no-cache bash git \
&& git clone "https://github.com/cloudfoundry/multiapps-cli-plugin"  multiapps-cli-plugin \
&& cd multiapps-cli-plugin \
&&  go mod download code.cloudfoundry.org/bytefmt \
&& go get github.com/cloudfoundry-incubator/multiapps-cli-plugin/commands \
&& ./build.sh \
&& cd build \
&& mv multiapps-plugin-static.linux64 /tmp/tools \
&& cd /tmp/tools \
&& rm -rf multiapps-cli-plugin

########################################################################################
# Bring the tools together into the final base stage
########################################################################################
FROM alpine:3 as tools
WORKDIR /usr/local/bin
COPY --from=cf_cli                 /tmp/tools/ .
COPY --from=btp_cli                /tmp/tools/ .
COPY --from=mta_build_tool         /tmp/tools/ .
COPY --from=cf_plugin_multiapps    /tmp/tools/ .

##################################################################################################################################################
# Now putting all pieces together 
##################################################################################################################################################

FROM python:3.9.9-alpine3.15 AS final_build
ENV USERNAME=user
ENV HOME_FOLDER /home/$USERNAME

ENV LIBS_FOLDER $HOME_FOLDER/libs
ENV CONTAINER_NAME=btp-setup-automator
COPY config/python/requirements.txt /tmp/pip-tmp/requirements.txt

# Add config folders according to https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
ENV XDG_CONFIG_HOME=$HOME_FOLDER/.config
ENV XDG_DATA_HOME=$HOME_FOLDER/.local/share
ENV XDG_STATE_HOME=$HOME_FOLDER/.local/state

ENV CF_HOME=$XDG_CONFIG_HOME/cf
ENV BTP_CLIENTCONFIG=$XDG_CONFIG_HOME/btp/config.json

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$HOME_FOLDER" \
    --no-create-home \
    "$USERNAME" \
    && apk update \
    && apk upgrade \
    && apk add --no-cache \
               bash \
               coreutils \
               git \
               make \
               nodejs \
               npm \
    && pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp \
    ## Set the right timezone in the container image
    && cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
##########################################################################################
# Install CAP CDS
##########################################################################################
    && npm install -g @sap/cds-dk --allow-root \
    && npm cache clean --force

##########################################################################################
# Fill the image with the necessary resources
##########################################################################################
USER $USERNAME
WORKDIR $HOME_FOLDER

## Copy all necessary executables from the tools stage
COPY --chown=root:root --from=tools /usr/local/bin/cf  /usr/local/bin
COPY --chown=root:root --from=tools /usr/local/bin/cf7  /usr/local/bin
COPY --chown=root:root --from=tools /usr/local/bin/btp /usr/local/bin
COPY --chown=root:root --from=tools /usr/local/bin/mbt /usr/local/bin
COPY --chown=root:root --from=tools /usr/local/bin/multiapps-plugin-static.linux64 /usr/local/bin

## Install the CF plugin for deploying MTAs on Cloudfoundry
RUN cf install-plugin -f https://github.com/cloudfoundry-incubator/multiapps-cli-plugin/releases/latest/download/multiapps-plugin.linux32 
#RUN cf install-plugin -f /usr/local/bin/multiapps-plugin-static.linux64

## Copy over the all necessary resources
COPY --chown=$USERNAME:$USERNAME usecases/                                  $HOME_FOLDER/usecases/

COPY --chown=$USERNAME:$USERNAME README.md                                  $HOME_FOLDER/
COPY --chown=$USERNAME:$USERNAME parameters.json                            $HOME_FOLDER/
COPY --chown=$USERNAME:$USERNAME docs                                       $HOME_FOLDER/docs
COPY --chown=$USERNAME:$USERNAME libs/python/btpsa                          $HOME_FOLDER/
COPY --chown=$USERNAME:$USERNAME libs/python/btp_cli.py                     $LIBS_FOLDER/python/
COPY --chown=$USERNAME:$USERNAME libs/python/helper*.py                     $LIBS_FOLDER/python/
COPY --chown=$USERNAME:$USERNAME libs/json/paramBtpSetupAutomator.json      $LIBS_FOLDER/json/

COPY --chown=$USERNAME:$USERNAME .reuse                                     $HOME_FOLDER/.reuse
COPY --chown=$USERNAME:$USERNAME LICENSES                                   $HOME_FOLDER/LICENSES
COPY --chown=$USERNAME:$USERNAME LICENSE                                    $HOME_FOLDER/

# Copy over some vscode settings to install the pyhton plugins
COPY --chown=$USERNAME:$USERNAME .vscode                                    $HOME_FOLDER/.vscode/

# For using outside of VS Code context:
CMD ["bash"]
