## eviction\_policy Type

`string`

## eviction\_policy Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"allkeys-lru"`     |             |
| `"volatile-lru"`    |             |
| `"allkeys-lfu"`     |             |
| `"volatile-lfu"`    |             |
| `"allkeys-random"`  |             |
| `"volatile-random"` |             |
| `"volatile-ttl"`    |             |
| `"noeviction"`      |             |

## eviction\_policy Default Value

The default value is:

```json
"noeviction"
```
