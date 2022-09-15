from subprocess import run, PIPE
import logging

log = logging.getLogger(__name__)


def getAllCliVersions():
    log.header("USED CLI TOOLS")
    result = []
    result.append(getVersionBtpCli())
    result.append(getVersionCfCli())
    result.append(getVersionMtaBuildTool())
    result.append(getVersionKubectl())
    result.append(getVersionHelm())

    # get the maximum length of the stored "name" for an entry
    # so that it's printed out in an aligned manner inside the log
    maxLenInfoString = max(len(x.get("name")) for x in result)
    for item in result:
        log.info(item.get("name") + " " * (maxLenInfoString - len(item.get("name"))) + ": " + item.get("version"))
    return result


def getVersionBtpCli():
    command = "btp --version"
    p = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    item = {"name": "BTP CLI", "version": p.stdout.decode().strip()}
    return item


def getVersionCfCli():
    command = "cf --version"
    p = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    item = {"name": "CF CLI", "version": p.stdout.decode().strip()}
    return item


def getVersionMtaBuildTool():
    command = "mbt --version"
    p = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    item = {"name": "MTA Build Tool", "version": p.stdout.decode().strip()}
    return item


def getVersionKubectl():
    command = "kubectl version --short"
    p = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    # As the output from the version is currently piped out through stderr
    # the code checks both (stdout and stderr)
    output = p.stdout.decode().strip().split("\n")
    info = ', '.join(output)
    item = {"name": "kubectl", "version": info}
    return item


def getVersionHelm():
    command = "helm version --template='{{.Version}}'"
    p = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    # As the output from the version is currently piped out through stderr
    # the code checks both (stdout and stderr)
    output = p.stdout.decode().strip()
    item = {"name": "helm", "version": output}
    return item
