# filter and project

using project to only list array elements that match condition

https://studio3t.com/knowledge-base/articles/filter-elements-from-mongodb-arrays/#how-to-use-elemmatch


find
```
{
   "$match" : {
       "stock" : {
          "$elemMatch" : {
             "$and" : [
                { "country" : "01" },
                { "warehouse.code" : "02" }
             ]
          }
       },
   }
}
```

project
```
{
   "$project" : {
       "article_code" : 1, "description" : 1,
       "stock" : {
          "$filter" : {
             "input" : "$stock",
             "as" : "stock",
             "cond" : {
                "$and" : [
                   { "$eq" : [ "$$stock.country", "01" ] },
                   { "$eq" : [ "$$stock.warehouse.code", "02" ] }
                ]
             }
          }
       }
   }
}
```

aggregate
```
db.articles.aggregate([
{
   "$match" : {
       "stock" : {
          "$elemMatch" : {
             "$and" : [
                { "country" : "01" },
                { "warehouse.code" : "02" }
             ]
          }
       },
   }
},
{
   "$project" : {
       "article_code" : 1, "description" : 1,
       "stock" : {
          "$filter" : {
             "input" : "$stock",
             "as" : "stock",
             "cond" : {
                "$and" : [
                   { "$eq" : [ "$$stock.country", "01" ] },
                   { "$eq" : [ "$$stock.warehouse.code", "02" ] }
                ]
             }
          }
       }
   }
}
])
```
