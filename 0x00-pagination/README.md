# Pagination

Pagination is the process of dividing a large list of items into smaller chunks (or "pages") to make it easier to display in a user interface. For example, think of a website that shows search results across multiple pages, where each page has a certain number of results.


Pagination allows you to retrieve data (REST resources) in an efficient way that doesn't strain the backend or frontend. More specifically, it allows you to partition data into digestible segments. This helps ensures smooth data transactions, which prevents server strain and enhances client experiences.

Most endpoints that returns a list of entities will need to have some sort of pagination.

Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic.
## Types of pagination

- Offset Pagination
- Keyset Pagination
- Seek Pagination

## Learning Objectives

- [x] How to paginate a dataset with simple page and page_size parameters
- [x] How to paginate a dataset with hypermedia metadata
- [x] How to paginate in a deletion-resilient manner

### Setup: `Popular_Baby_Names.csv`
use this data file for your project
```csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Hannah,56,8
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Grace,54,9
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Angela,54,9
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Ava,53,10

... 
```
