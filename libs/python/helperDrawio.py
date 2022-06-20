import zlib
import base64
import sys
import requests
import os
import xml.etree.ElementTree as ET
from urllib.parse import unquote
import xmltodict
import logging

log = logging.getLogger(__name__)


def getUseCaseDataFromDrawIoFile(filename):
    result = None
    rawData = None

    try:
        if "http://" in filename or "https://" in filename:
            rawData = requests.get(filename)
        else:
            if os.path.isfile(filename):
                # open text file in read mode
                f = open(filename, "r")
                rawData = f.read()

        if rawData is not None:
            tree = ET.fromstring(rawData.text)
            compressed = tree.attrib.get("compressed")
            myDict = None
            if compressed == "true":
                data = base64.b64decode(tree.find('diagram').text)
                rawXml = zlib.decompress(data, wbits=-15)
                xmlData = unquote(rawXml)
                myDict = xmltodict.parse(xmlData)

                objectModel = myDict.get("mxGraphModel")
                if objectModel.get("root") and objectModel.get("root").get("object") and objectModel.get("root").get("object").get("@btpsa-usecase"):
                    result = objectModel.get("root").get("object").get("@btpsa-usecase")
        else:
            log.error("can't read the draw.io file >" + filename + "<. As of now only compressed draw.io files are accepted.")
            sys.exit(os.EX_DATAERR)
    except Exception as e:
        log.error("please check the draw.io file >" + filename + "<: " + str(e))
        sys.exit(os.EX_DATAERR)

    return result
