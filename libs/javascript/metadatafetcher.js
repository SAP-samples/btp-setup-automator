'use strict';

const { createTokenAuth } = require("@octokit/auth-token");
const fetch = require('node-fetch');
const fs = require('node:fs');
const { mkdir } = require('node:fs/promises');
const {join} = require('node:path');
const { request } = require("@octokit/request");

async function createDirIfNotExisting(dirPath) {

    if (!fs.existsSync(dirPath)) {

        await mkdir(dirPath);

    }
}

async function getContent() {

    const sourcePath = join(process.env["METADATA_SOURCE_PATH"], process.env["METADATA_SOURCE_VERSION"]);
    const targetPath = process.env["METADATA_TARGET_PATH"];

    const result = await getContentFromGitHub(sourcePath);

    await storeResultInRepo(result, targetPath);
}

async function getContentFromGitHub(sourcePath) {

    const pat = process.env["METADATA_READ_TOKEN"];
    const owner = "btp-setup-automator";
    const repo = "btp-metadata-fetcher";

    const auth = createTokenAuth(pat);
    const authentication = await auth();

    const result = await request('GET /repos/{owner}/{repo}/contents/{path}', {
        headers: {
            authorization: `${authentication.type} ${authentication.token}`,
        },
        owner: owner,
        repo: repo,
        path: sourcePath
    });

    return result;

}

async function handleDirResult(resultEntry, targetPath) {

    const dirPath = join(targetPath, 'services');

    await createDirIfNotExisting(dirPath);

    const result = await getContentFromGitHub(resultEntry.path);

    await storeResultInRepo(result, dirPath);

}

async function handleFileResult(resultEntry, basePath) {

    let fileName = resultEntry.name;
    const downloadUrl = resultEntry.download_url;

    if (basePath !== "") {
        fileName = join(basePath, fileName);
    }

    const fileDownload = await fetch(downloadUrl);

    const writeStream = fs.createWriteStream(fileName);

    await new Promise((resolve, reject) => {
        fileDownload.body.pipe(writeStream);
        fileDownload.body.on("error", reject);
        writeStream.on("finish", resolve);
    });
}

async function storeResultInRepo(result, targetPath) {

    const typeFile = "file";
    const typeDir = "dir";


    for (let resultEntry of result.data) {

        if (resultEntry.type === typeFile) {

            await handleFileResult(resultEntry, targetPath);

        }
        else if (resultEntry.type === typeDir) {

            await handleDirResult(resultEntry, targetPath);

        }

    }

}

// Starter of function
(async () => { await getContent(); })()
