'use strict'

const { createTokenAuth } = require('@octokit/auth-token')
const fetch = require('node-fetch')
const fs = require('node:fs')
const { join } = require('node:path')
const { request } = require('@octokit/request')
const path = require('path')

async function getContent () {
  const targetConfigFolder = process.env.METADATA_TARGET_CONFIG_FOLDER
  const targetBaseFolder = process.env.METADATA_TARGET_BASE_FOLDER
  const version = process.env.METADATA_VERSION
  const folder = process.env.METADATA_FOLDER

  const sourcePath = join(version, folder)
  const targetPath = path.resolve(__dirname, '..', '..', targetConfigFolder, targetBaseFolder, version, folder)

  const result = await getContentFromGitHub(sourcePath)

  await storeResultInRepo(result, targetPath)
}

async function getContentFromGitHub (sourcePath) {
  const pat = process.env.METADATA_READ_TOKEN
  const owner = process.env.METADATA_SOURCE_OWNER
  const repo = process.env.METADATA_SOURCE_REPO

  const auth = createTokenAuth(pat)
  const authentication = await auth()

  console.log(`Fetching data from GitHub repo ${owner}/${repo}`);
  const result = await request('GET /repos/{owner}/{repo}/contents/{path}', {
    headers: {
      authorization: `${authentication.type} ${authentication.token}`
    },
    owner,
    repo,
    path: sourcePath
  })

  return result
}

async function handleDirResult (resultEntry, targetPath) {
  const result = await getContentFromGitHub(resultEntry.path)

  await storeResultInRepo(result, targetPath)
}

async function handleFileResult (resultEntry, basePath) {
  let fileName = resultEntry.name
  const downloadUrl = resultEntry.download_url

  if (basePath !== '') {
    fileName = join(basePath, fileName)
  }

  const fileDownload = await fetch(downloadUrl)

  console.log(`Writing file ${fileName}`)
  const writeStream = fs.createWriteStream(fileName)

  await new Promise((resolve, reject) => {
    fileDownload.body.pipe(writeStream)
    fileDownload.body.on('error', reject)
    writeStream.on('finish', resolve)
  })
}

async function storeResultInRepo (result, targetPath) {
  const typeFile = 'file'
  const typeDir = 'dir'

  for (const resultEntry of result.data) {
    if (resultEntry.type === typeFile) {
      await handleFileResult(resultEntry, targetPath)
    } else if (resultEntry.type === typeDir) {
      await handleDirResult(resultEntry, targetPath)
    }
  }
}

// Starter of function
(async () => { await getContent() })()
