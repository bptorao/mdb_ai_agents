# Data dictionary

## actor

`actor_id`: A surrogate primary key used to uniquely identify each actor in the table.

`first_name`: The actor first name.

`last_name`: The actor last name.

`last_update`: When the row was created or most recently updated.


## address

`address_id`: A surrogate primary key used to uniquely identify each address in the table.

`address`: The first line of an address.

`address2`: An optional second line of an address.

`district`: The region of an address, this may be a state, province, prefecture, etc.

`city_id`: A foreign key pointing to the city table.

`postal_code`: The postal code or ZIP code of the address (where applicable).

`phone`: The telephone number for the address.

`last_update`: When the row was created or most recently updated.

`location`: A Geometry column with a spatial index on it.


## category

`category_id`: A surrogate primary key used to uniquely identify each category in the table.

`name`: The name of the category.

`last_update`: When the row was created or most recently updated.


## city

`city_id`: A surrogate primary key used to uniquely identify each city in the table.

`city`: The name of the city.

`country_id`: A foreign key identifying the country that the city belongs to.

`last_update`: When the row was created or most recently updated.


## country

`country_id`: A surrogate primary key used to uniquely identify each country in the table.

`country`: The name of the country.

`last_update`: When the row was created or most recently updated.

## customer

`customer_id`: A surrogate primary key used to uniquely identify each customer in the table.

`store_id`: A foreign key identifying the customer “home store.” Customers are not limited to renting only from this store, but this is the store at which they generally shop.

`first_name`: The customer first name.

`last_name`: The customer last name.

`email`: The customer email address.

`address_id`: A foreign key identifying the customer address in the address table.

`active`: Indicates whether the customer is an active customer. Setting this to FALSE serves as an alternative to deleting a customer outright. Most queries should have a WHERE active = TRUE clause.

`create_date`: The date the customer was added to the system. This date is automatically set using a trigger during an INSERT.

`last_update`: When the row was created or most recently updated.


## film

`film_id`: A surrogate primary key used to uniquely identify each film in the table.

`title`: The title of the film.

`description`: A short description or plot summary of the film.

`release_year`: The year in which the movie was released.

`language_id`: A foreign key pointing at the language table; identifies the language of the film.

`original_language_id`: A foreign key pointing at the language table; identifies the original language of the film. Used when a film has been dubbed into a new language.

`rental_duration`: The length of the rental period, in days.

`rental_rate`: The cost to rent the film for the period specified in the rental_duration column.

`length`: The duration of the film, in minutes.

`replacement_cost`: The amount charged to the customer if the film is not returned or is returned in a damaged state.

`rating`: The rating assigned to the film. Can be one `of`: G, PG, PG-13, R, or NC-17.

`special_features`: Lists which common special features are included on the DVD. Can be zero or more `of`: Trailers, Commentaries, Deleted Scenes, Behind the Scenes.

`last_update`: When the row was created or most recently updated.


## film_actor

`actor_id`: A foreign key identifying the actor.

`film_id`: A foreign key identifying the film.

`last_update`: When the row was created or most recently updated.


## film_category

`film_id`: A foreign key identifying the film.

`category_id`: A foreign key identifying the category.

`last_update`: When the row was created or most recently updated.


## film_text

`film_id`: A surrogate primary key used to uniquely identify each film in the table.

`title`: The title of the film.

`description`: A short description or plot summary of the film.



## inventory

`inventory_id`: A surrogate primary key used to uniquely identify each item in inventory.

`film_id`: A foreign key pointing to the film this item represents.

`store_id`: A foreign key pointing to the store stocking this item.

`last_update`: When the row was created or most recently updated.


## language

`language_id`: A surrogate primary key used to uniquely identify each language.

`name`: The English name of the language.

`last_update`: When the row was created or most recently updated.


## payment

`payment_id`: A surrogate primary key used to uniquely identify each payment.

`customer_id`: The customer whose balance the payment is being applied to. This is a foreign key reference to the customer table.

`staff_id`: The staff member who processed the payment. This is a foreign key reference to the staff table.

`rental_id`: The rental that the payment is being applied to. This is optional because some payments are for outstanding fees and may not be directly related to a rental.

`amount`: The amount of the payment.

`payment_date`: The date the payment was processed.

`last_update`: When the row was created or most recently updated.


## rental

`rental_id`: A surrogate primary key that uniquely identifies the rental.

`rental_date`: The date and time that the item was rented.

`inventory_id`: The item being rented.

`customer_id`: The customer renting the item.

`return_date`: The date and time the item was returned.

`staff_id`: The staff member who processed the rental.

`last_update`: When the row was created or most recently updated.


## staff

`staff_id`: A surrogate primary key that uniquely identifies the staff member.

`first_name`: The first name of the staff member.

`last_name`: The last name of the staff member.

`address_id`: A foreign key to the staff member address in the address table.

`picture`: A BLOB containing a photograph of the employee.

`email`: The staff member email address.

`store_id`: The staff member “home store.” The employee can work at other stores but is generally assigned to the store listed.

`active`: Whether this is an active employee. If employees leave, their rows are not deleted from this table; instead, this column is set to FALSE.

`username`: The user name used by the staff member to access the rental system.

`password`: The password used by the staff member to access the rental system. The password should be stored as a hash using the SHA2() function.

`last_update`: When the row was created or most recently updated.


## store

`store_id`: A surrogate primary key that uniquely identifies the store.

`manager_staff_id`: A foreign key identifying the manager of this store.

`address_id`: A foreign key identifying the address of this store.

`last_update`: When the row was created or most recently updated.
