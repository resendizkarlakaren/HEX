

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|Symbol|Name|Type|Function|Formal use|Status|
|λ|Lambda|Operator|Transformation|λ(x) → x′|Core|
|→|Arrow|Relation|Trajectory|x → y|Core|
|Δ|Difference|Operator|Produces/marks difference|Δ(x,y)|Core|
|′|Prime|Modifier|Post-transformation state|x → x′|Core|
|NULL|Null|Condition|Contextual indeterminacy|NULL(x \| C)|Core|

|        |                |           |             |                           |                                    |        |
| ------ | -------------- | --------- | ----------- | ------------------------- | ---------------------------------- | ------ |
| Symbol | Meaning        | Type      | Domain      | Operation                 | Constraints                        | Status |
| λ      | Transformation | Operator  | Composition | transforms x              | must produce observable difference | Core   |
| Δ      | Difference     | Operator  | Relation    | distinguishes x,y         | requires relational context        | Core   |
| NULL   | Indeterminacy  | Condition | Context     | marks non-determinability | ≠ inexistence                      | Core   |
