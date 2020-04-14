# Objectives

## 1. xfail

- Commit branch: `objective_1_xfail`

## 2. adding new endpoint

- Commit branch: `objective_2_endpoint`

## 3. basic front-end integrating with apis

- Commit repo: https://github.com/dasani08/connections_client

## 4. new feature request

### Get relations API SPEC

Gets list of people connected within x degrees of separation to a specific person.

Assume that the data are as follows:

```
A is friend of B
C is friend of B
B is friend of D
E is friend of D
F is friend of E
```

Call `f(id, x)` is the function return a list of connected person within x degress of separation to a person with id

- f(D, 0) will return []
- f(D, 1) will return [B, E]
- f(D, 2) will return [B, E, A, C, F]
- f(D, 3) will return []

**URL:** `/relations`

**Method:** `GET` 

**Params:** 

  person_id: Integer
  
  degree: Integer (The degree should be greater or equal to 1)

#### Sample request

GET `/relations?person_id=1&degree=3`

#### Success Response

**Code:** `200`
**Format:** `JSON`
**Content examples:**

Return a list of person

```json
[
	{
		"id": 1,
		"first_name": "Joe",
		"last_name": "Ham",
		"email": "joe_ham@example.com"
	}
]
```

### Technical challenges

- With current database design, getting list of people connected with a specific person by x degrees of separation requires a lot of database query. That can be done by using union statement of sql or merging the result from each single query for each degree of separation.
	
- Over time, the number of records in database will increase greatly , so the number of records returned will increase accordingly. In addition, aggregating results from single queries will become more expensive.
	
- Query complexity increases with degrees of separation. For example: If person A have 100 connected people, number of people connected with A at level 3 of degree of separation will be:
		N = distinct of (100^1 + 100^2 + 100^3)

### Approach

- We can transform current database structure into graph model. It looks like a directed unweighted graph. Research and choosing a graph database will be good approach for this feature. Replacing a relational database by graph database costs much efforts and risks for the projec. If the project still in initial phase or research and development phase, we can dive in with graph db for find an optimal solution for this feature. 

### Concerns

1. Do we need to return path of a connection (A -> B -> ... -> Target) or only list of people within x degrees of separation?
2. How many levels of separation will be used?

