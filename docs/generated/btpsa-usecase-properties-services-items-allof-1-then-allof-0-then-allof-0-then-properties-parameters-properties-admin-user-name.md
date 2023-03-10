## admin\_user\_name Type

`string` ([Admin User Name](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-admin-user-name.md))

## admin\_user\_name Constraints

**maximum length**: the maximum number of characters for this string is: `40`

**minimum length**: the minimum number of characters for this string is: `0`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?!SAP_|_)[\.A-Z0-9_-]{0,40}$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F!SAP_%7C_\)%5B%5C.A-Z0-9_-%5D%7B0%2C40%7D%24 "try regular expression with regexr.com")
