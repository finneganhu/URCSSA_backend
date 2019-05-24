# URCSSA_backend

This is a self-test project for the backend of URCSSA official website.

## Structure of DynamoDB Table
* Professor
    * Department (Partition Key)
    * Name (Sort Key)
    * Info:
        * Gender
        * Email
        * ...
    * Evaluations:
        * (eval1):
            * Class
            * Rating
            * Comments
        * (eval2):
            * Class
            * Rating
            * Comments
        * ...

## Currently Supported API
* `create`
    - **function**: create a new professor item with given Department and Name
    - **method**: `POST`
    - **path**: `/`
    - **request body**: Department, Name, (Info)
* `delete`
    - **function**: delete a new professor item with given Department and Name
    - **method**: `DELETE`
    - **path**: `/{department}/{name}`
    - **request body**:
* `getProf`
    - **function**: get a specific professor item with given Department and Name
    - **method**: `GET`
    - **path**: `/{department}/{name}`
    - **request body**:
* `getProfs`
    - **function**: query all professor items in the given Department
    - **method**: `GET`
    - **path** `/{department}`
    - **request body**:
* `list`
    - **function**: scan through the database and list all professor items
    - **method**: `GET`
    - **path**: `/`
    - **request body**:
* `update`
    - **function**: update comments to a specific professor item given Department and Name
    - **method**: `PATCH`
    - **path**: `/{department}/{name}`
    - **request body**: Class, Rating, Comments
