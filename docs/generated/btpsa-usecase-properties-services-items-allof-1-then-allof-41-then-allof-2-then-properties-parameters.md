## parameters Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters.md))

# parameters Properties

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                          |
| :---------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [consortium](#consortium)                             | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-consortium.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/consortium")                             |
| [ordererAdmin](#ordereradmin)                         | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-ordereradmin.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/ordererAdmin")                         |
| [ordererOrg](#ordererorg)                             | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-ordererorg.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/ordererOrg")                             |
| [ordererTlsCaCertificate](#orderertlscacertificate)   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-orderertlscacertificate.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/ordererTlsCaCertificate")   |
| [orderers](#orderers)                                 | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-orderers.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/orderers")                                 |
| [peerAdmin](#peeradmin)                               | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peeradmin.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerAdmin")                               |
| [peerCaCertificate](#peercacertificate)               | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peercacertificate.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerCaCertificate")               |
| [peerCertificateAuthority](#peercertificateauthority) | `object` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peercertificateauthority.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerCertificateAuthority") |
| [peerOrg](#peerorg)                                   | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peerorg.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerOrg")                                   |
| [peerTlsCaCertificate](#peertlscacertificate)         | `string` | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peertlscacertificate.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerTlsCaCertificate")         |
| [peers](#peers)                                       | `array`  | Optional | cannot be null | [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peers.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peers")                                       |

## consortium

name of the consortium

`consortium`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-consortium.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/consortium")

### consortium Type

`string`

### consortium Default Value

The default value is:

```json
"< name of the consortium >"
```

## ordererAdmin

(optional) orderer admin user

`ordererAdmin`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-ordereradmin.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-ordereradmin.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/ordererAdmin")

### ordererAdmin Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-ordereradmin.md))

### ordererAdmin Default Value

The default value is:

```json
{
  "certificate": "< (optional) orderer user certificate> ",
  "key": "< (optional) orderer user key >"
}
```

## ordererOrg

orderer org name

`ordererOrg`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-ordererorg.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/ordererOrg")

### ordererOrg Type

`string`

### ordererOrg Default Value

The default value is:

```json
"< (optional) orderer org name >"
```

## ordererTlsCaCertificate

TLS CA certificate of the orderer org

`ordererTlsCaCertificate`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-orderertlscacertificate.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/ordererTlsCaCertificate")

### ordererTlsCaCertificate Type

`string`

### ordererTlsCaCertificate Default Value

The default value is:

```json
"< TLS CA certificate of the orderer org >"
```

## orderers

orderer urls

`orderers`

*   is optional

*   Type: `array`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-orderers.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/orderers")

### orderers Type

`array`

### orderers Default Value

The default value is:

```json
[
  "< (optional) orderer url:port >"
]
```

## peerAdmin

peer admin user

`peerAdmin`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peeradmin.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peeradmin.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerAdmin")

### peerAdmin Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peeradmin.md))

### peerAdmin Default Value

The default value is:

```json
{
  "certificate": "< peer user certificate> ",
  "key": "< peer user key >"
}
```

## peerCaCertificate

peer ca certificate

`peerCaCertificate`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peercacertificate.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerCaCertificate")

### peerCaCertificate Type

`string`

### peerCaCertificate Default Value

The default value is:

```json
"< (optional) peer ca certificate >"
```

## peerCertificateAuthority

(optional) certificate authority of peer admin user

`peerCertificateAuthority`

*   is optional

*   Type: `object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peercertificateauthority.md))

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peercertificateauthority.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerCertificateAuthority")

### peerCertificateAuthority Type

`object` ([Details](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peercertificateauthority.md))

### peerCertificateAuthority Default Value

The default value is:

```json
{
  "certificate": "< (optional) certificate authority certificate> ",
  "certificateChain": "< (optional) certificate authority certificate chain >",
  "key": "< (optional) certificate authority private key >"
}
```

## peerOrg

peer org name

`peerOrg`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peerorg.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerOrg")

### peerOrg Type

`string`

### peerOrg Default Value

The default value is:

```json
"< peer org name >"
```

## peerTlsCaCertificate

TLS CA certificate of the peer org

`peerTlsCaCertificate`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peertlscacertificate.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peerTlsCaCertificate")

### peerTlsCaCertificate Type

`string`

### peerTlsCaCertificate Default Value

The default value is:

```json
"< TLS CA certificate of the peer org >"
```

## peers

peer urls

`peers`

*   is optional

*   Type: `array`

*   cannot be null

*   defined in: [JSON Schema for BTPSA use case definitions](btpsa-usecase-properties-services-items-allof-1-then-allof-41-then-allof-2-then-properties-parameters-properties-peers.md "undefined#/properties/services/items/allOf/1/then/allOf/41/then/allOf/2/then/properties/parameters/properties/peers")

### peers Type

`array`

### peers Default Value

The default value is:

```json
[
  "< peer url:port >"
]
```
