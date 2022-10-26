## sapsystemname Type

`string` ([ABAP System ID](btpsa-usecase-properties-services-items-allof-1-then-allof-0-then-allof-0-then-properties-parameters-properties-abap-system-id.md))

## sapsystemname Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(?!ADD|ALL|AMD|AND|ANY|ARE|ASC|AUX|AVG|BIT|CDC|COM|CON|DBA|END|EPS|FOR|GET|GID|IBM|INT|KEY|LOG|LPT|MAP|MAX|MIN|MON|NIX|NOT|NUL|OFF|OLD|OMS|OUT|PAD|PRN|RAW|REF|ROW|SAP|SET|SGA|SHG|SID|SQL|SUM|SYS|TMP|TOP|UID|USE|USR|VAR)[A-Z][A-Z0-9]{2}$
```

[try pattern](https://regexr.com/?expression=%5E\(%3F!ADD%7CALL%7CAMD%7CAND%7CANY%7CARE%7CASC%7CAUX%7CAVG%7CBIT%7CCDC%7CCOM%7CCON%7CDBA%7CEND%7CEPS%7CFOR%7CGET%7CGID%7CIBM%7CINT%7CKEY%7CLOG%7CLPT%7CMAP%7CMAX%7CMIN%7CMON%7CNIX%7CNOT%7CNUL%7COFF%7COLD%7COMS%7COUT%7CPAD%7CPRN%7CRAW%7CREF%7CROW%7CSAP%7CSET%7CSGA%7CSHG%7CSID%7CSQL%7CSUM%7CSYS%7CTMP%7CTOP%7CUID%7CUSE%7CUSR%7CVAR\)%5BA-Z%5D%5BA-Z0-9%5D%7B2%7D%24 "try regular expression with regexr.com")

## sapsystemname Default Value

The default value is:

```json
"H01"
```
