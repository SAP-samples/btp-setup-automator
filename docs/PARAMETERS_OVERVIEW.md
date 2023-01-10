# Overview of btpsa parameters

As we have seen the setup-automator is configured via the `parameters.json` and the `usecase.json` files. These files allow an extensive configuration of the setup-automator. You find the documentation of the possible parameters of the files here:

- `parameters.json`: [Link](./generated/btpsa-parameters.md)
- `usecase.json`: [Link](./generated/btpsa-usecase.md)

*Be ware that the documentation is generated via [JSON Schema Markdown Tools](https://github.com/adobe/jsonschema2md) which gives us some rough edges in the documentation when it comes to the allowed values.*

> 📝 Tip - The `parameters.json` and the `usecase.json` files are backed by a [JSON schema](https://json-schema.org/). This helps you when editing the files via type-ahead support, so no need to have the documentation open side-by-side to check for possible values. Indeed the documentation is generated based on the JSON schemas.

## JSON schemas and IDEs

The `parameters.json` as well as the `usecase.json` files reference the corresponding JSON schemas directly in the code like:

```json
{
  "$schema": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-parameters.json",
  "usecasefile": "usecases/released/default.json",
  ...
}  
```

This ensures that the features and support provided by the schema are available for you, no matter which IDE you are using.

In addition every IDE offers additional approaches to reference a JSON schema for a specific IDE e.g., in [WebStorm](https://www.jetbrains.com/help/webstorm/json.html#ws_json_using_schemas). Using one of the alternatives makes the explicit reference to the JSON schema obsolete.

In case of VS Code the [configuration](https://code.visualstudio.com/docs/languages/json#_mapping-in-the-user-settings) can be done via the `.vscode/settings.json` file in this repository:

```JSON
{
...
"json.schemas": [
        {
            "fileMatch": [
                "*usecase.json"
            ],
            "url": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-usecase.json"
        },
        {
            "fileMatch": [
                "*parameters.json"
            ],
            "url": "https://raw.githubusercontent.com/SAP-samples/btp-setup-automator/main/libs/btpsa-parameters.json"
        }
    ]
}
```

This configuration makes use of the [file match syntax](https://code.visualstudio.com/docs/languages/json#_file-match-syntax) to identify the relevant JSON files. With VS Code and this configuration in place you can omit referencing the JSON schema in your own `parameters.json` and `usecase.json` files.

> ⚠ Note - To stay backwards compatible and support the IDE of your choice we stick to referencing the JSON schema explicitly. The `parameters.json` and `usecase.json` do as of today not consistently adhere to the file name matching needed for the configuration. However feel free to adopt the setup in your personal configurations.
