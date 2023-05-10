## eviction\_policy Type

`string`

## eviction\_policy Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"allkeys-lfu"`     |             |
| `"allkeys-lru"`     |             |
| `"allkeys-random"`  |             |
| `"noeviction"`      |             |
| `"volatile-lfu"`    |             |
| `"volatile-lru"`    |             |
| `"volatile-random"` |             |
| `"volatile-ttl"`    |             |

## eviction\_policy Default Value

The default value is:

```json
"noeviction"
```
