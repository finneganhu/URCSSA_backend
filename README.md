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
