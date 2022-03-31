import os


def writeKubeConfigFileToDefaultDir(kubeconfigFileString):
    # Default location for kubeconfig files see https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
    # Check whether the specified path exists or not
    path = "/home/user/.kube/"

    isPathExisting = os.path.exists(path)

    if not isPathExisting:
        # Create a new directory because it does not exist
        os.makedirs(path)

    filename = "config"
    fullPath = os.path.join(path, filename)
    fileWriter = open(fullPath, "w")

    fileWriter.write(kubeconfigFileString)

    fileWriter.close()
